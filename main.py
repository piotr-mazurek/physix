from physix.Point3D import Point3D
from physix.Vector3D import Vector3D
from physix.PhysicalObject import PhysicalObject
import random as r

# for i in range(10):
#     p = Point3D()
#     x, y, z = r.random()*100, r.random()*100, r.random()*100
#     vector = Vector3D(x, y, z)
#     p.setPosition(vector)

#     x, y, z = r.random()*10, r.random()*10, r.random()*10
#     vector = Vector3D(x, y, z)
#     p.setVelocity(vector)

#     print p

# point = Point3D()
# pos = Vector3D(10, 10, 10)
# vel = Vector3D(1, 2, 3)
# point.setPosition(pos)
# point.setVelocity(vel)

# dt = 0.01
# for i in range(15):
#     pos = point.getPosition()
#     vel = point.getVelocity()
#     new_position = pos.derivate(vel, dt)
#     point.setPosition(new_position)

#     print point
#     #vec3D
p1 = Point3D()
p2 = Point3D()

p2.setPosition(Vector3D(2, 2, 2))

obj = PhysicalObject()
obj.addPoint(p1)
obj.addPoint(p2)
obj.force_function(Vector3D(2, 2, 2))
# for i in range(10):
# obj.computeInternalForces()

vec = Vector3D(1, 1, 1)
vec2 = Vector3D(1, 2, 3)
print vec.getMagnitude()
print vec.getDelta(vec2)
