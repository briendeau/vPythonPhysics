from vpython import *

floor1 = box(pos=vector(0, -5, 0), color=color.orange, length=10, height=.1, width=10)
ceiling = box(pos=vector(0, 5, 0), color=color.orange, length=10, height=.1, width=10)
wall = box(pos=vector(0, 0, 5), color=color.orange, length=10, height=10, width=.10)
wall = box(pos=vector(0, 0, -5), color=color.orange, length=10, height=10, width=.10)
wall = box(pos=vector(-5, 0, 0), color=color.orange, length=.10, height=10, width=10)

marble = sphere(pos=vector(0, 0, 0), color=color.blue, length=3, radius=3)

while True:
    pass
