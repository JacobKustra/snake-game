# Main file to launch snake game

import pygame
import random

# Initialize pygame
pygame.init()
pygame.display.init()
pygame.font.init()

# Set screen size
screen_width = 900
screen_height = 900
square = min(screen_width, screen_height)
screen = pygame.display.set_mode((square, square))

# Grid set up
# Cell size and snake/fruit size should be based off of set number of columns 
# and rows and dynamic to window size 
grid_num = 32
cell_size = (square/grid_num)

# Set up game clock
clock = pygame.time.Clock()

# Game loop is active
running = True

# Frames per second
fps = 120

# adds movement delay to keep game looking fluid without having
# player move too fast
move_delay = 100
last_move_time = pygame.time.get_ticks()

# snake positioning and movement direction
snake_pos = [[16, 16], [17, 16], [18, 16]]
snake_len = 3
snake_direction = None
next_snake_direction = snake_direction
def move_snake(direction):
    if direction == "UP":
        temp_pos = snake_pos[0].copy()
        temp_pos[1] -= 1
        snake_pos.insert(0, temp_pos)
        if snake_len >= len(snake_pos):
            pass
        else:
            snake_pos.pop()
    elif direction == "DOWN":
        temp_pos = snake_pos[0].copy()
        temp_pos[1] += 1
        snake_pos.insert(0, temp_pos)
        if snake_len >= len(snake_pos):
            pass
        else:
            snake_pos.pop()
    elif direction == "LEFT":
        temp_pos = snake_pos[0].copy()
        temp_pos[0] -= 1
        snake_pos.insert(0, temp_pos)
        if snake_len >= len(snake_pos):
            pass
        else:
            snake_pos.pop()
    elif direction == "RIGHT":
        temp_pos = snake_pos[0].copy()
        temp_pos[0] += 1
        snake_pos.insert(0, temp_pos)
        if snake_len >= len(snake_pos):
            pass
        else:
            snake_pos.pop()
        
# Add Barriers
def walls():
    global running
    global grid_num
    if snake_pos[0][0] == -1:
        running = False
    if snake_pos[0][1] == -1:
        running = False
    if snake_pos[0][0] == grid_num:
        running = False
    if snake_pos[0][1] == grid_num:
        running = False

# Self Collision Check
def self_collision():
    global running
    counter = 0
    for i, snake_part in enumerate(snake_pos):
        if i == 0:
            pass
        else:
            if snake_part == snake_pos[0]:
                running = False
    
# Random fruit spawns
fruit_location = [None, None]
def spawn_fruit():
    # TODO - Improve to select random spot after excluding snake positions
    # to improve efficiency.
    fruit_location.clear()
    random_x = random.randint(0, (grid_num - 1))
    random_y = random.randint(0, (grid_num - 1))
    fruit_location.append(random_x)
    fruit_location.append(random_y)
    if fruit_location in snake_pos:
        spawn_fruit()

# Function to check if snake eats the fruit
def eat_fruit():
    global snake_len
    if fruit_location[0] == None or fruit_location[1] == None:
        spawn_fruit()
    if (snake_pos[0][0] == fruit_location[0]) and (snake_pos[0][1] == 
                                                   fruit_location[1]):
        snake_len += 1
        spawn_fruit()

# Font
font = pygame.font.Font(None, 45)

# Game loop
while running:
    # Checks for events
    for event in pygame.event.get():
        # pygame.QUIT event means user closed the window
        if event.type == pygame.QUIT:
            # Ends game loop
            running = False

        # pygame.KEYDOWN checks if key was pressed
        if event.type == pygame.KEYDOWN:
            new_direction = None
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                new_snake_direction = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                new_snake_direction = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                new_snake_direction = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                new_snake_direction = "RIGHT"
            next_snake_direction = new_snake_direction

    # Gets current time
    current_time = pygame.time.get_ticks()
    
    # Makes screen white and wipes away previous frame
    screen.fill("white")
        
    # Checks if fruit was eaten
    eat_fruit()

    # Draws the fruit
    fruit_x = fruit_location[0] * cell_size
    fruit_y = fruit_location[1] * cell_size
    pygame.draw.rect(screen, "green", (fruit_x, fruit_y,
                                       cell_size, cell_size))
    
    # Draws the snake in grid format
    for x, snake_part in enumerate(snake_pos):
        snake_x = snake_part[0] * cell_size
        snake_y = snake_part[1] * cell_size
        if x == 0:
            pygame.draw.rect(screen, "black", (snake_x, snake_y, 
                                             cell_size, cell_size))
        else:
            pygame.draw.rect(screen, "red", (snake_x, snake_y, 
                                             cell_size, cell_size))

    # Moves the snake
    if current_time - last_move_time > move_delay:
        snake_direction = next_snake_direction
        move_snake(snake_direction)
        last_move_time = current_time
    
    # Detects collision
    walls()
    self_collision()
   
    # Displays score
    score = f"Score: {snake_len}"
    text = font.render(score, True, (0, 0, 0))
    screen.blit(text, (cell_size, cell_size))

    # flip() displays shows work
    pygame.display.flip()

    # Games FPS
    clock.tick(60)

pygame.quit()


