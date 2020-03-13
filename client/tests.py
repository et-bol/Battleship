from base import *


#TESTS:
#Place, collide, remove, and rotate

print('\nTesting...\n')


def print_matrix(matrix):
  for array in matrix:
    for elem in array:
      print(str(elem), end=' ')
    print('')

#init
board = Board(6,6,blank=0)
ship1 = Ship(4,1)
ship1.rot = 'right'
ship2 = Ship(5,2)
ship2.rot = 'down'

#place right facing ship at 1,1
ship1.place(board, 1, 1)
print_matrix(board.matrix)
print()

#ship fails to place, as it collides with ship 1
print(board.can_place(ship2.gen(2,0)))
ship2.place(board, 2, 0)
print_matrix(board.matrix)
print()

#remove ship 1
ship1.remove(board)

#same code as before, but ship 2 successfully places
print(board.can_place(ship2.gen(2,0)))
ship2.place(board, 2, 0)
print_matrix(board.matrix)
print()

#rotate and place ship 1
ship1.rot = 'down'
ship1.place(board, 4, 2)
print_matrix(board.matrix)
