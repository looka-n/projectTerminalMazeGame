import random
import entity

class EasyOgre(entity.Entity):
  '''Creates an easier ogre object.'''
  
  def __init__(self):
    '''Calls super on the Entity class with its unique name and HP.'''
    super().__init__("Ogre", random.randint(3, 5))

  def attack(self, entity):
    '''The entity attacks the hero, making them lose HP.'''
    damage = random.randint(1, 4)
    entity.take_damage(damage)
    return f"{self._name} attacks a {entity._name} for {damage} damage."