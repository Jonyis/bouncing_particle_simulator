# Bouncing Particle Simulator

## Motivation

Bouncing Particle Simulator is a Python-based simulation that models the behavior of particles bouncing within a bounded area. 
This project was created in order to recreate several Youtube videos that were showing up at the time ([example 1](https://www.youtube.com/watch?v=rgjeRfHFjms) [example2](https://www.youtube.com/watch?v=1Aplfwg_nyI)).

## Demo

### Basic Simulation
Simulating particles in a bounded area with no collision detection.

https://github.com/user-attachments/assets/992fa886-6ef9-42d0-8347-d059ab938389

### Collision Detection
It is also possible to simulate particles with collision detection. 
However, the simulation becomes slow very fast. This was the motivation to recreate part of this project in C++, which can be found [here](https://github.com/Jonyis/particle_simulation).

https://github.com/user-attachments/assets/0521d00a-e92e-4c48-a616-6a13fbc8669c

### Custom Collision Functions
You can also specify functions to be applied to a particle upon collision, such as changing its color, increasing its radius, or playing a sound effect. 
This allows us to recreate some of the effects seen in the Youtube videos.

https://github.com/user-attachments/assets/f5647545-9fa7-404b-a50c-958b041fee25

https://github.com/user-attachments/assets/2cb5a9a6-649d-41f0-b0d7-e253dcc1c0ec
