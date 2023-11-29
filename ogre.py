import random
import entity

class Ogre(entity.Entity):
  '''Creates an ogre object.'''
  
  def __init__(self):
    '''Calls super on the Entity class with its unique name and HP.'''
    super().__init__("Lumbering Ogre", random.randint(8, 12))

  def attack(self, entity):
    '''The entity attacks the hero, making them lose HP.'''
    damage = random.randint(6, 10)
    entity.take_damage(damage)
    return f"{self._name} attacks a {entity._name} for {damage} damage."