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
        distance_vector.set_x(
            self.lennard_jones(distance_vector.get_x())
        )
        distance_vector.set_y(
            self.lennard_jones(distance_vector.get_y())
        )
        distance_vector.set_z(
            self.lennard_jones(distance_vector.get_z())
        )
        return distance_vector

    def add_point(self, point):
        self.points.append(point)

    def compute_internal_forces(self):
        for p1, p2 in combinations(self.points, 2):
            position1 = p1.get_position()
            position2 = p2.get_position()
            delta1 = position1.get_delta(position2)
            force = self.force_function(delta1)
            force2 = force * -1
            p1.add_force(force)
            p2.add_force(force2)
            p1.compute_acceleration()
            p2.compute_acceleration()

    def move(self, dt):
        for point in self.points:
            point.move(dt)

    def get_points(self):
        return self.points

    def zero_force(self):
        for p in self.points:
            p.remove_forces()
