import random
import entity

class EasyGoblin(entity.Entity):
  '''Creates an easier goblin object.'''
  
  def __init__(self):
    '''Calls super on the Entity class with its unique name and HP.'''
    super().__init__("Goblin", random.randint(3, 4))

  def attack(self, entity):
    '''The entity attacks the hero, making them lose HP.'''
    damage = random.randint(1, 3)
    entity.take_damage(damage)
    return f"{self._name} attacks a {entity._name} for {damage} damage."