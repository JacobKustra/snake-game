# Main file to launch snake game

import pygame

# Initialize pygame
pygame.init()
pygame.display.init()

# Set screen size
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height))

# Grid set up
# Cell size and snake/fruit size should be based off of set number of columns 
# and rows and dynamic to window size 

# Set up game clock
clock = pygame.time.Clock()

# Game loop is active
running = True

# Game loop
while running:
    # Checks for events
    for event in pygame.event.get():
        # pygame.QUIT event means user closed the window
        if event.type == pygame.QUIT:
            # Ends game loop
            running = False

    # Makes screen white and wipes away previous frame
    screen.fill("white")

    # flip() displays shows work
    pygame.display.flip()

    clock.tick(60)

pygame.quit()


