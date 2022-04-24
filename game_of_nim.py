from games import *

class GameOfNim(Game):

    def __init__(self, board):
        self.board = board
        moves = []
        for idx, item in enumerate(board):
            if item > 0:
                moves.extend([(idx, i) for i in range(1, item+1)])

        self.initial = GameState(
            to_move='MAX',
            utility=0,
            board=board, 
            moves=moves
            )

    def actions(self, state):
        return state.moves

    def result(self, state, move):

        board = state.board.copy()
        board[move[0]] = board[move[0]] - move[1]
        
        moves = []
        for idx, item in enumerate(board):
            if item > 0:
                moves.extend([(idx, i) for i in range(1, item+1)])

        return GameState(to_move=('MIN' if state.to_move == 'MAX' else 'MAX'),
                        utility=0,
                        board=board,
                        moves=moves)

    def utility(self, state, player):
        return state.utility if player == 'MAX' else -state.utility

if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1])
    #nim = GameOfNim(board=[7, 5, 3, 1])
    print(nim.initial.board)
    print(nim.initial.moves)
    print(nim.result(nim.initial, (1,3)))
    utility = nim.play_game(alpha_beta_player, query_player)
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
