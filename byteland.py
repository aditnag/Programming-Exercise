# cook your dish here
class Byteland:
    def findGold(self, x, a, b):
        if a == x:
            x = b
            return x
        elif b == x:
            x = a
            return x
        else:
            return x


o = Byteland()
inp = list(map(int, input().strip().split()))[:3]
n = inp[0]
x = inp[1]
s = inp[2]
gold = x
while s:
    swap = list(map(int, input().strip().split()))[:2]
    a = swap[0]
    b = swap[1]
    if n >= a != b <= n:
        x = o.findGold(x, a, b)
    s -= 1
print(x)
