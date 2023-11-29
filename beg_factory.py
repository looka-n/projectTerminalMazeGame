import random
import enemy_factory
import easy_goblin
import easy_ogre
import easy_troll

class BeginnerFactory(enemy_factory.EnemyFactory):
  '''Generates beginner level enemies.'''

  def create_random_enemy(self):
    '''Generates a random enemy.'''
    type = random.randint(1,3)
    if (type == 1):
      easyGoblinObject = easy_goblin.EasyGoblin()
      return easyGoblinObject
    elif (type == 2):
      easyOgreObject = easy_ogre.EasyOgre()
      return easyOgreObject
    elif (type == 3):
      easyTrollObject = easy_troll.EasyTroll()
      return easyTrollObject