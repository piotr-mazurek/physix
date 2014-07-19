from .. Point3D import Point3D
from .. Vector3D import Vector3D
import unittest


class TestPoint3D(unittest.TestCase):

    def test_point(self):
        point = Point3D()

        self.assertEquals(str(point.getPosition()), str(Vector3D(0, 0, 0)))
        self.assertEquals(str(point.getVelocity()), str(Vector3D(0, 0, 0)))

    def test_movement(self):
        point = Point3D()
        point.setVelocity(Vector3D(1, 1, 3))
        point.move(0.1)

        self.assertEquals(
            str(point.getPosition()),
            str(Vector3D(0.1, 0.1, 0.3)),
        )
