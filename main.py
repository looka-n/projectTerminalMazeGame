import random
import hero
import map
import beg_factory
import exp_factory

def input_get_range(prompt, low, high):
  val = 0
  valid = False
  while not valid:
    try:
      val = int(input(prompt))
      if val >= low and val <= high:
        valid = True
      else:
        print("Invalid input - should be within range " + str(low) + "-" + str(high) + ".")
    except ValueError:
      print("Invalid input - should be an integer.")
  return val

def main():
  '''The user navigates a grid in hopes of finding the finish whose location is unknown. They can encounter enemies that attack and Health Potions that heal them.'''
  #The player chooses their name and difficulty.
  name = input("What is your name, traveler? ")
  difficulty = "Difficulty:\n1. Beginner\n2. Expert\n"
  difficulty = input_get_range(difficulty, 1, 2)

  #Creates the hero object and map object.
  heroObject = hero.Hero(name)
  mapObject = map.Map()
  mapSelection = 1

  #Changes the map grid based on which level the player is on. Also, generates enemies based on difficulty chosen.
  mapObject.load_map(mapSelection)
  if (difficulty == 1):
    enemyFactory = beg_factory.BeginnerFactory()
  elif (difficulty == 2):
    enemyFactory = exp_factory.ExpertFactory()

  #Continuous loop that lets the player navigate and find .
  while True:
    #Prints the hero's name and current health.
    print(f"{heroObject}")
    #Prints the map.
    print(f"{mapObject.show_map(heroObject._loc)}")

    #The hero is prompted which direction they want to go and the option to quit.
    choice = "1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\nEnter choice: "
    choice = input_get_range(choice, 1, 5)
    positionValue = None
  
    if (choice == 1):
      mapObject.reveal(heroObject._loc)
      positionValue = heroObject.go_north()
    elif (choice == 2):
      mapObject.reveal(heroObject._loc)
      positionValue = heroObject.go_south()
    elif (choice == 3):
      mapObject.reveal(heroObject._loc)
      positionValue = heroObject.go_east()
    elif (choice == 4):
      mapObject.reveal(heroObject._loc)
      positionValue = heroObject.go_west()
    elif (choice == 5):
      print(f"\nGAME OVER\n{heroObject._name} fled like a coward and was exiled from Hyrule.")
      break

    #Entering a room has a unique consequence.
    #Enter start position
    if positionValue == "s":
      print("How'd we end up back here?\n")
    #Enter out of bounds
    elif positionValue == "x":
      print("Your clumsiness leads you to run into the wall.\n")
    #Enter empty room
    elif positionValue == "n":
      print("There is nothing here...\n")
    #Enter item room
    elif positionValue == "i":
      print("You found a Health Potion! You drink it to restore your health.\n")
      heroObject.heal()
      mapObject.remove_at_loc(heroObject._loc)
    #Enter monster encounter
    elif positionValue == "m":
      mapObject._revealed[heroObject._loc[0]][heroObject._loc[1]] = True
      enemyObject = enemyFactory.create_random_enemy()
      print("You encounter a ", end=f"{enemyObject}")
      while True:
        attackChoice = f"\n1. Attack {enemyObject._name}\n2. Run Away\nEnter choice: "
        attackChoice = input_get_range(attackChoice, 1, 2)
        #Attack
        if (attackChoice == 1):
          print(heroObject.attack(enemyObject))
          if enemyObject._hp <= 0:
            mapObject.remove_at_loc(heroObject._loc)
            print(f"You have slain the {enemyObject._name}\n")
            break
          print(enemyObject.attack(heroObject))
          print(f"\n{heroObject}\n{enemyObject}")
          if heroObject._hp <= 0:
            break
        #Run
        elif (attackChoice == 2):
          while True:
            runDirection = random.randint(1, 4)
            if runDirection == 1:
              if heroObject.go_north() != "x":
                break
            elif runDirection == 2:
              if heroObject.go_south() != "x":
                break
            elif runDirection == 3:
              if heroObject.go_east() != "x":
                break
            elif runDirection == 4:
              if heroObject.go_west() != "x":
                break
          break
    #Enter finish position. Changes map level and resets revealed locations.
    elif positionValue == "f":
      print(f"\nCongratulations! {heroObject._name} found the stairs to the next floor of the dungeon.\n------------------------------------------------------")
      mapSelection += 1
      if (mapSelection > 3):
        mapSelection = 1
      mapObject.load_map(mapSelection)

    #If the hero loses all of their health, they lose.
    if (heroObject._hp == 0):
      print(f"\nGAME OVER\n{heroObject._name} failed and was robbed of their rupees.")
      break

main()