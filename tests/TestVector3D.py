from ..physix.Vector3D import Vector3D
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

    def test_scalar_multiplication(self):
        """
        Tests scalar multiplication between two vectors
        """
        vector1 = Vector3D(2, 2, 2)
        vector2 = Vector3D(3, 3, 3)

        product = vector1 * vector2

        self.assertEquals(product, 18)

    def test_vector_by_scalar_multiplication(self):
        """
        Tests vector by scalar multiplication
        """
        vector = Vector3D(2, 2, 2)
        expected_output = Vector3D(4, 4, 4)
        self.assertEquals(vector * 2, expected_output)

    def test_vector_derivative(self):
        vector1 = Vector3D(10, 10, 30)
        vector2 = Vector3D(2, 2, 2)
        dt = 0.1

        vector1 = vector1.derivate(vector2, dt)
        self.assertEqual(vector1, Vector3D(10.2, 10.2, 30.2))

    def test_addition(self):
        vector1 = Vector3D(1, 2, 3)
        vector2 = Vector3D(3, 2, 1)

        self.assertEqual(vector1 + vector2, Vector3D(4, 4, 4))

    def test_division(self):
        vector1 = Vector3D(4, 6, 8)

        self.assertEquals(
            vector1.scalarDivision(2),
            Vector3D(2, 3, 4)
        )
