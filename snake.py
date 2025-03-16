# Main file to launch snake game

import pygame
import random

# Initialize pygame
pygame.init()
pygame.display.init()

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
snake_pos = [[16, 16], [17, 16], [17, 15]]
snake_len = 3
snake_direction = None
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
    if snake_pos[0][0] == 0:
        running = False
    if snake_pos[0][1] == 0:
        running = False
    if snake_pos[0][0] == grid_num:
        running = False
    if snake_pos[0][1] == grid_num:
        running = False
    
# Random fruit spawns
fruit_location = [None, None]

def spawn_fruit():
    fruit_location.clear()
    random_x = random.randint(0, (grid_num - 1))
    random_y = random.randint(0, (grid_num - 1))
    fruit_location.append(random_x)
    fruit_location.append(random_y)

# Function to check if snake eats the fruit
def eat_fruit():
    global snake_len
    print(snake_pos[0], fruit_location)
    if fruit_location[0] == None or fruit_location[1] == None:
        spawn_fruit()
    if (snake_pos[0][0] == fruit_location[0]) and (snake_pos[0][1] == 
                                                   fruit_location[1]):
        snake_len += 1
        spawn_fruit()


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
            if event.key == pygame.K_UP:
                snake_direction = "UP"
            if event.key == pygame.K_DOWN:
                snake_direction = "DOWN"
            if event.key == pygame.K_LEFT:
                snake_direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                snake_direction = "RIGHT"

    # Detects wall collision
    walls()

    # Gets current time
    current_time = pygame.time.get_ticks()
    
    # Makes screen white and wipes away previous frame
    screen.fill("white")
    
    eat_fruit()

    # Draws the fruit
    fruit_x = fruit_location[0] * cell_size
    fruit_y = fruit_location[1] * cell_size
    pygame.draw.rect(screen, "green", (fruit_x, fruit_y,
                                       cell_size, cell_size))
    
    # Draws the snake in grid format
    for snake_part in snake_pos:
        snake_x = snake_part[0] * cell_size
        snake_y = snake_part[1] * cell_size
        pygame.draw.rect(screen, "red", (snake_x, snake_y, 
                                         cell_size, cell_size))

    # Moves the snake
    if current_time - last_move_time > move_delay:
        move_snake(snake_direction)
        last_move_time = current_time


    # flip() displays shows work
    pygame.display.flip()

    # Games FPS
    clock.tick(60)

pygame.quit()


