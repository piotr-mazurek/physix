from physix import PhysicalObject, Vector3D


class SimpleObject(PhysicalObject):
    desired_distance = 2

    def force_function(self, first_point, second_point):
        u"""Simple force implementation with a fixed function minimum.

        f(x) = (x-desired_distance)**2
        """
        p1 = first_point.get_position()
        p2 = second_point.get_position()

        delta = p1.get_delta(p2)

        def internal(delta):
            if delta < self.desired_distance:
                return ((delta - self.desired_distance)** 2) * -1 
            else:
                return (delta - self.desired_distance) ** 2

        x = internal(delta.get_x())
        y = internal(delta.get_y())
        z = internal(delta.get_z())

        return Vector3D(x, y, z)
