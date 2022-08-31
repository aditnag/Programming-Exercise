class MatrixAddition:
    def add(self, a, b, n, m):
        c = [[0 for x in range(m)] for y in range(n)]
        for i in range(n):
            for j in range(m):
                c[i][j] = a[i][j] + b[i][j]
        return c

    def matrixaddition(self):
        n1, m1 = map(int, input().strip().split())
        matrixA = []
        for i in range(n1):
            matrixA.append([int(j) for j in input().split()])

        n2, m2 = map(int, input().strip().split())
        matrixB = []
        for i in range(n2):
            matrixB.append([int(j) for j in input().split()])

        if n1 == n2 and m1 == m2:
            matrixC = self.add(matrixA, matrixB, n1, m1)
            for i in range(m1):
                for j in range(n1):
                    print(matrixC[i][j], end=" ")
                print()


o = MatrixAddition()
o.matrixaddition()
