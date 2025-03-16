import pygame
import random
import string

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Morse Code Translator")

font = pygame.font.SysFont("MS Sans Serif", 40, bold=True)
font2 = pygame.font.SysFont("MS Sans Serif", 100, bold=True)
font3 = pygame.font.SysFont("MS Sans Serif", 40, bold=True)
font_letter_saved = pygame.font.SysFont("MS Sans Serif", 100, bold=False)
font_error = pygame.font.SysFont("MS Sans Serif", 70, bold=False)
font_word = pygame.font.SysFont("MS Sans Serif", 70, bold=True)

text = "SPIN"
padding = 10
surf = font.render(text, True, "black")
word = ""
letter = "-"
text_letter_saved = "saved!"
text_error = "unable to save..."
text_word = word
surf_word = font_word.render(text_word, True, "black")

button1 = pygame.Rect(150, 250, font.size(text)[0] + padding, font.size(text)[1] + padding)
button_next = pygame.Rect(250, 250, font3.size("NEXT")[0] + padding, font3.size("NEXT")[1] + padding)

surf2 = font2.render(letter, True, "black")
surf_letter_saved = font_letter_saved.render(text_letter_saved, True, "black")
surf_error = font_error.render(text_error, True, "black")
surf3 = font3.render("NEXT", True, "black")

def draw_button(button, surf):
    pygame.draw.rect(screen, (110, 110, 110), button)
    screen.blit(surf, (button.x + (padding / 2), button.y + (padding / 2)))

while True:
    screen.fill((255, 255, 255))

    screen.blit(surf_word, (30, 40))
    screen.blit(surf2, (220, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                letter = random.choice(string.ascii_uppercase)
                surf2 = font2.render(letter, True, "black")

            elif button_next.collidepoint(event.pos):
                if letter == "-":
                    screen.blit(surf_error, (70, 300))
                else:
                    word += letter
                    screen.blit(surf_letter_saved, (140, 300))

                letter = "-"
                surf2 = font2.render(letter, True, "black")
                surf_word = font_word.render(word, True, "black")

    draw_button(button1, surf)
    draw_button(button_next, surf3)

    pygame.display.update()
