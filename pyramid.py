class Pyramid:
    def pattern(self, n):
        for i in range(1, n+1):
            for k in range(n, i, -1):
                print(" ", end="")
            for j in range(i):
                print("* ", end="")
            print()


i = int(input())
p = Pyramid()
p.pattern(i)
