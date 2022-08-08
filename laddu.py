# cook your dish here
class Laddu:
    def find(self, activities, origin):
        sum = 0
        for i in range(int(activities)):
            data = input().strip().split()
            category = data[0]
            if category == "CONTEST_WON":
                rank = int(data[1])
                bonus = max(0, 20 - rank)
                sum += 300 + bonus
            if category == "TOP_CONTRIBUTOR":
                sum += 300
            if category == "BUG_FOUND":
                s = int(data[1])
                sum += s
            if category == "CONTEST_HOSTED":
                sum += 50
        print(sum // (200 if origin == "INDIAN" else 400))


o = Laddu()
t = int(input())
while t:
    activities, origin = map(str, input().strip().split())
    o.find(activities, origin)
    t -= 1
