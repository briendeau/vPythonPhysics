from vpython import *

G = 6.7e-11

giant_sun = sphere(pos=vector(-1e11,0,0), radius=2e10, color=color.blue,
                   make_trail=True, trail_type='points', interval=10, retain=50)

giant_sun.mass = 2e30  ##mass of sun
giant_sun.p = vector(0, 0, -1e4) * giant_sun.mass  ##momentum (m * v)

dwarf = sphere(pos=vector(1.5e11,0,0), radius=1e10, color=color.green,
               make_trail=True, interval=10, retain=50)

dwarf.mass = 1e30  #half mass of sun
dwarf.p = -giant_sun.p
dt= 1e5

while True:
    rate(200) #no more than 200 interations per second
    r = dwarf.pos - giant_sun.pos
    F = G * giant_sun.mass * dwarf.mass * r.hat / mag2(r)
    giant_sun.p = giant_sun.p + F*dt
    dwarf.p = dwarf.p - F*dt
    giant_sun.pos = giant_sun.pos + (giant_sun.p/giant_sun.mass) * dt
    dwarf.pos = dwarf.pos + (dwarf.p/dwarf.mass) * dt
    
    
    