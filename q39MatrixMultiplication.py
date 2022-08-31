# cook your dish here
class MatrixMultiplication:
    def multiplication(self):
        r1, c1 = map(int, input().strip().split())
        entries1 = list(map(int, input().split()))
        k = 0
        a = [[0 for _ in range(c1)] for _ in range(r1)]
        for i in range(r1):
            for j in range(c1):
                a[i][j] = entries1[k]
                k += 1
        r2, c2 = map(int, input().strip().split())
        entries2 = list(map(int, input().split()))
        k = 0
        b = [[0 for _ in range(c2)] for _ in range(r2)]
        for i in range(r2):
            for j in range(c2):
                b[i][j] = entries2[k]
                k += 1
        if c1 == r2:
            c = [[0 for x in range(c2)] for y in range(r1)]
            for i in range(r1):
                for j in range(c2):
                    c[i][j] = 0
                    for k in range(c1):
                        c[i][j] += a[i][k] * b[k][j]
            for i in range(r1):
                for j in range(c2):
                    print(c[i][j], end=" ")
                # print()
        else:
            print("IMPOSSIBLE")


o = MatrixMultiplication()
o.multiplication()
