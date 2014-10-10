from physix import *
import random as r
from objects import SimpleObject

o = SimpleObject()
p1 = Point3D()
p1.set_position(Vector3D(0, 0, 0))
p2 = Point3D()
p2.set_position(Vector3D(2, 2.5, 2))
o.add_point(p1)
o.add_point(p2)

print o.points

for i in range(100000):
    o.compute_internal_forces()
    o.move(0.01)
    o.zero_force()

print o.points
