import random
import entity

class Troll(entity.Entity):
  '''Creates a troll object.'''
  
  def __init__(self):
    '''Calls super on the Entity class with its unique name and HP.'''
    super().__init__("Tremendous Troll", random.randint(10, 14))

  def attack(self, entity):
    '''The entity attacks the hero, making them lose HP.'''
    damage = random.randint(8, 12)
    entity.take_damage(damage)
    return f"{self._name} attacks a {entity._name} for {damage} damage."