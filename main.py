from Point3d import *
from Vector3d import *
import random as r

for i in range(10):
    p = Point3d()
    x, y, z = r.random()*100, r.random()*100, r.random()*100
    vector = Vector3d(x, y, z)
    p.setPosition(vector)

    x, y, z = r.random()*10, r.random()*10, r.random()*10
    vector = Vector3d(x, y, z)
    p.setVelocity(vector)

    print p

point = Point3d()
pos = Vector3d(10, 10, 10)
vel = Vector3d(1, 2, 3)
point.setPosition(pos)
point.setVelocity(vel)

dt = 0.01
for i in range(15):
    pos = point.getPosition()
    vel = point.getVelocity()
    new_position = pos.derivate(vel, dt)
    point.setPosition(new_position)

    print point
    #vec3d
