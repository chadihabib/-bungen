import pygame

pygame.init()

score = 2

screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 36)
text = font.render(f"Score: {score}", True, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))
    screen.blit(text, (550,0))
    pygame.display.flip()
