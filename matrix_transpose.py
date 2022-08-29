# done for square matrix

class MatrixOpr:
    def transpose(self):
        r, c = map(int, input().strip().split())
        matrix = [[0 for x in range(c)] for y in range(r)]
        for i in range(r):
            for j in range(c):
                matrix[i][j] = int(input())

        for i in range(r):
            for j in range(c):
                print(format(matrix[i][j], "<3"), end="")
            print()
        print("**********")
        for i in range(r):
            for j in range(i, c):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(r):
            for j in range(c):
                print(format(matrix[i][j], "<3"), end="")
            print()





m = MatrixOpr()
m.transpose()
