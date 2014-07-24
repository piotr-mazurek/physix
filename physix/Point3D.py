from Vector3D import Vector3D
# [[p,p2,p3], quadratic]
#   quadratic(p, p2)


class Point3D():

    def __init__(self):
        self.position = Vector3D(0, 0, 0)
        self.velocity = Vector3D(0, 0, 0)
        self.acceleration = Vector3D(0, 0, 0)
        self.forces = []
        self.mass = 1.0

    def setPosition(self, vector):
        self.position = vector

    def getPosition(self):
        return self.position

    def setVelocity(self, velocity):
        self.velocity = velocity

    def getVelocity(self):
        return self.velocity

    def setAcceleration(self, acceleration):
        self.acceleration = acceleration

    def getAcceleration(self):
        return self.acceleration

    def addForce(self, vector):
        self.forces.append(vector)

    def computeAcceleration(self):
        force_sum = Vector3D(0, 0, 0)
        if len(self.forces):
            for force in self.forces:
                force_sum += force

        self.acceleration = force_sum / self.mass
        return self

    def removeForces(self):
        self.forces = []
        self.acceleration = Vector3D(0, 0, 0)
        return self

    def move(self, dt):
        u"""
        Moves point forward in time by given delta time.
        :param dt delta time
        """
        self.velocity.derivate(self.acceleration, dt)
        self.position.derivate(self.velocity, dt)

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
