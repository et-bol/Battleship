from base import Board, Ship

#peg states
EMPTY = 0
MISS = -1
HIT = 1

class Player:
  def __init__(self, shiplengths):
    self.field = Board(10, 10) #place ships
    self.shots = Board(10, 10, blank=EMPTY) #player attacks
    self.hit = Board(10, 10, blank=EMPTY) #opponent attacks

    self.ships = []
    for i in range(len(shiplengths)):
      self.ships.append(Ship(shiplengths[i], i))

  @property
  def ready(self):
    for ship in self.ships:
      if not ship.placed:
        return False
    return True

  #checks if a ship is sunk
  def is_sunk(self, shipID):
    ship = self.ships[shipID]
    for coords in ship.gen():
      if self.field.get(*coords) is ship.id:
        return False
    return True

  #checks if all ships are sunk
  @property
  def is_dead(self):
    for i in range(len(self.ships)):
      if not self.is_sunk(i):
        return False
    return True

  #receive data from opponent
  def hit(self, x, y, callback=None):
    spot = self.field.get(x, y)
    if spot is self.field.blank:
      self.hit.set(x, y, MISS)
    else:
      self.hit.set(x, y, HIT)

      if self.is_sunk(spot) and callback is not None:
          callback(spot)
