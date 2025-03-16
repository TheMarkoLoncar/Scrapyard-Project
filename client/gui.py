import pygame
import client

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Morse Code Translator")

font1 = pygame.font.Font("../assets/PixelOperator8.ttf", 20)
font2 = pygame.font.Font("../assets/PixelOperator8.ttf", 80)
font3 = pygame.font.Font("../assets/PixelOperator8.ttf", 50)

text = "SPIN"
padding = 10
surf = font1.render(text, True, "black")

button1 = pygame.Rect(150, 460, font1.size(text)[0] + padding, font1.size(text)[1] + padding)
button_next = pygame.Rect(250, 460, font1.size("NEXT")[0] + padding, font1.size("NEXT")[1] + padding)

surf2 = font1.render("NEXT", True, "black")

background_img = pygame.image.load("../assets/BackgroundSlotMachine.png")
def draw_button(button, surf):
    pygame.draw.rect(screen, (110, 110, 110), button)
    screen.blit(surf, (button.x + (padding / 2), button.y + (padding / 2)))

while True:
    screen.fill((255, 255, 255))
    
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    draw_button(button1, surf)
    draw_button(button_next, surf2)

    pygame.display.update()
