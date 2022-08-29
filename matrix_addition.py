class MatrixOpr:
    def addMatrices(self):
        r, c = map(int, input().strip().split())
        x = [[int(input()) for x in range(c)] for y in range(r)]
        y = [[int(input()) for x in range(c)] for y in range(r)]
        z = [[0 for x in range(c)] for y in range(r)]
        for i in range(r):
            for j in range(c):
                z[i][j] = x[i][j] + y[i][j]
        for i in range(r):
            for j in range(c):
                print(format(z[i][j], "<3"), end="")
            print()
        print(z)


m = MatrixOpr()
m.addMatrices()
