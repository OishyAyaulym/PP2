import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
bg_image = pygame.image.load('img/clock.png')
sec_img = pygame.image.load('img/sec_hand.png')
min_img = pygame.image.load('img/min_hand.png')
rect = bg_image.get_rect(center=(400, 309)) 

pivot_offset_sec = (sec_img.get_width() // 2, sec_img.get_height() // 2)
pivot_offset_min = (min_img.get_width() // 2, min_img.get_height() // 2)

while not done:
    screen.blit(bg_image, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time = datetime.now().time()

    sec_angle = -(time.second * 6)
    min_angle = -(time.minute * 6)

    nsec_img = pygame.transform.rotate(sec_img, sec_angle)
    sec_rect = nsec_img.get_rect(center=(rect.centerx, rect.centery))
    screen.blit(nsec_img, sec_rect.topleft)

    nmin_img = pygame.transform.rotate(min_img, min_angle)
    min_rect = nmin_img.get_rect(center=(rect.centerx, rect.centery))
    screen.blit(nmin_img, min_rect.topleft)

    pygame.display.flip()