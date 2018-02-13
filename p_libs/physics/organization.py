"""
Organizes particles such that the collision detection algorithm isn't
forced to check unnecessarily
"""
import math

from abc import ABC, abstractmethod


class organization(ABC):
    organized = {}

    def __init__(self, particle_list):
        self.particles = particle_list

    @abstractmethod
    def organize(self):
        pass


class uniform_grid(organization):
    grid_scale = 18

    def organize(self):
        self.organized = {}
        for particle in self.particles:
            # Calculate grid position
            grid_x = particle.x / self.grid_scale
            grid_y = particle.y / self.grid_scale

            # Floored grid position (bottom left node)
            fgrid_x = math.floor(grid_x)
            fgrid_y = math.floor(grid_y)

            # Grid squares that the particle is contained in
            squares = [(fgrid_x, fgrid_y)]

            # This assumes particle width == grid_scale
            if grid_x > fgrid_x:
                squares.append((fgrid_x + 1, fgrid_y))
            if grid_y > fgrid_y:
                squares.append((fgrid_x, fgrid_y + 1))
            if len(squares) == 3:
                squares.append((fgrid_x + 1, fgrid_y + 1))

            for square in squares:
                if square in self.organized:
                    self.organized[square].append(particle)
                else:
                    self.organized[square] = [particle]
