# Main file to launch snake game

import pygame

# Initialize pygame
pygame.init()

# Set screen size
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up game clock
clock = pygame.time.Clock()

# Game loop is active
running = True

dt = 0

# Width of Snake
snake_size = 20

# Player position with starting location
player_pos = pygame.Vector2((screen_width / 2), (screen_height / 2))

# Function that ends game if snake collides with wall
def hit_wall():
    print(player_pos.x, player_pos.y)
    global running
    if player_pos.x <= 0:
        running = False
    elif player_pos.x >= (screen_width - (snake_size - 2)):
        running = False
    elif player_pos.y <= 0:
        running = False
    elif player_pos.y >= (screen_height - (snake_size - 2)):
        running = False

# Ensures only these keys result in valid game interaction
eligible_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]

# Function that decides way movement will occur when key is pressed
def keys(key):
    if key == pygame.K_UP:
        if player_pos.y >= 0:
            player_pos.y -= 300 * dt
    if key == pygame.K_DOWN:
        if player_pos.y <= (screen.get_height() - (snake_size - 2)):
            player_pos.y += 300 * dt
    if key == pygame.K_LEFT:
        if player_pos.x >= 0:
            player_pos.x -= 300 * dt
    if key == pygame.K_RIGHT:
        if player_pos.x <= (screen.get_width() - (snake_size - 2)):
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
    # pygame.draw.circle(screen, "red", player_pos, 10)
    pygame.draw.rect(screen, "red", 
                     (player_pos.x, player_pos.y, snake_size, snake_size))

    # Checks if keys are pressed and moves snake
    if key_pressed:
        keys(key_pressed[0])
    
    # flip() displays shows work
    pygame.display.flip()


    hit_wall()

    # Limits the FPS to 60 and adjusts delta time 
    dt = clock.tick(60) / 1000

pygame.quit()


