import math
import random

from Vector2D import Vector2D


class Particle:
    def __init__(self,
                 pos: Vector2D,
                 vel: Vector2D,
                 acc: Vector2D,
                 radius=10,
                 mass=1,
                 update_method=None,
                 on_hit_method=None):
        self.pos = pos
        self.prev_pos = pos
        self.vel = vel
        self.acc = acc
        self.radius = radius
        self.mass = mass
        self.color = (0, 0, 255)
        self.color_index = random.randint(0, 100)
        self.elasticity = 1
        self.update_function = update_method
        self.on_hit_method = on_hit_method
        self.__visited = False
        self.collided = False

    def update(self, dt):
        self.prev_pos = self.pos
        self.pos += self.vel * dt + (0.5 * self.acc * (dt ** 2))
        self.vel += self.acc * dt

        if self.collided and self.on_hit_method:
            self.on_hit_method(self)

        self.__visited = False
        self.collided = False

    def custom_update(self):
        if self.update_function:
            self.update_function(self)

    def __repr__(self):
        return f"Particle(pos={self.pos}, vel={self.vel}, acc={self.acc})"

    def set_velocity(self, x, y):
        self.vel = Vector2D(x, y)

    def check_collision(self, other: "Particle"):

        # If other particle's collision has already been handled then skip it
        # if other.__visited:
        #     return

        distance_sqrd = self.pos.distance_sqrd(other.pos)
        if distance_sqrd > (self.radius + other.radius) ** 2:
            return

        delta_pos = self.pos - other.pos
        distance = math.sqrt(distance_sqrd)
        offset = distance - (self.radius + other.radius)

        self.pos += ((delta_pos * -1) / distance) * offset / 2
        other.pos += (delta_pos / distance) * offset / 2

        total_mass = self.mass + other.mass
        delta_vel_1 = self.__compute_delta_vel(self, other, total_mass)
        delta_vel_2 = self.__compute_delta_vel(other, self, total_mass)

        self.vel += delta_vel_1
        other.vel += delta_vel_2

        self.__visited = True
        other.__visited = True
        self.collided = True
        # self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # other.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    @staticmethod
    def __compute_delta_vel(p1: "Particle", p2: "Particle", total_mass: float):
        return -2 * p2.mass / total_mass * \
               Vector2D.dot_product(p1.vel - p2.vel, p1.pos - p2.pos) / \
               Vector2D.inner_sum((p1.pos - p2.pos) ** 2) * (p1.pos - p2.pos)
