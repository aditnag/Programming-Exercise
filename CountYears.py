# cook your dish here
class Years():
    def find(self, a, b):
        year = 0
        while (a <= b):
            a = 3 * a
            b = 2 * b
            year += 1
        return year


inp = input()
i = inp.split()
obj = Years()
print(obj.find(int(i[0]), int(i[1])))