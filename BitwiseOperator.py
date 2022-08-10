# cook your dish here
class BitwiseOperator:
    def findX(self, x):
        for i in range(x):
            a = i
            b = x - a
            if (a & b) + (a | b) == x:
                print(f"{a} {b}")
                break
            else:
                print(-1)


o = BitwiseOperator()
t = int(input())
while t:
    x = int(input())
    o.findX(x)
    t -= 1
