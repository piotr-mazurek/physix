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

    def set_position(self, vector):
        self.position = vector

    def get_position(self):
        return self.position

    def set_velocity(self, velocity):
        self.velocity = velocity

    def get_velocity(self):
        return self.velocity

    def set_acceleration(self, acceleration):
        self.acceleration = acceleration

    def get_acceleration(self):
        return self.acceleration

    def add_force(self, vector):
        self.forces.append(vector)

    def compute_acceleration(self):
        force_sum = Vector3D(0, 0, 0)
        if len(self.forces):
            for force in self.forces:
                force_sum += force

        self.acceleration = force_sum / self.mass
        return self

    def remove_forces(self):
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
            self.position.get_x(),
            self.position.get_y(),
            self.position.get_z(),

            self.velocity.get_x(),
            self.velocity.get_y(),
            self.velocity.get_z(),
        )
