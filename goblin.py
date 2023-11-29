import random
import entity

class Goblin(entity.Entity):
  '''Creates a goblin object.'''
  
  def __init__(self):
    '''Calls super on the Entity class with its unique name and HP.'''
    super().__init__("Vicious Goblin", random.randint(6, 10))

  def attack(self, entity):
    '''The entity attacks the hero, making them lose HP.'''
    damage = random.randint(4, 8)
    entity.take_damage(damage)
    return f"{self._name} attacks a {entity._name} for {damage} damage."