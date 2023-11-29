import abc

class Entity(abc.ABC):

    def __init__(self, name, max_hp):
      '''Creates an Entity object with a name and HP.'''
      self._name = name
      self.max_hp = max_hp
      self._hp = max_hp

    @property
    def name():
      '''Gets the entity's name.'''
      return self._name
    @property
    def hp():
      '''Gets the entity's HP.'''
      return self._hp

    def take_damage(self, dmg):
      '''Removes the entity's HP based on the amount of damage it takes.'''
      self._hp -= dmg
      if (self._hp < 0):
        self._hp = 0

    def heal(self):
      '''Heals the entity to its maximum health.'''
      self._hp = self.max_hp

    def __str__(self):
      '''Returns a string displaying the entity's name and current HP.'''
      return f"{self._name}\nHP: {self._hp}/{self.max_hp}"

    @abc.abstractmethod
    def attack(self, entity):
      '''Defines an abstract method where the entity attacks another entity.'''
      pass