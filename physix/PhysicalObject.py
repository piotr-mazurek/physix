from Point3D import *
from itertools import combinations


class PhysicalObject():

    def __init__(self):
        self.points = []
        self.relations = []

    def force_function(self, distance_vector):
        u"""Computes force for given distance vector

        Must be defined for each physical object.
        """
        raise NotImplementedError

    def add_point(self, point):
        self.points.append(point)

    def compute_internal_forces(self):
        u"""Uses force_function to compute all internal forces"""
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
