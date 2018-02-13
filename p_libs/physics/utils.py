import math


# This method is not meant for readability
# It is meant purely for performance
# No single calculation is performed twice
def calc_exit_vels(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y

    d_sqr = dx ** 2 + dy ** 2

    # Check if particles are overlapping
    are_colliding = (p1.r + p2.r) ** 2 > d_sqr
    if not are_colliding:
            return None

    dvelx = p1.velocity_x - p2.velocity_x
    dvely = p1.velocity_y - p2.velocity_y

    dsum = dx * dvelx + dy * dvely

    denom = d_sqr * (p1.mass + p2.mass)

    c_ans = 2 * dsum / denom

    c_ans1 = c_ans * p1.mass
    vx1 = p1.velocity_x - c_ans1 * dx
    vy1 = p1.velocity_y - c_ans1 * dy

    c_ans2 = c_ans * p2.mass
    vx2 = p2.velocity_x + c_ans2 * dx
    vy2 = p2.velocity_y + c_ans2 * dy

    return [(vx1, vy1), (vx2, vy2)]


# Calculates the time until a collision will occur between two particles
# Can possibly be negative
# Stolen shamelessly from https://gamedev.stackexchange.com/questions/62360/small-high-speed-object-collisions-avoiding-tunneling
def calc_coll_time(p1, p2):
    a = p1.x
    b = p1.y

    c = p2.x
    d = p2.y

    w = p1.velocity_x
    x = p2.velocity_x

    y = p1.velocity_y
    z = p2.velocity_y

    r = p1.r
    s = p2.r

    discrim = (2*a*w-2*a*x+2*b*y-2*b*z-2*c*w+2*c*x-2*d*y+2*d*z)**2-4*(w**2-2*w*x+x**2+y**2-2*y*z+z**2)*(a**2-2*a*c+b**2-2*b*d+c**2+d**2-r**2-2*r*s-s*2)
    # If discrim is negative or 0 -> no collision
    if discrim <= 0:
        return None

    t = (-1/2 * math.sqrt(discrim)-a*w+a*x-b*y+b*z+c*w-c*x+d*y-d*z)/(w**2-2*w*x+x**2+y**2-2*y*z+z**2)

    return t
