# Main file to launch snake game

import pygame

# Initialize pygame
pygame.init()
pygame.display.init()

# Set screen size
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
square = min(screen_width, screen_height)
screen = pygame.display.set_mode((square, square))

# Frames per second
fps = 60

# Grid set up
# Cell size and snake/fruit size should be based off of set number of columns 
# and rows and dynamic to window size 
grid_num = 32
cell_size = (square/grid_num)

# Set up game clock
clock = pygame.time.Clock()

# Game loop is active
running = True

# x position = grid_position * cell_size
# For example, if the player is at grid position (3, 2) and cell_size = 60
# position_x=3×60 = 180 & position_y=2x60 = 120

snake_pos = pygame.Vector2((square / 2), (square / 2))

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
                snake_pos.y -= cell_size
            if event.key == pygame.K_DOWN:
                snake_pos.y += cell_size
            if event.key == pygame.K_LEFT:
                snake_pos.x -= cell_size
            if event.key == pygame.K_RIGHT:
                snake_pos.x += cell_size


    # Makes screen white and wipes away previous frame
    screen.fill("white")
    

    # Draws the snake
    pygame.draw.rect(screen, "red", (snake_pos.x, snake_pos.y, 
                                     cell_size, cell_size))


    # flip() displays shows work
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()


