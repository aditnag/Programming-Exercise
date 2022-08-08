class HCF:
    def find(self, a, b):
        m = min(a, b)
        gcd = 0
        for i in range(1, m+1):
            if a % i == 0 and b % i == 0:
                gcd = i
        print(gcd)


a = int(input())
b = int(input())
h = HCF()
h.find(a, b)
