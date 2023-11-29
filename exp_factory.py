import random
import enemy_factory
import goblin
import ogre
import troll

class ExpertFactory(enemy_factory.EnemyFactory):
  '''Generates expert level enemies.'''

  def create_random_enemy(self):
    '''Generates a random enemy.'''
    type = random.randint(1,3)
    if (type == 1):
      goblinObject = goblin.Goblin()
      return goblinObject
    elif (type == 2):
      ogreObject = ogre.Ogre()
      return ogreObject
    elif (type == 3):
      trollObject = troll.Troll()
      return trollObject