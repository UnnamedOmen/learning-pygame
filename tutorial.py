import pygame
import random
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# Surfaces
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

score = 0
score_surface = test_font.render(f"Score: {score}", False, (64,64,64))
score_rect = score_surface.get_rect(center = (400, 50))

player_gravity = 0
player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

# Initialize enemy positions

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (800, 300))




# Game-Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    
    # Display terrain and score surfaces
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    
    screen.blit(score_surface, score_rect)

    # Display enemy and player surfaces
    screen.blit(snail_surface, snail_rect)
   
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.y >= 301: player_rect.y = 250
    screen.blit(player_surface, player_rect)

    # Decrement snail position for movement, then reset snail position
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
        score += 1
        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("space")


    
    # Frame-rate and screen update
    pygame.display.update()
    clock.tick(60)
