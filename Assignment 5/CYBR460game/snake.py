import pygame
import random

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake settings
snake = [[200, 200]]
direction = "RIGHT"
speed = 10

# Food
food = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

def draw():
    screen.fill(BLACK)
    # Draw snake
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, 10, 10))
    # Draw food
    pygame.draw.rect(screen, RED, (*food, 10, 10))
    # Score
    score = font.render(f"Score: {len(snake)-1}", True, (255,255,255))
    screen.blit(score, (10, 10))
    pygame.display.update()

running = True
while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"
    # Move snake
    head = snake[0].copy()
    if direction == "UP":
        head[1] -= 10
    elif direction == "DOWN":
        head[1] += 10
    elif direction == "LEFT":
        head[0] -= 10
    elif direction == "RIGHT":
        head[0] += 10

    snake.insert(0, head)
    if (
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT or
        head in snake[1:]
    ):
        running = False
    # Eat food
    if head == food:
        food = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
    else:
        snake.pop()
    draw()

pygame.quit()