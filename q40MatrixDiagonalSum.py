# cook your dish here

class MatrixDiagonal:
    def dsum(self):
        n, m = map(int, input().strip().split())
        mat = []
        for i in range(n):
            mat.append([int(j) for j in input().split()])

        sum_rd = 0
        sum_ld = 0
        ri = 0
        rj = 0
        li = 0
        lj = m - 1
        while ri < n and rj < m:
            sum_rd += mat[ri][rj]
            ri += 1
            rj += 1

        while li < n and lj >= 0:
            sum_ld += mat[li][lj]
            li += 1
            lj -= 1

        if n * m % 2 == 0:
            print(sum_ld + sum_rd)
        else:
            print(sum_ld + sum_rd - mat[n // 2][n // 2])


o = MatrixDiagonal()
o.dsum()
