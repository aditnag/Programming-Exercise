# cook your dish here
class GameWithCells:
    def findMinDrop(self, n, m):
        if n * m % 4 == 0:
            numOfPackages = n * m // 4
        elif n * m % 4 == 1:
            numOfPackages = n * m // 4 + 1
        elif n * m % 4 == 2:
            numOfPackages = n * m // 4 + 1
        elif n * m % 4 == 3:
            numOfPackages = n * m // 4 + 1
        return numOfPackages


inp = input()
i = inp.split()
n = int(i[0])
m = int(i[1])

game = GameWithCells()
print(game.findMinDrop(n, m))
