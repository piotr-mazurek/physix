import math
import numbers


class Vector3D():

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def setValues(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def setX(self, value):
        self.x = value

    def setY(self, value):
        self.y = value

    def setZ(self, value):
        self.z = value

    def __mul__(self, factor):
        """
        If factor is a vector returns product of scalar multiplication.
        If is a numeric variable returns a new vector.
        """

        if isinstance(factor, self.__class__):
            result = (
                self.x * factor.getX()
                + self.y * factor.getY()
                + self.z * factor.getZ()
            )
        elif isinstance(factor, numbers.Number):
            result = self.__class__(
                self.x * factor,
                self.y * factor,
                self.z * factor,
            )

        return result

    def __add__(self, vector):
        return self.scalarAddition(vector)

    def __div__(self, vector):
        return self.vectorDivision(vector)

    def vectorDivision(self, vector):
        try:
            self.x /= vector.getX()
        except:
            pass
        try:
            self.y /= vector.getY()
        except:
            pass
        try:
            self.z /= vector.getZ()
        except:
            pass
        return self

    def scalarDivision(self, scalar):
        if scalar != 0:
            self.x /= scalar
            self.y /= scalar
            self.z /= scalar
        return self

    def scalarMultiplication(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self

    def scalarAddition(self, vector):
        self.x += vector.getX()
        self.y += vector.getY()
        self.z += vector.getZ()
        return self

    def getDelta(self, vector):
        x = vector.getX() - self.x
        y = vector.getY() - self.y
        z = vector.getZ() - self.z
        return Vector3D(x, y, z)

    def derivate(self, vector, dt):
        self.x = self.x + dt * vector.getX()
        self.y = self.y + dt * vector.getY()
        self.z = self.z + dt * vector.getZ()
        return self

    def getMagnitude(self):
        return math.sqrt(
            self.x * self.x
            + self.y * self.y
            + self.z * self.z
        )

    def __repr__(self):
        return "[x:%.2f, y:%.2f, z:%.2f]" % (
            self.getX(),
            self.getY(),
            self.getZ(),
        )

    def __eq__(self, vector):
        """
        Overloads equality operator
        """
        if not isinstance(vector, self.__class__):
            return False

        if (
            self.x == vector.getX()
            and self.y == vector.getY()
            and self.z == vector.getZ()
        ):
            return True
        else:
            return False
