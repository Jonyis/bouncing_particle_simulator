import math

import Particle
import Renderer
from BoundingArea import BoundingArea
from Vector2D import Vector2D


class BoundingBox(BoundingArea):
    def __init__(self, top_left: Vector2D, bottom_right: Vector2D):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.__should_accelerate_on_impact = False
        self.__impact_acceleration_percentage = 1.01

    def __repr__(self):
        return f"BoundingBox(top_left={self.top_left}, bottom_right={self.bottom_right})"

    def handle_particle_collision(self, particle: Particle):
        if particle.pos.x + particle.radius > self.bottom_right.x:
            particle.pos = self.__get_new_pos_x_bound(particle, self.bottom_right.x - particle.radius)
            particle.vel.x *= -1 * particle.elasticity
            particle.collided = True
            if self.__should_accelerate_on_impact:
                particle.vel = self.__apply_acceleration_on_collision(particle)

        elif particle.pos.x - particle.radius < self.top_left.x:
            particle.pos = self.__get_new_pos_x_bound(particle, self.top_left.x + particle.radius)
            particle.vel.x *= -1 * particle.elasticity
            particle.collided = True
            if self.__should_accelerate_on_impact:
                particle.vel = self.__apply_acceleration_on_collision(particle)

        if particle.pos.y - particle.radius < self.top_left.y:
            particle.pos = self.__get_new_pos_y_bound(particle, self.top_left.y + particle.radius)
            particle.vel.y *= -1 * particle.elasticity
            particle.collided = True
            if self.__should_accelerate_on_impact:
                particle.vel = self.__apply_acceleration_on_collision(particle)

        elif particle.pos.y + particle.radius > self.bottom_right.y:
            particle.pos = self.__get_new_pos_y_bound(particle, self.bottom_right.y - particle.radius)
            particle.vel.y *= -1 * particle.elasticity
            particle.collided = True
            if self.__should_accelerate_on_impact:
                particle.vel = self.__apply_acceleration_on_collision(particle)

        return particle

    @staticmethod
    def __get_new_pos_x_bound(particle: Particle, x_bound):
        cur_pos = particle.pos
        prev_pos = cur_pos - particle.vel

        m = ((cur_pos.y - prev_pos.y) / (cur_pos.x - prev_pos.x))
        b = prev_pos.y - m * prev_pos.x

        angle = math.atan2(cur_pos.y - prev_pos.y, cur_pos.x - prev_pos.x)
        angle = math.pi - angle

        impact_point = Vector2D(x_bound, m*x_bound + b)
        distance = particle.vel.get_length() - (impact_point - prev_pos).get_length()

        return Vector2D(impact_point.x + distance*math.cos(angle), impact_point.y + distance*math.sin(angle))

    @staticmethod
    def __get_new_pos_y_bound(particle: Particle, y_bound):
        cur_pos = particle.pos
        prev_pos = cur_pos - particle.vel

        # If moving directly horizontally must be handled separately
        if cur_pos.x == prev_pos.x:
            angle = math.pi/2 * math.copysign(1, -particle.vel.y)
            impact_point = Vector2D(cur_pos.x, y_bound)
        else:
            m = ((cur_pos.y - prev_pos.y) / (cur_pos.x - prev_pos.x))
            b = prev_pos.y - m * prev_pos.x

            angle = math.atan2(cur_pos.y - prev_pos.y, cur_pos.x - prev_pos.x)
            angle = angle

            impact_point = Vector2D((y_bound - b) / m, y_bound)

        distance = particle.vel.get_length() + (impact_point - prev_pos).get_length()

        return Vector2D(impact_point.x + distance*math.cos(angle), impact_point.y + distance*math.sin(angle))

    def __apply_acceleration_on_collision(self, particle: Particle):
        return Vector2D(particle.vel.x * self.__impact_acceleration_percentage,
                        particle.vel.y * self.__impact_acceleration_percentage)

    def draw(self, screen):
        Renderer.draw_unfilled_rectangle(screen, self.top_left, self.bottom_right)

    def clear(self, screen):
        Renderer.draw_rectangle(screen, self.top_left, self.bottom_right, (255, 255, 255))
