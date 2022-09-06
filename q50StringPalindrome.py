class Palindrome:
    def find(self):
        s = list(input())
        n = len(s)
        p = 0
        q = n-1
        c = 0
        while p <= q:
            if s[p] != s[q]:
                c += 1
            p += 1
            q -= 1
        print(c)


o = Palindrome()
o.find()
