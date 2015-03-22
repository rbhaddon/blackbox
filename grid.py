'''
    Grid - a grid implementation for board games

'''

import copy
import random

class Grid(object):
    def __init__(self, width, height, board=None):
        self.default = '-'
        self.fill = '*'
        self.set_list = set()
        if board is not None:
            self._height = len(board)
            self._width = len(board[0])
            self._grid = board
        else:
            self._width = width
            self._height = height
            self._grid = self._make_grid()

    def __len__(self):
        return self.height * self.width

    def __repr__(self):
        lines = []
        lines.append("  " + "".join(["%2d" % col for col in range(self.width)]))
        for num, row in enumerate(self._grid):
            lines.append("%2d" % num + "".join(["%2s" % element for element in row]))
        return "\n".join(lines)

    def _make_grid(self):
        '''
        Make a new grid
        '''
        return [[self.default for col in range(self.width)] for row in range(self.height)]

    @property
    def height(self):
        '''
        Return the height of the grid
        '''
        return self._height

    @height.setter
    def height(self, value):
        '''
        Change grid height and reset grid
        '''
        self._height = value
        self.clear()

    @property
    def width(self):
        '''
        Return the width of the grid
        '''
        return self._width

    @width.setter
    def width(self, value):
        '''
        Change grid width and reset grid
        '''
        self._width = value
        self.clear()

    @property
    def count(self):
        '''
        Return the number of set positions in the grid
        '''
        return len(self.set_list)

    def is_empty(self, cell):
        '''
        Return True if the given grid position is clear, else false
        '''
        row, col = cell
        return self._grid[row][col] == self.default

    def is_full(self, cell):
        '''
        Return True if the given grid position is set, else false
        '''
        row, col = cell
        return self._grid[row][col] == self.fill

    def set_pos(self, cell):
        '''
        Set the given grid position
        '''
        row, col = cell
        self._grid[row][col] = self.fill
        self.set_list.add(cell)

    def clear_pos(self, cell):
        '''
        Clear the given grid position
        '''
        row, col = cell
        self._grid[row][col] = self.default
        try:
            self.set_list.remove(cell)
        except KeyError:
            pass

    def is_inbounds(self, cell):
        '''
        Check if cell is within grid
        '''
        row, col = cell
        return (0 <= row < self.height) and (0 <= col < self.width)

    def clear(self):
        '''
        Clear the grid
        '''
        self.set_list.clear()
        self._grid = self._make_grid()

    def shuffle(self, num):
        '''
        Clear the grid and set num positions randomly
        '''
        if num > len(self):
            raise ValueError("Value out of range: %r" % num)
        self.clear()
        while len(self.set_list) < num:
            new_pos = ((random.randrange(self.width), random.randrange(self.height)))
            self.set_pos(new_pos)

    def clone(self):
        '''
        Return a shallow copy of this grid()
        '''
        return copy.copy(self)

