from BoundingCircle import BoundingCircle
from Particle import Particle
from ParticleSystem import ParticleSystem
from SoundSystem import SoundSystem
from Vector2D import Vector2D
from rgb_colors_lookup import rgb_colors_array


def accelerate(particle: Particle):
    particle.vel *= 1.015


def increase_radius(particle: Particle, max_radius):
    if particle.radius < max_radius:
        particle.radius *= 1.015
    if particle.radius >= max_radius:
        raise ValueError("particle radius too large")
    if particle.radius < 1:
        raise ValueError("particle radius too small")


def change_color(particle: Particle):
    next_index = (particle.color_index + 1) % len(rgb_colors_array)
    particle.color = rgb_colors_array[next_index]
    particle.color_index = next_index


def run_simulation():

    collision_sound_path = ''  # TODO: add path to collision sound to use SoundSystem#play_collision_sound method
    sound_system = SoundSystem(collision_sound_path)

    scaling_factor = 0.75

    bounding_area = BoundingCircle(
        Vector2D(180*2*scaling_factor, 270*2*scaling_factor),
        160*2*scaling_factor
    )

    particle_system = ParticleSystem(
        720*scaling_factor,
        1020*scaling_factor,
        bounding_area,
        sub_steps=1)

    N = 1
    radius = 20*scaling_factor
    for i in range(N):
        particle_system.add_particle(
            bounding_area.center,
            Vector2D(100, 0)*10*10,
            Vector2D.up() * 2 * 900 * 10*10*10*10,
            radius,
            4,
            update_method=lambda particle: change_color(particle),
            on_hit_method=lambda particle: [accelerate(particle),
                                            increase_radius(particle, bounding_area.radius),
                                            sound_system.play_collision_sound_from_music()])

    particle_system.run(fps=120*1, dt=1/10000)


if __name__ == '__main__':
    run_simulation()
