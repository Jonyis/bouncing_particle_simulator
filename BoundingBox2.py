import Renderer
from BoundingArea import BoundingArea
from Particle import Particle
from Vector2D import Vector2D


class BoundingBox2(BoundingArea):
    def __init__(self, top_left: Vector2D, bottom_right: Vector2D):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def handle_particle_collision(self, particle: Particle, dt):
        if particle.pos.x - particle.radius < self.top_left.x:
            particle.vel.x -= particle.acc.x * dt
            particle.pos.x = self.top_left.x + int(particle.radius)
            particle.vel.x *= -1 * particle.elasticity
            particle.collided = True
        elif particle.pos.x + particle.radius > self.bottom_right.x:
            particle.vel.x -= particle.acc.x * dt
            particle.pos.x = self.bottom_right.x - int(particle.radius)
            particle.vel.x *= -1 * particle.elasticity
            particle.collided = True
        if particle.pos.y - particle.radius < self.top_left.y:
            particle.vel.y -= particle.acc.y * dt
            particle.pos.y = self.top_left.y + int(particle.radius)
            particle.vel.y *= -1 * particle.elasticity
            particle.collided = True
        elif particle.pos.y + particle.radius > self.bottom_right.y:
            particle.vel.y -= particle.acc.y * dt
            particle.pos.y = self.bottom_right.y - int(particle.radius)
            particle.vel.y *= -1 * particle.elasticity
            particle.collided = True

        return particle

    def draw(self, screen):
        Renderer.draw_unfilled_rectangle(screen, self.top_left, self.bottom_right)

    def clear(self, screen):
        Renderer.draw_rectangle(screen, self.top_left, self.bottom_right, (255, 255, 255))
