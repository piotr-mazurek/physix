import math
import numbers


class Vector3D():

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def set_values(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def set_x(self, value):
        self.x = value

    def set_y(self, value):
        self.y = value

    def set_z(self, value):
        self.z = value

    def __mul__(self, factor):
        """
        If factor is a vector returns product of scalar multiplication.
        If is a numeric variable returns a new vector.
        """

        if isinstance(factor, self.__class__):
            result = (
                self.x * factor.get_x()
                + self.y * factor.get_y()
                + self.z * factor.get_z()
            )
        elif isinstance(factor, numbers.Number):
            result = self.__class__(
                self.x * factor,
                self.y * factor,
                self.z * factor,
            )

        return result

    def __add__(self, vector):
        return self.scalar_addition(vector)

    def __div__(self, vector):
        return self.vector_division(vector)

    def vector_division(self, vector):
        try:
            self.x /= vector.get_x()
        except:
            pass
        try:
            self.y /= vector.get_y()
        except:
            pass
        try:
            self.z /= vector.get_z()
        except:
            pass
        return self

    def scalar_division(self, scalar):
        if scalar != 0:
            self.x /= scalar
            self.y /= scalar
            self.z /= scalar
        return self

    def scalar_multiplication(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self

    def scalar_addition(self, vector):
        self.x += vector.get_x()
        self.y += vector.get_y()
        self.z += vector.get_z()
        return self

    def get_delta(self, vector):
        x = vector.get_x() - self.x
        y = vector.get_y() - self.y
        z = vector.get_z() - self.z
        return Vector3D(x, y, z)

    def derivate(self, vector, dt):
        self.x = self.x + dt * vector.get_x()
        self.y = self.y + dt * vector.get_y()
        self.z = self.z + dt * vector.get_z()
        return self

    def get_magnitude(self):
        return math.sqrt(
            self.x * self.x
            + self.y * self.y
            + self.z * self.z
        )

    def __repr__(self):
        return "[x:%.2f, y:%.2f, z:%.2f]" % (
            self.get_x(),
            self.get_y(),
            self.get_z(),
        )

    def __eq__(self, vector):
        """
        Overloads equality operator
        """
        if not isinstance(vector, self.__class__):
            return False

        if (
            self.x == vector.get_x()
            and self.y == vector.get_y()
            and self.z == vector.get_z()
        ):
            return True
        else:
            return False
