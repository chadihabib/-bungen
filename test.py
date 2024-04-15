import pygame
import pygame_widgets as pw
import time
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Button erstellen
button = pw.Button(screen, 100, 100, 200, 50, text='Klick mich!')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Button aktualisieren und zeichnen
    button.listen(event)
    button.draw()

    pygame.display.flip()
