import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Paddle dimensions
paddle_width = 100
paddle_height = 15

# Ball dimensions
ball_radius = 10

# Paddle position and speed
paddle_x = screen_width // 2 - paddle_width // 2
paddle_speed = 10

# Ball position and speed
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = 0
ball_speed_y = 5

# Score and lives
score = 0
lives = 3

# Fonts
font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 35)

# Function to display score and lives
def show_score_lives():
    score_display = font.render(f"Score: {score}", True, white)
    lives_display = font.render(f"Lives: {lives}", True, white)
    screen.blit(score_display, (20, 20))
    screen.blit(lives_display, (screen_width - lives_display.get_width() - 20, 20))

# Function to display game over message
def show_game_over():
    game_over_display = font.render("GAME OVER", True, red)
    screen.blit(game_over_display, (screen_width // 2 - game_over_display.get_width() // 2, screen_height // 2 - game_over_display.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # Ball movement
    ball_y += ball_speed_y

    # Ball collision with paddle
    if ball_y >= screen_height - paddle_height - ball_radius and paddle_x < ball_x < paddle_x + paddle_width:
        ball_y = 0
        ball_x = random.randint(ball_radius, screen_width - ball_radius)
        score += 1
        ball_speed_y += 0.5

    # Ball out of bounds
    elif ball_y > screen_height:
        ball_y = 0
        ball_x = random.randint(ball_radius, screen_width - ball_radius)
        lives -= 1
        if lives == 0:
            show_game_over()
            running = False
    
    # Drawing
    screen.fill(black)
    pygame.draw.rect(screen, blue, (paddle_x, screen_height - paddle_height, paddle_width, paddle_height))
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    show_score_lives()

    # Update display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()

