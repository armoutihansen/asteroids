# Asteroids

A small game of Asteroids written in Python using the Pygame library. This project is a work in progress and serves as a simple implementation of the classic arcade game. Players control a spaceship, navigate through space, and shoot asteroids to survive.

## Features

- **Player Movement**: The player can rotate and move the spaceship in any direction.
- **Shooting Mechanic**: The player can shoot projectiles to destroy asteroids.
- **Asteroid Splitting**: When an asteroid is hit, it splits into smaller pieces until it reaches the minimum size.
- **Random Asteroid Spawning**: Asteroids spawn at random edges of the screen with random velocities and sizes.
- **Collision Detection**: The game detects collisions between the player, asteroids, and projectiles.
- **Game Over Condition**: The game ends when the player collides with an asteroid.

## Project Structure

The project is organized into several Python modules:

- **`main.py`**: The entry point of the game. It initializes the game, handles the main game loop, and manages updates and rendering.
- **`constants.py`**: Contains game constants such as screen dimensions, player speed, asteroid properties, and more.
- **`player.py`**: Implements the `Player` class, which handles player movement, rotation, shooting, and rendering.
- **`asteroid.py`**: Implements the `Asteroid` class, which handles asteroid behavior, including movement, rendering, and splitting.
- **`asteroidfield.py`**: Implements the `AsteroidField` class, which manages the spawning of asteroids at random edges of the screen.
- **`shot.py`**: Implements the `Shot` class, which represents projectiles fired by the player.
- **`circleshape.py`**: A base class for circular game objects, providing common functionality such as collision detection.
- **`requirements.txt`**: Specifies the required Python dependencies for the project.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.

## How to Run

1. Install Python (version 3.12 or higher is recommended).
2. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:

   ```bash
   python main.py
   ```

## Controls

- `W`: Move forward.
- `S`: Move backward.
- `A`: Rotate left.
- `Space`: Shoot projectiles.

## Dependencies

This project uses the following dependency:

`Pygame` (version 2.6.1)

## Future Improvements

- Add a scoring system to track the player's progress.
- Implement multiple levels with increasing difficulty.
- Add sound effects and background music.
- Improve graphics with better visuals and animations.
- Add a main menu and pause functionality.
