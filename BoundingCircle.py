import math

import Particle
import Renderer
from BoundingArea import BoundingArea
from Vector2D import Vector2D


class BoundingCircle(BoundingArea):
    def __init__(self, center: Vector2D, radius):
        self.center = center
        self.radius = radius
        self.elasticity = 1

    def __repr__(self):
        return f"BoundingCircle(center={self.center}, radius={self.radius})"

    def handle_particle_collision(self, particle: Particle, dt):
        """Translate the ball back inside the world and reflect its velocity."""

        # If the particle is inside the circle then there is no collision
        if particle.pos.distance_sqrd(self.center) < (self.radius - particle.radius) ** 2:
            return particle

        # Translate the ball back inside the world
        contact_point = self.__find_contact_point(particle, dt)
        particle.pos = Vector2D(contact_point.x, contact_point.y)

        # Reflect the ball's velocity
        new_ball_vel = self.__reflect_ball(particle)
        particle.vel = Vector2D(new_ball_vel.x, new_ball_vel.y)
        particle.collided = True

        return particle

    def __find_contact_point(self, particle: Particle, dt):
        """Find the point of contact between the ball and the world."""
        # See http://gamedev.stackexchange.com/a/29658
        A = self.center
        B = particle.prev_pos
        C = particle.pos
        R = self.radius
        r = particle.radius

        AB = B - A
        BC = C - B
        AB_len = AB.get_length()
        BC_len = BC.get_length()

        # If BC_len == 0, then B and C are equal, meaning D is also equal.
        # Continuing will produce divide-by-zero error
        if BC_len == 0:
            return C

        # If previous position is also outside the circle we project it back inside
        distance_from_circle = B.distance_sqrd(self.center) - ((self.radius - particle.radius) ** 2)
        if distance_from_circle > 0:
            B += AB.normalized() * - math.sqrt(distance_from_circle)
            AB = B - A
            BC = C - B
            AB_len = AB.get_length()
            BC_len = BC.get_length()

        b = AB.dot_product(BC) / math.pow(BC_len, 2) * -1
        c = (math.pow(AB_len, 2) - math.pow(R - r, 2)) / math.pow(BC_len, 2)
        d = b * b - c
        try:
            d_sqrt = math.sqrt(d)
        except ValueError:
            print("critical error exiting")
            print(d, particle, self)
            raise SystemExit

        k = b - d_sqrt

        if k < 0:
            k = b + d_sqrt

        BD = C - B
        BD_len = BC_len * k
        BD.set_length(BD_len)

        D = B + BD
        return D

    def __reflect_ball(self, particle: Particle):
        """Reflect the ball off the world and return its new velocity."""
        # See http://stackoverflow.com/questions/573084/bounce-angle
        world_pt = self.center
        ball_pt = particle.pos
        v = particle.vel
        n = (ball_pt - world_pt).normalized()

        # Assume perfect elasticity for now
        world_elasticity = self.elasticity
        restitution = particle.elasticity * world_elasticity

        # Solve reflection
        u = n * v.dot_product(n)
        w = v - u
        v_after = w - u
        reflection = (v_after - v) * restitution

        # Return new velocity
        new_ball_vel = v + reflection
        return new_ball_vel

    def draw(self, screen):
        Renderer.draw_unfilled_circle(screen, self.center, self.radius)

    def clear(self, screen):
        Renderer.draw_circle(screen, self.center, self.radius, (255, 255, 255))
