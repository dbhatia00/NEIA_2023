#
# player.py
#
# A Connect-Four Player class 
#  

from board import *

# write your class below.

class Player:
    """
    a Player class to represent a player of the Connect Four game
    """
    def __init__(self, checker):
        """
        Constructor for the player object
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        return 'Player ' + self.checker

    def opponent_checker(self):
        """
        returns a one-character string representing the
        checker of the Player object's opponent
        """
        if self.checker == "X":
            return "O"
        return "X"

    def next_move(self, b):
        """
        accepts a Board object b as a parameter and returns 
        the column where the player wants to make the next move
        """
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col):
                self.num_moves+=1
                break
            print('Try again!')
        
        return col

class RandomPlayer(Player):
    def next_move(self, b):
        """
        accepts a Board object b as a parameter and returns 
        a random column for the next move
        """
        while True:
            cols = [c for c in range(b.width) if b.slots[0][c] == " "]
            col = random.choice(cols)
            if b.can_add_to(col):
                self.num_moves+=1
                break
        return col

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """
        Constructor for the AI Player
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """
        Defines print stucture for AI Player obj
        """
        s=  super().__repr__()
        s = s + " (" + self.tiebreak + ", " + str(self.lookahead) + ")"
        return s

    def max_score_column(self, scores):
        """
        takes a list scores containing a score for each column of the board, 
        and that returns the index of the column with the maximum score
        """
        maxVal = max(scores)
        listBest = []
        for i in range(len(scores)):
            if maxVal == scores[i]:
                listBest += [i]
        
        if self.tiebreak == "RIGHT":
            return listBest[-1]
        elif self.tiebreak == "LEFT":
            return listBest[0]
        else:
            return listBest[random.choice(range(len(listBest)))]


    def scores_for(self, b):
        """
        returns a list containing one score for each column.
        """
        if self.checker == "X":
            otherChecker = "O"
        else:
            otherChecker = "X"

        scores = [0]*b.width
        for i in range(b.width):
            if b.slots[0][i] != " ":
                scores[i] = -1
            elif b.is_win_for(self.checker):
                scores[i] = 100
            elif b.is_win_for(otherChecker):
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                # LOOKAHEAD
                b.add_checker(self.checker, i)
                p2 = AIPlayer(otherChecker, self.tiebreak, self.lookahead-1)
                p2_scores = p2.scores_for(b)
                if max(p2_scores) == 100:
                    scores[i] = 0
                elif max(p2_scores) == 50:
                    scores[i] = 50
                else:
                    scores[i] = 100
                b.remove_checker(i)
        return scores


    def next_move(self, b):
        """
        determines the next move for the AI Player
        """
        self.num_moves+=1
        return self.max_score_column(self.scores_for(b))