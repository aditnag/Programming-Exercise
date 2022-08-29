# cook your dish here

class ChefAndRainbow:
    def rainbow(self):
        t = int(input())
        while t:
            n = int(input())
            ar = list(map(int, input().strip().split()))[:n]
            j = n // 2 - 1 if n % 2 == 0 else n // 2
            flag = 0
            prev = ar[0]
            i = 0
            k = 1
            col = []
            col.append(prev)
            if ar[0] == 1:
                while i <= n // 2 and n != 0:
                    if ar[i] == ar[n - 1 - i]:
                        i += 1
                        continue
                    else:
                        flag = 1
                        break
                while k <= j and flag == 0:
                    col.append(ar[k])
                    if ar[k] == prev:
                        k += 1
                        continue
                    elif prev < ar[k] <= 7 and ar[k] - prev == 1:
                        prev = ar[k]
                        k += 1
                    else:
                        flag = 1
                        break
            else:
                flag = 1
            elements = set(col)
            if flag == 0 and len(elements) == 7:
                print("yes")
            else:
                print("no")
            t -= 1


obj = ChefAndRainbow()
obj.rainbow()
