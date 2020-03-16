class Coords:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  #unpacking operator (*) to get [x, y] as arguments
  def __getitem__(self, key):
    if key == 0:
      return self.x
    elif key == 1:
      return self.y
    else:
      raise IndexError("invalid key '{}'".format(key))


'''
#creates a coordinate generator that iterates over a matrix
def coord_gen(matrix, target):
  coords = []
  for y in range(len(matrix)):
    for x in range(len(matrix[y])):
      if matrix[y][x] == target:
        coords.append(Coords(x,y))

  def gen():
    yield from coords

  return gen
class GridShape:
  def __init__(self, gen):
    x_max = 0
    y_max = 0
    for coords in gen:
      if coords.x > x_max:
        x_max = coords.x
      if coords.y > y_max:
        y_max = coords.y
    self.x_max = x_max
    self.y_max = y_max
    self.gen = gen

  def gen_at(self, x, y):
    for coord in self.gen():
      yield Coords(x + coord.x, y + coord.y)
''' and None #block comment, not docstring



#creates a dimensional array with a list of given dimensions
def create_tensor(*dimensions, fill=0):
  if len(dimensions) == 0:
    return fill
  else:
    subdim = list(dimensions)
    dim = subdim.pop()
    array = []
    for _ in range(dim):
      array.append(create_tensor(*subdim, fill=fill))
    return array


#checks if a value is within a given min-max range
def in_range(val, min, max):
  return min <= val and val <= max


class Board:
  def __init__(self, width, height, blank=None):
    self.width = width
    self.height = height
    self.blank = blank
    self.matrix = create_tensor(width, height, fill=blank)

  def x_check(self, x):
    return in_range(x, 0, self.width-1)

  def y_check(self, y):
    return in_range(y, 0, self.height-1)

  def index_check(self, x, y):
    return self.x_check(x) and self.y_check(y)

  def get(self, x, y):
    if self.index_check(x,y):
      return self.matrix[y][x]
    else:
      return self.blank

  def set(self, x, y, val):
    if self.index_check(x,y):
      self.matrix[y][x] = val

  def is_open(self, x, y):
    if self.index_check(x,y):
      return self.matrix[y][x] == self.blank
    else:
      return False

  def can_place(self, shape):
    for coords in shape:
      if not self.is_open(*coords):
        return False
    return True

  def place(self, shape, fill):
    for coords in shape:
      self.set(*coords, fill)



class Ship:
  def __init__(self, length, id):
    self.length = length
    self.rot = 'right'
    self.id = id
    self.pos = None #coords where ship is placed

  @property
  def placed(self):
    return self.pos is not None

  def gen_right(self, x, y):
    for i in range(self.length):
      yield Coords(x+i, y)

  def gen_down(self, x, y):
    for i in range(self.length):
      yield Coords(x, y+i)

  def gen_from(self, x, y):
    if self.rot == 'right':
      yield from self.gen_right(x,y)
    elif self.rot == 'down':
      yield from self.gen_down(x,y)

  def gen(self):
    yield from self.gen_from(*self.pos)

  def rotate(self):
    if self.placed:
      raise raise AttributeError('cannot rotate ship while placed')

    if self.rot == 'right':
      self.rot = 'down'
    elif self.rot == 'down':
      self.rot = 'right'
    else:
      raise ValueError('Ship.rot was an unexpected value')

  def remove(self, board):
    if self.placed:
      board.place(self.gen(), board.blank)
      self.pos = None

  def can_place(self, board, x, y):
    return board.can_place(self.gen_from(x, y))

  def place(self, board, x, y):
    if self.can_place(board, x, y):
      board.place(self.gen_from(x, y), self.id)
      self.pos = Coords(x, y)
