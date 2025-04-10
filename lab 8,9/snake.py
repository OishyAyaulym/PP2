import pygame
from random import randrange
import time

# Game settings
res = 800  # Window size
size = 50   # Grid size

# Load images
apple_img = pygame.image.load('apple.png')
apple_img = pygame.transform.scale(apple_img, (size, size))  # Resize to fit grid
banana_img = pygame.image.load('banana.png')
banana_img = pygame.transform.scale(banana_img, (size, size))  # Resize to fit grid
snake_img = pygame.image.load('snake.png')
snake_img = pygame.transform.scale(snake_img, (size, size))  # Resize to fit grid

# Function to generate food at a valid position
def generate_food(snake):
    while True:
        food = randrange(0, res, size), randrange(0, res, size)
        if food not in snake:  # Ensure food does not spawn on the snake
            return food

# Initialize snake
x, y = randrange(0, res, size), randrange(0, res, size)
snake = [(x, y)]
length = 1
apple = generate_food(snake)
banana = generate_food(snake)
apple_timer = pygame.time.get_ticks()
banana_timer = pygame.time.get_ticks()
food_lifetime = 5000  # Food disappears after 5 seconds

dirs = {'W': True, 'S': True, 'A': True, 'D': True}
dx, dy = 0, 0
fps = 5  # Initial speed
score = 0
level = 1

# Initialize Pygame
pygame.init()
sc = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_level = pygame.font.SysFont('Arial', 26, bold=True)

# Game loop
while True:
    sc.fill(pygame.Color('black'))
    
    # Draw the snake
    for i, j in snake:
        sc.blit(snake_img, (i, j))  # Draw snake using image
    
    # Check if food expired
    current_time = pygame.time.get_ticks()
    if current_time - apple_timer > food_lifetime:
        apple = generate_food(snake)
        apple_timer = current_time
    if current_time - banana_timer > food_lifetime:
        banana = generate_food(snake)
        banana_timer = current_time
    
    # Draw the apple and banana images
    sc.blit(apple_img, apple)
    sc.blit(banana_img, banana)
    
    # Display score and level
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    render_level = font_level.render(f'LEVEL: {level}', 1, pygame.Color('cyan'))
    sc.blit(render_score, (5, 5))
    sc.blit(render_level, (5, 35))
    
    # Move the snake
    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-length:]
    
    # Check for collisions (Wall or Self)
    if x < 0 or x >= res or y < 0 or y >= res or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (res // 2 - 200, res // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    
    # Check if apple is eaten
    if snake[-1] == apple:
        apple = generate_food(snake)  # Generate new food
        apple_timer = pygame.time.get_ticks()
        length += 1
        score += 1
    
    # Check if banana is eaten (gives more points)
    if snake[-1] == banana:
        banana = generate_food(snake)  # Generate new food
        banana_timer = pygame.time.get_ticks()
        length += 2  # Banana increases length more
        score += 2   # Banana gives more points
    
    # Level up every 5 points instead of 3 for faster progression with bananas
    if score % 5 == 0 and score > 0:
        level += 1
        fps += 2  # Increase speed
    
    pygame.display.flip()
    clock.tick(fps)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    # Control snake movement
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}