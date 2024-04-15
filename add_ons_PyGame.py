import pygame

def scorecounting(score,ENEMY_SPEED):
    score += ENEMY_SPEED
    return score

def drawscore(score,BLACK,screen):
    display_field = pygame.font.Font(None,25)
    text = display_field.render(f"Score:{score}", True,BLACK)
    screen.blit(text,(450,5))

def highscore(score,highscorelist,screen,BLACK):
    highscorelist.append(score)
    highscorelist.sort(reverse=True)

    display_field = pygame.font.Font(None,35)
    scorelist = display_field.render(f"Highscorelist:\n 1. {highscorelist[0]} \n 2. {highscorelist[1]} \n 3. {highscorelist[2]} \n 4. {highscorelist[3]} \n 5. {highscorelist[4]}", True,BLACK)
    screen.blit(scorelist,(5,5))

