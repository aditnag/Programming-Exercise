# cook your dish here
class KingMovement:
    def numOfMoves(self):
        t = int(input())
        while t:
            r, c, k = map(int, input().strip().split())
            moves = 0
            if 1 <= r <= 8 and 1 <= c <= 8:
                for i in range(1, 9):
                    for j in range(1, 9):
                        if max(abs(i-r), abs(j-c)) <= k:
                            moves += 1
            print(moves)
            t -= 1


o = KingMovement()
o.numOfMoves()
