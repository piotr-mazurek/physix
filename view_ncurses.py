#!/usr/bin/env python
import curses
from physix import Point3D, Vector3D, PhysicalObject, SquareObject
import time


def login(stdscr):
# Clear screen
    stdscr.clear()
    stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')

    maxyx = stdscr.getmaxyx()
    mid_x = maxyx[1] / 2.0
    mid_y = maxyx[0] / 2.0

    p = Point3D.Point3D()
    p2 = Point3D.Point3D()
    p3 = Point3D.Point3D()
    p2.setPosition(Vector3D.Vector3D(2.0002, 2.0002, 2))
    p3.setPosition(Vector3D.Vector3D(-1.0002, 1.0002, 1))

    po = PhysicalObject.PhysicalObject()

    po.addPoint(p)
    po.addPoint(p2)
    po.addPoint(p3)

    dt = 0.01
    while True:
        time.sleep(0.01)
        stdscr.clear()
        po.zero_force()
        po.computeInternalForces()
        po.move(dt)
        points = po.get_points()
        for i, p in enumerate(points):
            position = p.getPosition()
            stdscr.addstr(i, 0, str(position))
            x = int(position.getX() + mid_x)
            y = int(position.getY() + mid_y)
            stdscr.addch(y, x, 'o')

        stdscr.refresh()

    stdscr.getch()

curses.wrapper(login)
