class Strong:
    def fac(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f

    def main(self, m):
        n = m
        if n == 0:
            return False
        d = 0
        sum = 0
        while n != 0:
            d = n % 10
            f = self.fac(d)
            sum += f
            n = n // 10
        if sum == m:
            return True
        else:
            return False


n = int(input())
f = Strong()
print(f.main(n))
