class MatrixOpr:
    def addDiadonals(self):
        r, c = map(int, input().strip().split())
        matrix = [[0 for x in range(c)] for y in range(r)]
        for i in range(r):
            for j in range(c):
                matrix[i][j] = int(input())

        for i in range(r):
            for j in range(c):
                print(format(matrix[i][j], "<3"), end="")
            print()

        pi = 0
        pj = 0
        si = 0
        sj = r - 1
        sum_primary = 0
        sum_secondary = 0
        while pi < r and pj < c:
            sum_primary += matrix[pi][pj]
            pi += 1
            pj += 1
        print(f"Sum of Primary diagonal = {sum_primary}")

        while si < r and sj >= 0:
            sum_secondary += matrix[si][sj]
            si += 1
            sj -= 1
        print(f"Sum of Secondary diagonal = {sum_secondary}")


m = MatrixOpr()
m.addDiadonals()
