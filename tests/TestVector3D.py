from .. Vector3D import Vector3D
import unittest


class TestVector3D(unittest.TestCase):

    def test_vector(self):
        vector = Vector3D(0, 0, 0)
        self.assertEqual(vector.getX(), 0.0)
        self.assertEqual(vector.getY(), 0.0)
        self.assertEqual(vector.getZ(), 0.0)

        vector = Vector3D(1, 2, 3)
        self.assertEqual(vector.getX(), 1.0)
        self.assertEqual(vector.getY(), 2.0)
        self.assertEqual(vector.getZ(), 3.0)

    def test_vector_multiplication(self):
        vector1 = Vector3D(2, 2, 2)
        vector2 = Vector3D(3, 3, 3)

        self.assertEquals(str(vector1 * vector2), str(Vector3D(6, 6, 6)))

    def test_vector_derivative(self):
        vector1 = Vector3D(10, 10, 30)
        vector2 = Vector3D(2, 2, 2)
        dt = 0.1

        vector1 = vector1.derivate(vector2, dt)
        self.assertEqual(str(vector1), str(Vector3D(10.2, 10.2, 30.2)))

    def test_addition(self):
        vector1 = Vector3D(1, 2, 3)
        vector2 = Vector3D(3, 2, 1)

        self.assertEqual(str(vector1 + vector2), str(Vector3D(4, 4, 4)))

    def test_division(self):
        vector1 = Vector3D(4, 6, 8)
        vector2 = Vector3D(2, 2, 2)

        self.assertEquals(
            str(vector1.scalarDivision(vector2)),
            str(Vector3D(2, 3, 4))
        )
