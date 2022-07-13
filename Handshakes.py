class Handshakes:

    def handshake(self, n):
        hs = 0
        for i in range(n - 1):
            hs = hs + (n - 1)
            n = n - 1
        print(hs)


numOfPeople = int(input())
if 1 <= numOfPeople <= 1000000:
    obj = Handshakes()
    obj.handshake(numOfPeople)
else:
    print("Number of people out of range")
