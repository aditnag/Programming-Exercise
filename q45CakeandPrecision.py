# cook your dish here
# ith min ====> 2^i
# total time taken to bake = a
# a ====> 2^a
# k ====> 2^a/2
# k+2 ====> (2^a/2)*4
class CakeandPrecison:
    def find(self):
        t = int(input())
        while t:
            a = int(input())
            print(a + 1)
            t -= 1


o = CakeandPrecison()
o.find()
