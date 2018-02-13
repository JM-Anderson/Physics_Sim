from p_libs.physics.utils import calc_coll_time, calc_exit_vels

from enum import Enum


# Where
# 0 = particle
# 1 = wall
class coll_type:
    # Particle to particle
    p2p = (0, 0)

    # Particle to wall
    p2w = (0, 1)


class collision:
    def __init__(self, particle_set, time_left, coll_type=coll_type.p2p):
        self.time_left = time_left
        self.p_set = particle_set


class collision_stack:
    collisions = {}

    def __init__(self, particle_sets, dt):
        for p_set in particle_sets:
            if len(p_set) <= 1:
                continue

            self.collisions[self.create_key(p_set)] = collision(p_set, dt)

    def resolve(self, collision):
        p1 = collision.p_set[0]
        p2 = collision.p_set[1]

        r_sum = p1.r + p2.r

        # Check if bounding boxes of particles are colliding
        if abs(p1.x - p2.x) < r_sum > abs(p1.y - p2.y):

            # Calculate how long until the particles collide
            coll_time = calc_coll_time(p1, p2)
            if coll_time is not None:
                # If time till collision is greater than timestep
                # the collision will not occur this frame
                if coll_time > collision.time_left or coll_time < 0:
                    return

                p1.in_collision = True
                p2.in_collision = True

                # Move both particles so they are colliding perfectly
                p1.p_move(coll_time)
                p2.p_move(coll_time)

                new_vels = calc_exit_vels(p1, p2)
                p1.set_vel(new_vels[0][0], new_vels[0][1])
                p2.set_vel(new_vels[1][0], new_vels[1][1])

                collision.time_left -= coll_time

                p1.p_move(collision.time_left)
                p2.p_move(collision.time_left)

    def resolve_all(self):
        for key, collision in self.collisions.items():
            self.resolve(collision)

    def create_key(self, particle_set):
        key = []
        for p in particle_set:
            key.append(p.id)

        return tuple(key)
