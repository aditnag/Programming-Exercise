# cook your dish here
class KitchenTimetable:
    def findStudents(self, a, b):
        count = 0
        for i in range(len(a)):
            if i == 0 and a[i] >= b[i]:
                count += 1
            elif a[i] - a[i - 1] >= b[i]:
                count += 1
        return count


o = KitchenTimetable()
n = int(input())
a = list(map(int, (input().strip().split())))[:n]
b = list(map(int, (input().strip().split())))[:n]
print(o.findStudents(a, b))

