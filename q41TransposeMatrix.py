# cook your dish here

class TransposeMatrix:
    def transpose(self, a, b, n, m):
        for i in range(m):
            for j in range(n):
                b[i][j] = a[j][i]
        return b

    def find_transpose(self):
        n, m = map(int, input().strip().split())
        matrix = []
        for i in range(n):
            matrix.append([int(j) for j in input().split()])
        mat = [[0 for x in range(n)] for y in range(m)]
        self.transpose(matrix, mat, n, m)

        for i in range(m):
            for j in range(n):
                print(mat[i][j], end=" ")
            print()


o = TransposeMatrix()
o.find_transpose()
