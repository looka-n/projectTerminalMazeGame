import random
import entity
import map

class Hero(entity.Entity):
  '''Creates a Hero object based on the Entity class.'''
    
  def __init__(self, name):
    '''Gives the hero a name, HP, and defines its location relative to the map.'''
    super().__init__(name, 25)
    self._loc = [0, 0]

  @property
  def loc():
    '''Gets the hero's location.'''
    return self._loc
    
  def attack(self, entity):
    '''Attacks the hero for a random amount of damage.'''
    damage = random.randint(2, 5)
    entity.take_damage(damage)
    return f"{self._name} attacks a {entity._name} for {damage} damage."

  def go_north(self):
    '''The hero moves north on the map.'''
    mapObject = map.Map()
    if (self._loc[0] - 1 < 0):
      return "x"
    else:
      self._loc[0] -= 1
      return mapObject._map[self._loc[0]][self._loc[1]]

  def go_south(self):
    '''The hero moves south on the map.'''
    mapObject = map.Map()
    if (self._loc[0] + 1 > 4):
      return "x"
    else:
      self._loc[0] += 1
      return mapObject._map[self._loc[0]][self._loc[1]]

  def go_east(self):
    '''The hero moves east on the map.'''
    mapObject = map.Map()
    if (self._loc[1] + 1 > 4):
      return "x"
    else:
      self._loc[1] += 1
      return mapObject._map[self._loc[0]][self._loc[1]]

  def go_west(self):
    '''The hero moves west on the map.'''
    mapObject = map.Map()
    if (self._loc[1] - 1 < 0):
      return "x"
    else:
      self._loc[1] -= 1
      return mapObject._map[self._loc[0]][self._loc[1]]