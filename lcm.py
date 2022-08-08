class LCM:
    def lcm(self, a, b):
        m = max(a, b)
        l = 1
        while True:
            if m % a == 0 and m % b == 0:
                l = m
                break
            m += 1
        print(l)


a = int(input())
b = int(input())
h = LCM()
h.lcm(a, b)
