# cook your dish here
class ForgottenLanguage:
    def inUse(self):
        n, k = map(int, (input().strip().split()))
        s = list(input().strip().split())[:n]
        ar = []
        for i in range(k):
            l = list(input().strip().split())
            size = int(l[0]) + 1
            for j in range(1, size):
                ar.append(l[j])
        for i in range(n):
            word = s[i]
            for j in range(len(ar)):
                if word == ar[j]:
                    print("YES", end=" ")
                    break
            else:
                print("NO", end=" ")


o = ForgottenLanguage()
o.inUse()
