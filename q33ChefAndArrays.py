import array as arr


class ChefAndArrays:
    def findGreatest(self, a, b):
        ar = arr.array('i', [])
        for i in range(len(a)):
            suff = int(a[i] + b[i])
            pre = int(b[i] + a[i])
            if suff > pre:
                ar.append(suff)
            else:
                ar.append(pre)
        for i in range(len(ar)):
            print(ar[i], end=" ")
        print()


o = ChefAndArrays()
t = int(input())
while t:
    an = int(input())
    a = list(input().strip().split())[:an]
    bn = int(input())
    b = list(input().strip().split())[:bn]
    o.findGreatest(a, b)
    t -= 1
