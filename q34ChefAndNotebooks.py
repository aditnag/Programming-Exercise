# cook your dish here
class ChefAndNotebooks:
    def lucky(self):
        t = int(input())
        for i in range(t):
            x, y, k, n = map(int, input().strip().split())
            books = []
            for j in range(n):
                p, c = map(int, input().strip().split())
                books.append((p, c))
            for p, c in books:
                if p >= x - y and c <= k:
                    print("LuckyChef")
                    break
            else:
                print("UnluckyChef")


obj = ChefAndNotebooks()
obj.lucky()
