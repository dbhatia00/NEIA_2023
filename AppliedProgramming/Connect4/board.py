#
# board.py
#
# A Connect Four Board class
#
# NEIA Winter Enrichment
#

import random

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        """
        Constructor for the board object
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        for i in range(self.width*2 + 1):
            s+="-"
        s+="\n"
        for i in range(self.width):
            s = s+ " " + str(i%10)
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        for i in range(self.height-1, -1, -1):
            if self.slots[i][col] not in 'XO':
                self.slots[i][col] = checker
                break
    
    ### add your reset method here ###
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here

    def remove_checker(self, col):
        """
        Removes the top checker from col
        """
        for i in range(self.height):
            if (self.slots[i][col] == "X") or (self.slots[i][col] == "O"):
                self.slots[i][col] = " "
                break

    def reset(self):
        """
        Resets the board
        """
        self = self.__init__(self.height, self.width)

    def can_add_to(self, col):
        """
        returns True if it is valid to place a checker in
        the column col on the calling Board object
        """
        if (0 <= col < self.width) and (self.slots[0][col] == ' '):
            return True
        return False

    def is_full(self):
        """
        returns True if the called Board object is completely full of checkers
        """
        for i in range(self.width):
            if self.can_add_to(i):
                return False
        return True

    def is_win_for(self, checker):
        """
        returns True if there are four consecutive slots containing checker on the board
        """
        assert(checker == 'X' or checker == 'O')  

        #colcheck
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                self.slots[row][col + 1] == checker and \
                self.slots[row][col + 2] == checker and \
                self.slots[row][col + 3] == checker:
                    return True

        #rowCheck
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                self.slots[row+1][col] == checker and \
                self.slots[row+2][col] == checker and \
                self.slots[row+3][col] == checker:
                    return True

        #diagCheck (Downwards)
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                self.slots[row+1][col+1] == checker and \
                self.slots[row+2][col+2] == checker and \
                self.slots[row+3][col+3] == checker:
                    return True
        
        #diagCheck (Upwards)
        for row in range(3, self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                self.slots[row-1][col+1] == checker and \
                self.slots[row-2][col+2] == checker and \
                self.slots[row-3][col+3] == checker:
                    return True


        # if we make it here, there were no horizontal wins
        return False

