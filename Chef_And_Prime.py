from math import sqrt


class ChefAndPrime:
    def isPrime(self, n):
        if n < 2:
            return False
        e = int(sqrt(n))
        for i in range(2, e+1):
            if n % i == 0:
                return False
        return True

    def main(self):
        testCases = int(input())
        while testCases:
            numElements = int(input())
            elements = list(map(int, (input().strip().split())))[:numElements]
            sum = 0
            for i in range(len(elements)):
                if elements[i] == 0:
                    sum += 1
                else:
                    count = 0
                    while elements[i] > 0:
                        elements[i] //= 10
                        count += 1
                    sum += count
            if self.isPrime(sum):
                print("Yes")
            else:
                print("No")
            testCases -= 1


obj = ChefAndPrime()
obj.main()
