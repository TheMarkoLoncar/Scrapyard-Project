import pygame
import random
import client
import string

pygame.init()

screen = pygame.display.set_mode((500, 550))
pygame.display.set_caption("Morse Code Translator")

font1 = pygame.font.Font("../assets/PixelOperator8.ttf", 20)
font2 = pygame.font.Font("../assets/PixelOperator8.ttf", 80)
font3 = pygame.font.Font("../assets/PixelOperator8.ttf", 50)

text = "SPIN"
padding = 10
surf = font1.render(text, True, "black")

button1 = pygame.Rect(150, 510, font1.size(text)[0] + padding, font1.size(text)[1] + padding)
button_next = pygame.Rect(250, 510, font1.size("NEXT")[0] + padding, font1.size("NEXT")[1] + padding)

surf2 = font1.render("NEXT", True, "black")

background_img = pygame.image.load("../assets/BackgroundSlotMachine.png")
dash_img = pygame.image.load("../assets/ResultSlotDash.png")
dot_img = pygame.image.load("../assets/ResultSlotDot.png")
space_img = pygame.image.load("../assets/ResultSlotSpace.png")
slash_img = pygame.image.load("../assets/ResultSlotSlash.png")

def draw_button(button, surf):
    pygame.draw.rect(screen, (110, 110, 110), button)
    screen.blit(surf, (button.x + (padding / 2), button.y + (padding / 2)))

letter = ""
while True:
    screen.fill((255, 255, 255))
    
    screen.blit(background_img, (0, 50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                letter = random.choice(string.ascii_lowercase + " ")
            elif button_next.collidepoint(event.pos):
                pass

    draw_button(button1, surf)
    draw_button(button_next, surf2)

    for i in range(4):
        mc_letter = client.letters[letter]
        pos = (90 * i + 79, 307)
        if i < len(mc_letter):
            match(mc_letter[i]):
                case "-":
                    screen.blit(dash_img, pos)
                case ".":
                    screen.blit(dot_img, pos)
                case "/":
                    screen.blit(slash_img, pos)
        else:
            screen.blit(space_img, pos)

    pygame.display.update()