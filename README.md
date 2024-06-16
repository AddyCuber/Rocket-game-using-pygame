# Rocket-game-using-pygame
This project is a simple space shooter game developed using Pygame. The player controls a rocket, moves left and right, and shoots bullets to destroy incoming demons. Features include score tracking, collision detection, and a game over screen with a restart option. It's an engaging way to practice basic game development concepts with Pygame.

Libraries used-
• pygame:
  •	Purpose: Used for creating video games.
  •	Functions:
    o	pygame.init(): Initializes Pygame modules.
    o	pygame.display.set_mode(): Sets up the game window.
    o	pygame.display.set_caption(): Sets the window title.
    o	pygame.display.set_icon(): Sets the window icon.
    o	pygame.image.load(): Loads images.
    o	pygame.font.Font(): Creates font objects.
    o	pygame.event.get(): Retrieves events like key presses and window close.
    o	screen.fill(): Fills the screen with a color.
    o	screen.blit(): Draws images on the screen.
    o	pygame.display.update(): Updates the display.
• random:
  •	Purpose: Provides random number generation.
  •	Function:
    o	random.randint(a, b): Generates a random integer between a and b. Used for random positioning of demons.
• math:
  •	Purpose: Provides mathematical functions.
  •	Functions:
    o	math.sqrt(x): Calculates the square root. Used for collision detection.
    o	math.pow(x, y): Raises x to the power of y. Used in distance calculations for collision detection.



• Initialization and Setup:
  •	Initializes Pygame and creates a display window (800x600).
  •	Sets the game title and icon.

• Player Configuration:
  •	Loads the player image.
  •	Sets the initial player position and movement variables.

• Demon Configuration:
  •	Initializes lists to store multiple demons' images, positions, and movement patterns.
  •	Randomly positions demons within specified ranges.

• Bullet Configuration:
  •	Loads the bullet image and sets its initial position and state (ready or fired).

• Score and Fonts:
  •	Initializes score variables and fonts for displaying the score and game over messages.

• Functions:
  •	game_over_text(): Displays the game over and play again messages.
  •	showScore(x, y): Displays the current and highest scores.
  •	player(x, y): Draws the player at the specified coordinates.
  •	demon(x, y, i): Draws the demon at the specified coordinates.
  •	fire_bullet(x, y): Changes bullet state to fire and draws it.
  •	isCollision(demonX, demonY, bulletX, bulletY): Checks for collisions between bullets and demons.
  •	reset_game(): Resets the game to its initial state.

• Game Loop:
  •	Handles events (keystrokes for movement and firing bullets).
  •	Updates player and bullet positions.
  •	Checks for collisions and updates the score.
  •	Displays the player, demons, and score.
  •	Handles game over conditions and displays the game over text.
