class PointsOperation:
    def find_point(self, px, py, qx, qy):
        print(2 * qx - px, 2 * qy - py)


inp = input()
i = inp.split()
# print(i)
px = int(i[0])
py = int(i[1])
qx = int(i[2])
qy = int(i[3])
point = PointsOperation()
point.find_point(px, py, qx, qy)
