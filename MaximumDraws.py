class Socks:
    def maxDraws(self, n):
        if 1 <= n <= 1000000:
            print(n + 1)


print("Enter the number of colours of socks in the drawer")
num = int(input())
socks = Socks()
socks.maxDraws(num)
