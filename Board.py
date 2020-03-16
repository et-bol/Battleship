import tkinter as tk

class Board:
    def __init__(self, master, width, height, blank=None):
        self.width = width
        self.height = height
        self.blank = blank
        self.grid = self.create_grid(master, width, height, fill=blank)

    def x_check(self, x):
        return self.in_range(x, 0, self.width - 1)

    def y_check(self, y):
        return self.in_range(y, 0, self.height - 1)

    def index_check(self, x, y):
        return self.x_check(x) and self.y_check(y)

    def get(self, x, y):
        if self.index_check(x, y):
            return self.grid[y][x]
        else:
            return self.blank

    def set(self, x, y, val):
        if self.index_check(x, y):
            self.grid[y][x] = val

    def is_open(self, x, y):
        if self.index_check(x, y):
            return self.grid[y][x] == self.blank
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

    def create_grid(self, master, *dimensions, fill=0):
        frame = tk.Frame(master)
        btn_grid = []






    # checks if a value is within a given min-max range
    def in_range(self, val, min, max):
        return min <= val and val <= max

