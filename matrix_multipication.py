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

# OR
# import numpy as np
#
#
# class MatrixMultiplication:
#     def multiplication(self):
#         r1, c1 = map(int, input().strip().split())
#         entries1 = list(map(int, input().split()))
#         a = np.array(entries1).reshape(r1, c1)
#         r2, c2 = map(int, input().strip().split())
#         entries2 = list(map(int, input().split()))
#         b = np.array(entries2).reshape(r2, c2)
#         if c1 == r2:
#             c = [[0 for x in range(c2)] for y in range(r1)]
#             for i in range(r1):
#                 for j in range(c2):
#                     c[i][j] = 0
#                     for k in range(c1):
#                         c[i][j] += a[i][k] * b[k][j]
#             for i in range(r1):
#                 for j in range(c2):
#                     print(format(c[i][j], "<3"), end="")
#                 # print()
#         else:
#             print("IMPOSSIBLE")
#
#
# o = MatrixMultiplication()
# o.multiplication()

