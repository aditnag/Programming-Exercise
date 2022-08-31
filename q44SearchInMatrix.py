# cook your dish here
class SearchinMatrix:
    def search(self):
        n, m = map(int, input().strip().split())
        mat = []
        for i in range(n):
            mat.append([int(j) for j in input().split()])
        target = int(input())
        flag = 0
        for i in range(n):
            for j in range(m):
                if target == mat[i][j]:
                    flag = 1
                    break
                else:
                    continue
        if flag == 1:
            print("true")
        else:
            print("false")


o = SearchinMatrix()
o.search()
