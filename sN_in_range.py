class Range:
    def fac(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f

    def main(self, n):
        num = 1
        while num <= n:
            temp = num
            if temp == 0:
                return False
            sum = 0
            while temp != 0:
                d = temp % 10
                f = self.fac(d)
                sum += f
                temp = temp // 10
            if sum == num:
                print(num)
            num += 1


i = int(input())
r = Range()
r.main(i)
