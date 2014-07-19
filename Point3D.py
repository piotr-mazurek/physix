import Vector3D


class Point3D():
    position = Vector3D
    velocity = Vector3D
    mass = 1.0

    def setPosition(self, vector):
        self.position = vector

    def getPosition(self):
        return self.position

    def setVelocity(self, velocity):
        self.velocity = velocity

    def getVelocity(self):
        return self.velocity

    def __repr__(self):
        return "POSITION [x:%.2f, y:%.2f, z:%.2f], \
            V[x:%.2f, y:%.2f, z:%.2f]" % (
            self.position.getX(),
            self.position.getY(),
            self.position.getZ(),

            self.velocity.getX(),
            self.velocity.getY(),
            self.velocity.getZ(),
        )