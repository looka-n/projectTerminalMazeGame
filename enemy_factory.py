import abc

class EnemyFactory(abc.ABC):
  '''Creates enemies that the hero will go against.'''

  @abc.abstractmethod
  def create_random_enemy(self):
    '''Creates an abstract method that will overridden to generate enemies.'''
    pass