class Vector3D():
    x, y, z = (0.0, 0.0, 0.0)

    def __init__(self, x, y, z):
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

    def __mul__(self, vector):
        x = self.x * vector.getX()
        y = self.y * vector.getY()
        z = self.z * vector.getZ()
        return Vector3D(x, y, z)

    def derivate(self, vector, dt):
        self.x = self.x + dt * vector.getX()
        self.y = self.y + dt * vector.getY()
        self.z = self.z + dt * vector.getZ()
        return self

    def __repr__(self):
        return "[x:%.2f, y:%.2f, z:%.2f]" % (
            self.getX(),
            self.getY(),
            self.getZ(),
        )
