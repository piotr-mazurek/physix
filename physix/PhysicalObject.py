from Point3D import *
from itertools import combinations


class PhysicalObject():
    def __init__(self):
        self.points = []
        self.relations = []
        self.force_function = lambda x: x

    def addPoint(self, point):
        self.points.append(point)

    # def computeInternalForces(self):
    #     for p1, p2 in combinations(self.points, 2):
    #         delta1 = p1.getDelta(p2)
    #         force = self.forceFunction(
    #             delta1.getMagnitude()
    #         )
    #         p1.applyForce(force)
    #         p2.applyForce(force)

    #         print p1, p2
