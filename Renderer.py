import pygame

import Particle
from Vector2D import Vector2D


def clear_screen(screen):
    screen.fill((255, 255, 255))


def draw_particle(screen, particle: Particle):
    # pygame.draw.circle(screen, (0, 0, 0), (int(particle.pos.x), int(particle.pos.y)), int(particle.radius*1.05))
    pygame.draw.circle(screen, particle.color, (int(particle.pos.x), int(particle.pos.y)), int(particle.radius))
    draw_unfilled_circle(screen, particle.pos, particle.radius, width=1, color=(0, 0, 0))


def draw_unfilled_circle(screen, center: Vector2D, radius: int, width: int = 2, color: (int, int, int) = (0, 0, 255)):
    pygame.draw.circle(
        screen,
        color,
        (int(center.x),
         int(center.y)),
        int(radius),
        width)


def draw_circle(screen, center: Vector2D, radius: int, color: (int, int, int) = (0, 0, 255)):
    pygame.draw.circle(
        screen,
        color,
        (int(center.x),
         int(center.y)),
        int(radius))


def draw_rectangle(screen, top_left: Vector2D, bottom_right: Vector2D, color: (int, int, int) = (0, 255, 0)):

    pygame.draw.rect(
        screen,
        color,
        pygame.Rect(
            top_left.x,
            top_left.y,
            bottom_right.x - top_left.x,
            bottom_right.y - top_left.y))


def draw_unfilled_rectangle(screen, top_left: Vector2D, bottom_right: Vector2D, color: (int, int, int) = (0, 255, 0)):

    pygame.draw.rect(
        screen,
        color,
        pygame.Rect(
            top_left.x,
            top_left.y,
            bottom_right.x - top_left.x,
            bottom_right.y - top_left.y),
        2)
