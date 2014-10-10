from Point3D import *
from itertools import combinations


class PhysicalObject():

    def __init__(self):
        self.points = []
        self.relations = []

    def force_function(self, first_point, second_point):
        u"""Computes force for given points.

        Must be defined for each physical object.
        Must take two points, and compute force between them.
        Returns force vector.
        """
        raise NotImplementedError

    def add_point(self, point):
        self.points.append(point)

    def compute_internal_forces(self):
        u"""Uses force_function to compute all internal forces"""
        for p1, p2 in combinations(self.points, 2):
            force = self.force_function(p1, p2)
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
