import pygame
import random
import client
import string
import time

pygame.init()

screen = pygame.display.set_mode((500, 570))
pygame.display.set_caption("Morse Code Translator")

font1 = pygame.font.Font("../assets/PixelOperator8.ttf", 20)
font2 = pygame.font.Font("../assets/PixelOperator8.ttf", 80)
font3 = pygame.font.Font("../assets/PixelOperator8.ttf", 50)

word = ""
text = "SPIN"
padding = 10
surf = font1.render(text, True, "black")

button1 = pygame.Rect(150, 520, font1.size(text)[0] + padding, font1.size(text)[1] + padding)
button_next = pygame.Rect(250, 520, font1.size("NEXT")[0] + padding, font1.size("NEXT")[1] + padding)

surf2 = font1.render("NEXT", True, "black")
surf_word = font3.render(word, True, "black")

background_img = pygame.image.load("../assets/BackgroundSlotMachine.png")
dash_img = pygame.image.load("../assets/ResultSlotDash.png")
dot_img = pygame.image.load("../assets/ResultSlotDot.png")
space_img = pygame.image.load("../assets/ResultSlotSpace.png")
slash_img = pygame.image.load("../assets/ResultSlotSlash.png")

cycle_dash_img = pygame.image.load("../assets/CycleSlotDash.png")
cycle_dot_img = pygame.image.load("../assets/CycleSlotDot.png")
cycle_space_img = pygame.image.load("../assets/CycleSlotSpace.png")
cycle_slash_img = pygame.image.load("../assets/CycleSlotSlash.png")

def draw_button(button, surf):
    pygame.draw.rect(screen, (110, 110, 110), button)
    screen.blit(surf, (button.x + (padding / 2), button.y + (padding / 2)))

def update_letter(letter, cycle):
    for i in range(4):
        mc_letter = client.letters[letter]
        pos = (90 * i + 79, 287)
        if i < len(mc_letter):
            match(mc_letter[i]):
                case "-":
                    screen.blit(cycle_dash_img if cycle else dash_img, pos)
                case ".":
                    screen.blit(cycle_dot_img if cycle else dot_img, pos)
                case "/":
                    screen.blit(cycle_slash_img if cycle else slash_img, pos)
                case " ":
                    screen.blit(cycle_space_img if cycle else space_img, pos)
letter = ""
while True:
    screen.fill((255, 255, 255))
    screen.blit(background_img, (0, 30))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                for i in range(4):
                    update_letter(random.choice(string.ascii_lowercase), True)
                    time.sleep(1 / (4 - i))

                letter = random.choice(string.ascii_lowercase + " ")
            elif button_next.collidepoint(event.pos):
                if letter == "":
                    continue
                else:
                    letter_saved = letter
                    word += letter_saved
                    letter = ""
                    print(letter_saved)
                    print(word)
                    surf_word = font3.render(word, True, "black")
                    

    draw_button(button1, surf)
    draw_button(button_next, surf2)
    screen.blit(surf_word, (10, 10))

    update_letter(letter, False)

    pygame.display.update()