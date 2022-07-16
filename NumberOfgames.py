# cook your dish here
class Mist:
    def numOfGames(self, p, d, m, s):
        count = 0
        while s >= p:
            s = s - p
            count += 1
            p = max(m, p - d)
        return count


inp = input()
i = inp.split()
p = int(i[0])
d = int(i[1])
m = int(i[2])
s = int(i[3])
obj = Mist()
print(obj.numOfGames(p, d, m, s))
