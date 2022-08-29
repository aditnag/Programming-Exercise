# done for square matrix

class MatrixOpr:
    def multiplication(self):
        m, n, p = map(int, input().strip().split())
        a = [[int(input()) for x in range(n)] for y in range(m)]
        b = [[int(input()) for x in range(p)] for y in range(n)]
        c = [[0 for x in range(p)] for y in range(m)]
        for i in range(m):
            for j in range(p):
                c[i][j] = 0
                for k in range(n):
                    c[i][j] += a[i][k] * b[k][j]

        for i in range(m):
            for j in range(p):
                print(format(c[i][j], "<3"), end="")
            print()


m = MatrixOpr()
m.multiplication()
