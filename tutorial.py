import pygame
import random
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    current_time_seconds = current_time / 1000
    score_surface = test_font.render(f"{current_time_seconds:.2f}", False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0

# Surfaces
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()


# score_surface = test_font.render(f"Score: {score}", False, (64,64,64))
# score_rect = score_surface.get_rect(center = (400, 50))

player_gravity = 0
player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

# Intro screen
player_stand = pygame.image.load('graphics\Player\player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_title = test_font.render("Pixel  Runner", False, (64,64,64))
game_title_rect = game_title.get_rect(center = (400, 80))
instructions = test_font.render("Press  Space   to  Start", False, (64,64,64))
instructions_rect = instructions.get_rect(center = (400, 320))


# Initialize enemy positions
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (800, 300))




# Game-Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = pygame.time.get_ticks()

    if game_active:
        # Display terrain and score surfaces
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # screen.blit(score_surface, score_rect)
        display_score()



        # Display enemy and player surfaces
        screen.blit(snail_surface, snail_rect)
    
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # Decrement snail position for movement, then reset snail position
        snail_rect.x -= 6
        if snail_rect.right <= 0:
            snail_rect.left = 800
            

        if player_rect.colliderect(snail_rect):
            game_active = False

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title, game_title_rect)
        screen.blit(instructions, instructions_rect)
    # Frame-rate and screen update
    pygame.display.update()
    clock.tick(60)







# To-Do: Scoring system
# Change score_surface to time
# Points variable = number of times you've jumped the snail
# Add a new score text. 
# Make score = how many times you've jumped over the snail
# Increment points by 1 each time the snail is jumped
# After 10 seconds increment points by 1.1 each time the snail is jumped etc 