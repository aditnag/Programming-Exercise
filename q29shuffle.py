# cook your dish here
class Shuffle:
    def if_possible(self, r, c):
        if r % 2 == 0 and c % 2 == 0:
            return "YES"
        elif (r % 2 == 0 and c % 2 != 0) or (r % 2 != 0 and c % 2 == 0):
            return "NO"
        elif (r % 2 != 0) and (c % 2 != 0):
            return "NO"


o = Shuffle()
t = int(input())
while t:
    table = list(map(int, input().strip().split()))[:2]
    row = table[0]
    col = table[1]
    if row >= 2 and col >= 2:
        print(o.if_possible(row, col))
    t -= 1
