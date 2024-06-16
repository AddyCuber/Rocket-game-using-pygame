import pygame
import random
import math

# Initialize pygame
pygame.init()

# Create the display
screen = pygame.display.set_mode((800, 600))  # height and width

# Title and icon
pygame.display.set_caption("Space Rocket")
icon = pygame.image.load("r_g_logo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("game.png")
playerX = 370  # approx half because image has a size
playerY = 480
playerX_change = 0

# Demon
demonImg = []
demonX = []
demonY = []
demonX_change = []
demonY_change = []
num_demon = 6
for i in range(num_demon):
    demonImg.append(pygame.image.load("virus.png"))
    demonX.append(random.randint(0, 735))  # approx half because image has a size
    demonY.append(random.randint(50, 150))
    demonX_change.append(0.3)
    demonY_change.append(40)

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"  # ready-cant see the bullet, fire-bullet visible

score_value = 0
highest_score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over
gameoverfont = pygame.font.Font('freesansbold.ttf', 64)
playagainfont = pygame.font.Font('freesansbold.ttf', 32)


def game_over_text():
    gameover = gameoverfont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameover, (200, 250))  # blit means drawing
    playagain = playagainfont.render("Press P to Play Again", True, (255, 255, 255))
    screen.blit(playagain, (210, 350))


def showScore(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))  # blit means drawing
    highscore = font.render("Highest Score: " + str(highest_score), True, (255, 255, 255))
    screen.blit(highscore, (x, y + 40))


def player(x, y):
    screen.blit(playerImg, (x, y))  # blit means drawing


def demon(x, y, i):
    screen.blit(demonImg[i], (x, y))  # blit means drawing


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))  # centering


def isCollision(demonX, demonY, bulletX, bulletY):
    distance = math.sqrt((math.pow(demonX - bulletX, 2)) + (math.pow(demonY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Reset the game to its initial state
def reset_game():
    global playerX, playerY, playerX_change
    global bulletX, bulletY, bullet_state
    global demonX, demonY, demonX_change, demonY_change
    global score_value

    # Reset player position and movement
    playerX = 370
    playerY = 480
    playerX_change = 0

    # Reset bullet position and state
    bulletX = 0
    bulletY = 480
    bullet_state = "ready"

    # Reset demon positions and movement
    demonX = [random.randint(0, 735) for _ in range(num_demon)]
    demonY = [random.randint(50, 150) for _ in range(num_demon)]
    demonX_change = [0.3 for _ in range(num_demon)]
    demonY_change = [40 for _ in range(num_demon)]

    # Reset score
    score_value = 0


# Game loop
running = True
game_over = False
while running:
    # RGB
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # close button sets the value of running as false
            running = False
        # every keystroke is an event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_p and game_over:  # Press P to play again
                game_over = False
                reset_game()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player boundaries
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # image is 64x64
        playerX = 736

    if not game_over:
        for i in range(num_demon):
            # Game Over
            if demonY[i] > 440:
                for j in range(num_demon):
                    demonY[j] = 2000
                game_over = True
                if score_value > highest_score:
                    highest_score = score_value
                game_over_text()
                break

            demonX[i] += demonX_change[i]
            if demonX[i] <= 0:
                demonX_change[i] = 0.3
                demonY[i] += demonY_change[i]
            elif demonX[i] >= 736:  # image is 64x64
                demonX_change[i] = -0.3
                demonY[i] += demonY_change[i]

            # Collision
            collision = isCollision(demonX[i], demonY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "ready"
                score_value += 1

                demonX[i] = random.randint(0, 735)  # approx half because image has a size
                demonY[i] = random.randint(50, 150)
            demon(demonX[i], demonY[i], i)  # player is called after to screen

        # Bullet movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)  # player is called after to screen
    else:
        game_over_text()

    showScore(textX, textY)
    # Update display
    pygame.display.update()
