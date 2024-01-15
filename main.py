import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf',50)

sky_surface = pygame.image.load('Sky.png').convert_alpha ()
ground_surface = pygame.image.load('ground.png').convert.convert_alpha()
text_surface = test_font.render('My game', False, 'Green')

snail_surface = pygame.image.load('snail1.png').convert_alpha()
snail_x_pos = 600


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # draw all our elements
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    snail_x_pos -= 3
    if snail_x_pos < -100: snail_x_pos = 800 
    screen.blit(snail_surface, (snail_x_pos,262))



    # update everything
    pygame.display.update()
    clock.tick(50)



