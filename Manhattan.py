import copy
class Board:
    def __init__ (self, board):         #board is of type int list
        self.board = board

    def swap(self, i, j):
        new = copy.deepcopy(self)
        new.board[i], new.board[j] = new.board[j], new.board[i]
        return new

    def __str__(self):
        new_board = [str(self.board[0:3]),str(self.board[3:6]),str(self.board[6:])]
        return '\n'.join(new_board)

    def moves(self):                    #moves produce a list of possible next moves
        p = []
        i = self.board.index(0)
        if i % 3 == 0 or i % 3 == 1:
            p.append(self.swap(i, i + 1))
        if i % 3 == 1 or i % 3 == 2:
            p.append(self.swap(i - 1, i))
        if i // 3 == 0 or i // 3 == 1:
            p.append(self.swap(i, i + 3))
        if i // 3 == 1 or i // 3 == 2:
            p.append(self.swap(i - 3, i))
        return p

    def md(self):                       #compute the Manhattan distance
        acc = 0
        for i in self.board:
            if i != 0:
                m = self.board.index(i)
                acc += abs(m % 3 - (i - 1) % 3) + abs(m // 3 - (i - 1) // 3)
        return acc

    def success(self):
        return self.board == [1,2,3,4,5,6,7,8,0]

def print_bc(bc):
    print('Begin')
    for e in bc:
        print(e)
        print('\n')
    print('End')

class Puzzle:
    def __init__(self, board_collection):   #board_collection is a list of boards
        self.bc = board_collection

    def __str__(self):
        lst = list(map(str,self.bc))
        return ('\n'*2).join(lst)

    def seen(self,n):
        for x in self.bc:
            if x.board == n.board:
                return True
        return False

    def best_child(self):
        last = self.bc[-1]
        all_moves = last.moves()
        best = None
        min = float('inf')
        for i in all_moves:
            if not self.seen(i):
                k = i.md()
                if k < min:
                    best = i
                    min = k
        return best

    def solution(self):
        last = self.bc[-1]
        if not last.success():
            self.bc.append(self.best_child())
            self.solution()
        return self

    def steps(self):
        return len(self.bc) - 1

x = Board([1,2,3,4,5,0,6,7,8])
y = Puzzle([x])
print(y.solution())
print(y.steps())
