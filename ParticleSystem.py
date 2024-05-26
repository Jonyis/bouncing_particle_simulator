import random

import pygame

import BoundingArea
import Renderer
from Particle import Particle
from Vector2D import Vector2D


class ParticleSystem:
    def __init__(self, screen_width, screen_height, bounding_area: BoundingArea, sub_steps=1):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bounding_area = bounding_area
        self.sub_steps = sub_steps
        self.__paused = True

        # Initialize the pygame library
        pygame.init()

        # Set the screen size
        self.screen = pygame.display.set_mode((screen_width, screen_height))

        # Create a white background
        self.screen.fill((0, 0, 0))
        self.bounding_area.clear(self.screen)

        # Create a list to store the particles
        self.particles = []

    def add_particle(self, pos, vel, acc, radius=10, mass=1, on_hit_method=None, update_method=None):
        self.particles.append(
            Particle(pos, vel, acc, radius, mass, update_method=update_method, on_hit_method=on_hit_method))

    def update(self, dt):
        for i in range(self.sub_steps):
            # Update the position and velocity of each particle
            self.update_particles(dt/self.sub_steps)

        # Run custom update function (only ran once per time step)
        for particle in self.particles:
            particle.custom_update()

        # Clear the screen
        #Renderer.clear_screen(self.screen)

        # Draw the particles and the bounding box
        self.render_frame()

    def update_particles(self, dt):
        for particle in self.particles:
            particle.update(dt)
            self.bounding_area.handle_particle_collision(particle, dt)
            for p2 in self.particles:
                if particle == p2:
                    continue
                p2.check_collision(particle)

    def render_frame(self):
        # self.bounding_area.clear(self.screen)
        for particle in self.particles:
            Renderer.draw_particle(self.screen, particle)

    def run(self, fps=60, dt=0.01):

        clock = pygame.time.Clock()
        frame = 0
        # Start a game loop
        running = True
        while running:

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for i in range(20):
                            self.add_particle(
                                self.bounding_area.center +
                                Vector2D.random(self.bounding_area.radius) -
                                Vector2D(self.bounding_area.radius/2, self.bounding_area.radius/2),
                                Vector2D.zero(),
                                Vector2D.up()*5,
                                random.randint(10, 10),
                                100)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s and self.__paused:
                        # Update the particles (step)
                        self.update(dt)

                    if event.key == pygame.K_p:
                        self.__paused = not self.__paused
                        
            if not self.__paused:
                # Update the particles
                self.update(dt)


            # Display the screen
            pygame.display.flip()

            # Limit the FPS
            clock.tick(fps)
            # print(clock.get_fps())
