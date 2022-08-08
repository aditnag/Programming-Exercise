import math


class Expression:
    def fac(self, n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

    def sum_of_exp(self, n, x):
        sum = 0
        for i in range(n+1):
            if i == 0:
                sum += 1
            else:
                sum += math.pow(x, i) * 1.0 / self.fac(i)
                # print(sum)
        return sum


n = int(input())
x = int(input())
e = Expression()
print(e.sum_of_exp(n, x))
