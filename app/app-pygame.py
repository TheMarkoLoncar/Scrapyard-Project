import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Morse Code Translator")

font = pygame.font.SysFont('MS Sans Serif', 40, bold=True)
text = "SPIN"
padding = 10
surf = font.render(text, True, 'black')
button1 = pygame.Rect(75, 250, font.size(text)[0] + padding, font.size(text)[1] + padding)
button2 = pygame.Rect(150, 250, font.size(text)[0] + padding, font.size(text)[1] + padding)
button3 = pygame.Rect(225, 250, font.size(text)[0] + padding, font.size(text)[1] + padding)
letter1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letter2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letter3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
font2 = pygame.font.SysFont('MS Sans Serif', 100, bold=True)
text2 = f"{letter1} - {letter2} - {letter3}"
surf2 = font2.render(text2, True, 'black')
screen.fill((255, 255, 255))

def draw_button(button, padding, screen, surf):
    pygame.draw.rect(screen, (110, 110, 110), button)
    screen.blit(surf, (button.x + (padding / 2), button.y + (padding / 2)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
               screen.fill((255, 255, 255))
               letter1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
               font2 = pygame.font.SysFont('MS Sans Serif', 100, bold=True)
               text2 = f"{letter1} - {letter2} - {letter3}"
               surf2 = font2.render(text2, True, 'black')
               screen.blit(surf2, (100, 100)) 
               pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button2.collidepoint(event.pos):
                screen.fill((255, 255, 255))
                letter2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                font2 = pygame.font.SysFont('MS Sans Serif', 100, bold=True)
                text2 = f"{letter1} - {letter2} - {letter3}"
                surf2 = font2.render(text2, True, 'black')
                screen.blit(surf2, (100, 100)) 
                pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button3.collidepoint(event.pos):
                screen.fill((255, 255, 255))
                letter3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                font2 = pygame.font.SysFont('MS Sans Serif', 100, bold=True)
                text2 = f"{letter1} - {letter2} - {letter3}"
                surf2 = font2.render(text2, True, 'black')
                screen.blit(surf2, (100, 100)) 
                pygame.display.update()
    
    a,b = pygame.mouse.get_pos()
    draw_button(button1, padding, screen, surf)
    draw_button(button2, padding, screen, surf)
    draw_button(button3, padding, screen, surf)

    
    pygame.display.update()
