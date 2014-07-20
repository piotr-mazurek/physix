from Point3D import *
from itertools import combinations


class PhysicalObject():
    def __init__(self):
        self.points = []
        self.relations = []

    def force_function(self, distance_vector):
        distance_vector.setX(
            distance_vector.getX() ** 2
        )
        distance_vector.setY(
            distance_vector.getY() ** 2
        )
        distance_vector.setZ(
            distance_vector.getZ() ** 2
        )
        return distance_vector

    def addPoint(self, point):
        self.points.append(point)

    def computeInternalForces(self):
        for p1, p2 in combinations(self.points, 2):
            delta1 = p1.getDelta(p2)
            delta2 = p2.getDelta(p1)
            force = self.force_function(delta1)
            force2 = self.force_function(delta2)
            p1.addForce(force)
            p2.addForce(force2)

            print p1, p2
