class CountSquares:

    def __init__(self):
        self.points = {}

        

    def add(self, point: List[int]) -> None:
        pointTup = (point[0], point[1])
        if pointTup not in self.points:
            self.points[(pointTup)] = 0
        self.points[(pointTup)] +=1 


    def count(self, point: List[int]) -> int:
        ret = 0
        for p in self.points.keys():
            # if this is positive, then the point is on the right
            x_diff = p[0] - point[0]
            y_diff = p[1] - point[1]

            if (abs(x_diff) == abs(y_diff)) and (x_diff !=0 and y_diff != 0):
                # consider the other points now
                newpt1 = (point[0], p[1])
                newpt2 = (p[0], point[1])
                if newpt1 in self.points and newpt2 in self.points:
                    ways = self.points[newpt1] * self.points[newpt2] * self.points[p]
                    ret += ways
        
        return ret


