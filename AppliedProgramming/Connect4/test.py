from connect4 import *

def test():
    '''
        USAGE: connect_four(playertype, playertype)
        There are currently three types of players:
            AIPlayer(marker type, biasing (right, left, or rand), lookahead) 
            RandomPlayer(marker)
            Player(marker)
    '''
    #connect_four(AIPlayer('X', 'RIGHT', 5), AIPlayer('O', 'RANDOM', 5))
    connect_four(Player('X'), AIPlayer('O', 'RANDOM', 5))

test()