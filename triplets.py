# cook your dish here
class Triplets():
    def compare(self, ac, ao, ad, bc, bo, bd):
        a_point = 0
        b_point = 0
        if ac > bc:
            a_point += 1
        elif ac < bc:
            b_point += 1
        else:
            pass
        if ao > bo:
            a_point += 1
        elif ao < bo:
            b_point += 1
        else:
            pass
        if ad > bd:
            a_point += 1
        elif ad < bd:
            b_point += 1
        else:
            pass
        print(a_point, b_point)


alice_inp = input()
bob_inp = input()
a_inp = alice_inp.split()
b_inp = bob_inp.split()
a_clarity = int(a_inp[0])
a_originality = int(a_inp[1])
a_diff = int(a_inp[2])
b_clarity = int(b_inp[0])
b_originality = int(b_inp[1])
b_diff = int(b_inp[2])

obj = Triplets()
obj.compare(a_clarity, a_originality, a_diff, b_clarity, b_originality, b_diff)
