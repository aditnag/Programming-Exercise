# cook your dish here
class CopsandThief:
    def escape(self):
        m, x, y = map(int, input().strip().split())
        copHouse = list(map(int, input().strip().split()))[:m]
        h = []
        a = 1
        s = []
        for i in range(100):
            h.append(a)
            a += 1
        for i in copHouse:
            ll = i - x*y
            ul = i + x*y
            for j in range(ll, ul+1):
                if 0 < j <= 100:
                    s.append(j)

        distinct = set(s)
        h = list(distinct)
        print(100 - len(h))


o = CopsandThief()
o.escape()
