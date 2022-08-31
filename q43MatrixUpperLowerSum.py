class MatrixUpperLowerSum:
    def LowerSum(self, mat, n):
        sum = 0
        for i in range(n):
            for j in range(i+1):
                sum += mat[i][j]
        return sum

    def UpperSum(self, mat, n, m):
        sum = 0
        for i in range(n):
            for j in range(i, m):
                sum += mat[i][j]
        return sum

    def main(self):
        n, m = map(int, input().strip().split())
        mat = []
        for i in range(n):
            mat.append([int(j) for j in input().split()])
        print(self.UpperSum(mat, n, m))
        print(self.LowerSum(mat, n))


o = MatrixUpperLowerSum()
o.main()
