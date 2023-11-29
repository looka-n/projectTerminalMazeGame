class Map:
  '''Creates a map object.'''

  _instance = None
  _initialized = False
  
  def __new__(cls):
    '''Creates an instance of the class if one hasn't already been created.'''
    if (cls._instance is None):
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    '''Creates an empty map and revealed map list. If a map object has already been created.'''
    if not Map._initialized:
      self._map = []
      self._revealed = []
      Map._initialized = True

  def load_map(self, map_num):
    '''Loads the map based on what level the player is at and resets the revealed map to all False.'''
    #Reads the given "map.txt" and creates a 2D list based on the contents of its individual lines
    if (map_num == 1):
      mapFile = open("map1.txt")
    elif (map_num == 2):
      mapFile = open("map2.txt")
    elif (map_num == 3):
      mapFile = open("map3.txt")
    mapList = mapFile.readlines()
    self._map = [[] for x in range(5)]
    for x in mapList:
      x.replace("\n", "")
      self._map[0].append(x[0])
      self._map[1].append(x[1])
      self._map[2].append(x[2])
      self._map[3].append(x[3])
      self._map[4].append(x[4])
    #Creates a 2D list of the same size, but filled with booleans initially set to False.
    self._revealed = [[False for i in range(5)] for j in range(5)]
  
  def __getitem__(self, row):
    '''Returns the specified row from the map.'''
    pass
  
  def __len__(self):
    '''Returns the number of rows in the map list.'''
    return len(self._revealed)
  
  def show_map(self, loc):
    '''Displays the map to the hero indicating their position and what has/hasn't been explored yet.'''
    #Denotes the hero's position with "*"
    row = loc[0]
    column = loc[1]
    self._revealed[row][column] = "*"

    #Replaces True values with corresponding room.
    lineReset = 0
    for x in range(5):
      for y in range(5):
        if (self._revealed[x][y] == True):
          self._revealed[x][y] = self._map[x][y]
    #Replaces False values with "x."
    for x in self._revealed:
      for y in x:
        if (y == False):
          y = "x"
        print(y, end=" ")
        lineReset += 1
        if (lineReset == 5):
          print("")
          lineReset = 0
    return ""
  
  def reveal(self, loc):
    '''Changes the specified position in the revealed map to True.'''
    row = loc[0]
    column = loc[1]
    self._revealed[row][column] = True
  
  def remove_at_loc(self, loc):
    '''Replaces the specified position with an "n."'''
    row = loc[0]
    column = loc[1]
    self._map[row][column] = "n"