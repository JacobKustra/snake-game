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

# Game loop
while running:
    # Checks for events
    for event in pygame.event.get():
        # pygame.QUIT event means user closed the window
        if event.type == pygame.QUIT:
            # Ends game loop
            running = False

    # Makes screen blue and wipes away previous frame
    screen.fill("blue")

    # Draws player
    pygame.draw.circle(screen, "red", player_pos, 40)

    # Checks if keys are pressed and moves player
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt


    # flip() displays shows work
    pygame.display.flip()

    # Limits the FPS to 60 and adjusts delta time 
    dt = clock.tick(60) / 1000

pygame.quit()


