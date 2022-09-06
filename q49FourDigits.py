# cook your dish here
class FourDigits:
    def digits(self):
        n = int(input())
        m = n
        c = 0
        res = ""
        while m != 0:
            d = m % 10
            c += 1
            m = m // 10
        z = 4 - c
        for i in range(z):
            res += "0"
        if n == 0:
            print(res)
        else:
            print(res + str(n))


o = FourDigits()
o.digits()
