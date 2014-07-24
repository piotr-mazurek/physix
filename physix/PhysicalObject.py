from Point3D import *
from itertools import combinations


class PhysicalObject():
    epsilon = 0.05
    rm = 0.8

    def __init__(self):
        self.points = []
        self.relations = []

    def lennard_jones(self, distance):
        try:
            result = self.epsilon * (
                (self.rm / float(distance)) ** 12 -
                2 * (self.rm / float(distance)) ** 6
            )
        except ZeroDivisionError:
            result = 0

        if distance > self.rm:
            return abs(result + self.epsilon)
        else:
            return abs(result + self.epsilon) * -1

    def force_function(self, distance_vector):
        distance_vector.setX(
            self.lennard_jones(distance_vector.getX())
        )
        distance_vector.setY(
            self.lennard_jones(distance_vector.getY())
        )
        distance_vector.setZ(
            self.lennard_jones(distance_vector.getZ())
        )
        return distance_vector

    def addPoint(self, point):
        self.points.append(point)

    def computeInternalForces(self):
        for p1, p2 in combinations(self.points, 2):
            position1 = p1.getPosition()
            position2 = p2.getPosition()
            delta1 = position1.getDelta(position2)
            force = self.force_function(delta1)
            force2 = force * -1
            p1.addForce(force)
            p2.addForce(force2)
            p1.computeAcceleration()
            p2.computeAcceleration()

    def move(self, dt):
        for point in self.points:
            point.move(dt)

    def get_points(self):
        return self.points

    def zero_force(self):
        for p in self.points:
            p.removeForces()
