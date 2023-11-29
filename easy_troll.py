import random
import entity

class EasyTroll(entity.Entity):
  '''Creates an easier troll object.'''
  
  def __init__(self):
    '''Calls super on the Entity class with its unique name and HP.'''
    super().__init__("Troll", random.randint(4, 5))

  def attack(self, entity):
    '''The entity attacks the hero, making them lose HP.'''
    damage = random.randint(1, 5)
    entity.take_damage(damage)
    return f"{self._name} attacks a {entity._name} for {damage} damage."