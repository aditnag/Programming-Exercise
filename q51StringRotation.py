# cook your dish here
class StringRotation:
    def find(self):
        s = list(input())
        slen = len(s)
        t = list(input())
        flag = 0
        for i in range(slen):
            end_ele = s.pop()
            s.insert(0, end_ele)
            if s == t:
                flag = 1
        if flag == 1:
            print("Yes")
        else:
            print("No")


o = StringRotation()
o.find()
