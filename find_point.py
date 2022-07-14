class Point:
    def __init__(self):
        self.px = None
        self.py = None
        self.qx = None
        self.qy = None

    def find_point(self, px, py, qx, qy):
        self.px = px
        self.py = py
        self.qx = qx
        self.qy = qy
        rx = 2*self.qx - self.px
        ry = 2*self.qy - self.py
        return rx, ry


try:
    px = int(float(input()))
    py = int(float(input()))
    qx = int(float(input()))
    qy = int(float(input()))
    if -100 <= px <= 100 and -100 <= py <= 100 and -100 <= qx <= 100 and -100 <= qy <= 100:
        point = Point()
        print(point.find_point(px, py, qx, qy))
    else:
        print("Numbers out of range")
except:
    print("Invalid input")
