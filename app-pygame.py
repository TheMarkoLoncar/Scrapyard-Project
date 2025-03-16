import pygame
import random


pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Morse Code Translator")

font = pygame.font.SysFont('MS Sans Serif', 40, bold=True)
text = "SPIN"
padding = 10
surf = font.render(text, True, 'black')
button = pygame.Rect(75, 350, font.size(text)[0] + padding, font.size(text)[1] + padding)
letter1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letter2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letter3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
font2 = pygame.font.SysFont('MS Sans Serif', 100, bold=True)
text2 = f"{letter1} - {letter2} - {letter3}"
surf2 = font2.render(text2, True, 'black')
rectangle = pygame.Rect(75, 350, font.size(text2)[0] + padding, font.size(text2)[1] + padding)
screen.fill((255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
               screen.fill((255, 255, 255))
               letter1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
               letter2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
               letter3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
               font2 = pygame.font.SysFont('MS Sans Serif', 100, bold=True)
               text2 = f"{letter1} - {letter2} - {letter3}"
               surf2 = font2.render(text2, True, 'black')
               screen.blit(surf2, (100, 100)) 
               pygame.display.update()
    
    a,b = pygame.mouse.get_pos()
    if button.x <= a <= button.x + font.size(text)[0] + padding and button.y <= b <= button.y + font.size(text)[1] + padding:
        pygame.draw.rect(screen, (180, 180, 180), button)
    else:
        pygame.draw.rect(screen, (110, 110, 110), button)
    screen.blit(surf, (button.x + (padding / 2), button.y + (padding / 2)))
    
    pygame.display.update()