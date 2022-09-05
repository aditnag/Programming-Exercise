class SumofRotatedStrings:
    def find(self):
        num = input()
        l = list(num)
        a = int(l[0])
        b = int(l[1])
        c = int(l[2])
        x = 100*a+10*b+1*c
        y = 100*b+10*c+1*a
        z = 100*c+10*a+1*b
        print(x+y+z)


o = SumofRotatedStrings()
o.find()
