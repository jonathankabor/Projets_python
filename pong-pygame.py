import sys
sys.path.append(r"C:\Users\Hp\PycharmProjects\pythonProject\RobotFramework\venv\Lib\site-packages")
import pygame 


# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout / Brick Breaker Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Paddle
paddle_width = 100
paddle_height = 15
paddle_speed = 7
paddle = pygame.Rect(WIDTH//2 - paddle_width//2, HEIGHT - 50, paddle_width, paddle_height)

# Ball
ball_radius = 10
ball_speed = [5, -5]
ball = pygame.Rect(WIDTH//2 - ball_radius, HEIGHT//2 - ball_radius, ball_radius*2, ball_radius*2)

# Bricks
brick_rows = 5
brick_cols = 10
brick_width = WIDTH // brick_cols
brick_height = 30
bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(col*brick_width, row*brick_height, brick_width-2, brick_height-2)
        bricks.append(brick)

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Ball movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collisions with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] *= -1
    if ball.top <= 0:
        ball_speed[1] *= -1
    if ball.bottom >= HEIGHT:
        running = False  # Game over

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_speed[1] *= -1

    # Ball collision with bricks
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_speed[1] *= -1
        score += 10

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # Draw paddle
    pygame.draw.rect(screen, BLUE, paddle)

    # Draw ball
    pygame.draw.ellipse(screen, YELLOW, ball)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, HEIGHT - 40))

    pygame.display.flip()

pygame.quit()