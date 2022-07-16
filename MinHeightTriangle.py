# cook your dish here
from math import ceil


class Triangle:
    def findHeight(self, b, a):
        return ceil(2 * a / b)


inp = input()
i = inp.split()
b = int(i[0])
a = int(i[1])
obj = Triangle()
print(obj.findHeight(b, a))
