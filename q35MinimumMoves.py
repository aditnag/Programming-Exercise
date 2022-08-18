# cook your dish here
import sys


class MinimumMoves:
    def moves(self):
        n = int(input())
        salary = list(map(int, (input().strip().split())))[:n]
        moves = 0
        min = sys.maxsize
        for i in salary:
            min = (i if i < min else min)
        for j in salary:
            moves += j - min
        print(moves)


obj = MinimumMoves()
obj.moves()
