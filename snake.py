# Main file to launch snake game

import pygame

# Initialize pygame
pygame.init()

# Set screen size
screen = pygame.display.set_mode((1280, 720))

# Set up game clock
clock = pygame.time.Clock()

# Game loop is active
running = True

# Delta Time (dt) is used to track time since last frame
dt = 0

# Player position with starting location
player_pos = pygame.Vector2((screen.get_width() / 2), 
                            (screen.get_height() / 2))

eligible_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]

# Function that decides way movement will occur when key is pressed
def keys(key):
    if key == pygame.K_UP:
        player_pos.y -= 300 * dt
    if key == pygame.K_DOWN:
        player_pos.y += 300 * dt
    if key == pygame.K_LEFT:
        player_pos.x -= 300 * dt
    if key == pygame.K_RIGHT:
        player_pos.x += 300 * dt

# Stores keys pressed
key_pressed = []

# Game loop
while running:
    # Checks for events
    for event in pygame.event.get():
        # pygame.QUIT event means user closed the window
        if event.type == pygame.QUIT:
            # Ends game loop
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in eligible_keys:
                key_pressed.clear()
                key_pressed.append(event.key)
        

    # Makes screen blue and wipes away previous frame
    screen.fill("green")

    # Draws snake
    pygame.draw.circle(screen, "red", player_pos, 10)

    # Checks if keys are pressed and moves snake
    if key_pressed:
        keys(key_pressed[0])

    # flip() displays shows work
    pygame.display.flip()

    # Limits the FPS to 60 and adjusts delta time 
    dt = clock.tick(60) / 1000

pygame.quit()


