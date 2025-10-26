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

score_surface = test_font.render("My game", False, "Black")
score_rect = score_surface.get_rect(center = (400, 50))

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
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print("Collision")
    
    # Display terrain and score surfaces
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    
    pygame.draw.rect(screen, "Pink", score_rect)
    pygame.draw.rect(screen, "Pink", score_rect)
    pygame.draw.line(screen, "Pink", (0,0), (800,400), 10)
    screen.blit(score_surface, score_rect)

    # Display enemy and player surfaces
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    # Decrement snail position for movement, then reset snail position
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800

    # if player_rect.colliderect(snail_rect):
    #     print("collision")
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())
    
    
    # Frame-rate and screen update
    pygame.display.update()
    clock.tick(60)
