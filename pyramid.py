class Pyramid:
    def findPattern(self, n):
        for i in range(1, n, 1):
            for j in range(n-1, 0, -1):
                print("#", end="")
            for k in range(0, i, 1):
                print("* ")
            # print("\r")


n = int(input())
py = Pyramid()
py.findPattern(n)
