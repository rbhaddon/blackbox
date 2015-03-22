'''
    Blackbox
'''

from grid import Grid

class BlackboxBoard(Grid):
    def __init__(self, *args, **kwargs):
        super(BlackboxBoard, self).__init__(*args, **kwargs)
        self._direction = None

    def ray(self, entry):
        '''
        Shoot a 'ray' through the board at the entry position
        '''
        pass

    def ord_to_cell(self, entry):
        '''
        Convert an ordinal value of the grid's perimeter to cell position
        '''
        if entry > (2 * self.width + 2 * self.height - 1) or entry < 0:
            raise ValueError("Value is out of range: %d" % entry)

        # Top row
        if entry < self.width:
            return (0, entry)

        # Last column
        if entry < (self.width + self.height):
            return (entry - self.width, self.width - 1)

        # Bottom row
        if entry < (self.width * 2 + self.height):
            return (self.height - 1, self.width - entry % (self.width + self.height) - 1)

        # First column
        if entry >= (self.width * 2 + self.height):
            return (self.height - entry % (self.width * 2 + self.height) - 1, 0)

    def cell_to_ord(self, cell):
        '''
        Convert a cell position to an ordinal value of the grid's perimeter

        A naive solution.  Needs to account for current direction of ray
        '''
        if not self.is_inbounds(cell):
            raise ValueError("Cell is out of bounds: %s." % str(cell))

        row, col = cell

        # Top row
        if row == 0:
            return col

        # Bottom row
        if row == self.height - 1:
            return self.width + self.height + (self.width - col - 1)

        # Last column
        if col == self.width - 1:
            return self.width + row

        # First column
        if col == 0:
            return self.width * 2 + self.height + self.height - row - 1
