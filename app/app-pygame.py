# import pygame
# import random
# import time

# pygame.init()

# screen = pygame.display.set_mode((500, 500))
# pygame.display.set_caption("Morse Code Translator")

# font = pygame.font.SysFont('MS Sans Serif', 40, bold=True)
# text = "SPIN"
# padding = 10
# surf = font.render(text, True, 'black')
# button1 = pygame.Rect(150, 250, font.size(text)[0] + padding, font.size(text)[1] + padding)
# button2 = pygame.Rect(225, 250, font.size(text)[0] + padding, font.size(text)[1] + padding)
# button3 = pygame.Rect(300, 250, font.size(text)[0] + padding, font.size(text)[1] + padding)
# letter = "-"
# font2 = pygame.font.SysFont('MS Sans Serif', 100, bold=True)
# text2 = f"{letter}"
# surf2 = font2.render(text2, True, 'black')
# font3 = pygame.font.SysFont('MS Sans Serif', 40, bold=True)
# text3 = "NEXT"
# surf3 = font3.render(text3, True, 'black')
# word = ""
# saved_letter = ""
# font_letter_saved = pygame.font.SysFont('MS Sans Serif', 100, bold=False)
# text_letter_saved = "saved!"
# surf_letter_saved = font_letter_saved.render(text_letter_saved, True, 'black')
# font_error = pygame.font.SysFont('MS Sans Serif', 70, bold=False)
# text_error = "unable to save..."
# surf_error = font_error.render(text_error, True, 'black')
# font_word = pygame.font.SysFont('MS Sans Serif', 70, bold=True)
# text_word = word
# surf_word = font_word.render(text_word, True, 'black')
# button_next = pygame.Rect(250, 250, font3.size(text3)[0] + padding, font3.size(text3)[1] + padding)
# screen.fill((255, 255, 255))
# screen.blit(surf2, (230, 100))
# screen.blit(surf_word, (200, 400))

# def draw_button(button, padding, screen, surf):
#     pygame.draw.rect(screen, (110, 110, 110), button)
#     screen.blit(surf, (button.x + (padding / 2), button.y + (padding / 2)))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if button1.collidepoint(event.pos):
#                screen.fill((255, 255, 255))
#                screen.blit(surf_word, (30, 30))
#                letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ_")
#                font2 = pygame.font.SysFont('MS Sans Serif', 100, bold=True)
#                text2 = f"{letter}"
#                surf2 = font2.render(text2, True, 'black')
#                pygame.display.update()
#                screen.blit(surf2, (220, 100)) 
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if button_next.collidepoint(event.pos):
#                 screen.fill((255, 255, 255))
#                 screen.blit(surf_word, (30, 30))
#                 if letter == "-":
#                     screen.blit(surf_error, (70, 300))
#                 else:
#                     saved_letter = letter
#                     word += saved_letter
#                     screen.blit(surf_letter_saved, (140, 300))
#                     screen.blit(surf_word, (30, 30))
#                 letter = "-"
#                 font2 = pygame.font.SysFont('MS Sans Serif', 100, bold=True)
#                 text2 = f"{letter}"
#                 surf2 = font2.render(text2, True, 'black')
#                 screen.blit(surf2, (230, 100)) 
#                 font_word = pygame.font.SysFont('MS Sans Serif', 70, bold=True)
#                 text_word = word
#                 surf_word = font_word.render(text_word, True, 'black')
#                 screen.blit(surf_word, (30, 30))
#                 pygame.display.update()

    
#     a,b = pygame.mouse.get_pos()
#     draw_button(button1, padding, screen, surf)
#     draw_button(button_next, padding, screen, surf3)

    
#     pygame.display.update()
import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Morse Code Translator")

font = pygame.font.SysFont("MS Sans Serif", 40, bold=True)
text = "SPIN"
padding = 10
surf = font.render(text, True, "black")
button1 = pygame.Rect(
    150, 250, font.size(text)[0] + padding, font.size(text)[1] + padding
)
button2 = pygame.Rect(
    225, 250, font.size(text)[0] + padding, font.size(text)[1] + padding
)
button3 = pygame.Rect(
    300, 250, font.size(text)[0] + padding, font.size(text)[1] + padding
)
letter = "-"
font2 = pygame.font.SysFont("MS Sans Serif", 100, bold=True)
text2 = f"{letter}"
surf2 = font2.render(text2, True, "black")
font3 = pygame.font.SysFont("MS Sans Serif", 40, bold=True)
text3 = "NEXT"
surf3 = font3.render(text3, True, "black")
word = ""
saved_letter = ""
font_letter_saved = pygame.font.SysFont("MS Sans Serif", 100, bold=False)
text_letter_saved = "saved!"
surf_letter_saved = font_letter_saved.render(text_letter_saved, True, "black")
font_error = pygame.font.SysFont("MS Sans Serif", 70, bold=False)
text_error = "unable to save..."
surf_error = font_error.render(text_error, True, "black")
font_word = pygame.font.SysFont("MS Sans Serif", 70, bold=True)
text_word = word
surf_word = font_word.render(text_word, True, "black")
button_next = pygame.Rect(
    250, 250, font3.size(text3)[0] + padding, font3.size(text3)[1] + padding
)
screen.fill((255, 255, 255))
screen.blit(surf2, (230, 100))
screen.blit(surf_word, (200, 400))


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
                screen.blit(surf_word, (30, 30))
                letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ_")
                font2 = pygame.font.SysFont("MS Sans Serif", 100, bold=True)
                text2 = f"{letter}"
                surf2 = font2.render(text2, True, "black")
                pygame.display.update()
                screen.blit(surf2, (220, 100))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_next.collidepoint(event.pos):
                screen.fill((255, 255, 255))
                screen.blit(surf_word, (30, 30))
                if letter == "-":
                    screen.blit(surf_error, (70, 300))
                else:
                    saved_letter = letter
                    word += saved_letter
                    screen.blit(surf_letter_saved, (140, 300))
                    screen.blit(surf_word, (30, 30))
                letter = "-"
                font2 = pygame.font.SysFont("MS Sans Serif", 100, bold=True)
                text2 = f"{letter}"
                surf2 = font2.render(text2, True, "black")
                screen.blit(surf2, (230, 100))
                font_word = pygame.font.SysFont("MS Sans Serif", 70, bold=True)
                text_word = word
                surf_word = font_word.render(text_word, True, "black")
                screen.blit(surf_word, (30, 30))
                pygame.display.update()

    a, b = pygame.mouse.get_pos()
    draw_button(button1, padding, screen, surf)
    draw_button(button_next, padding, screen, surf3)

    pygame.display.update()
