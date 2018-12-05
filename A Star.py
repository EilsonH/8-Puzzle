class Board:
    def __init__ (self, board):         #board is of type int list
        self.board = board

    def swap(self, i, j):
        self.board[i], self.board[j] = self.board[j], self.board[i]

    def moves(self):                    #moves produce a list of possible next moves
        p = []
        i = self.board.index('0')
        if i % 3 = 0 or i % 3 = 1:
            new_board = self
            p.append(new_board.swap(i, i + 1))
        if i % 3 = 1 or i % 3 = 2:
            new_board = self
            p.append(new_board.swap(i - 1, i))
        if i // 3 = 0 or i // 3 = 1:
            new_board = self
            p.append(new_board.swap(i, i + 3))
        if i // 3 = 1 or i // 3 = 2:
            new_board = self.board
            p.append(new_board.swap(i - 3, i))
        return p

    def md(self):                       #compute the Manhattan distance
        acc = 0
        for i in self.board:
            if i != 0:
                m = abs(self.board.index(i) - i + 1)
                acc += m // 3 + m % 3
        return acc

    def best_child(self):
        all_moves = self.moves()
        e = 
        for i in all_moves:
            if
