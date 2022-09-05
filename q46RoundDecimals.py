# cook your dish here
from math import trunc


class RoundDecimals:
    def nearest(self):
        s = input()
        d = trunc(float(s))
        if d > 0:
            sum = float(s) + 0.5
            if trunc(sum) == (d+1):
                print(trunc(sum))
            else:
                print(d)
        else:
            sum = float(s) + 0.5
            if trunc(sum) == (d + 1):
                print(trunc(sum))
            else:
                print(d)


o = RoundDecimals()
o.nearest()
