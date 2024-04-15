import pygame

def scorecounting(score,ENEMY_SPEED):
    score =+ ENEMY_SPEED
    return score

def drawscore(score,BLACK,screen):
    display_field = pygame.font.Font(None,35)
    text = display_field.render(f"Score:{score}", True,BLACK)
    screen.blit(text,(450,5))
