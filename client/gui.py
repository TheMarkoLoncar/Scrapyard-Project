import pygame
import random
import client
import string

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Morse Code Translator")

font1 = pygame.font.Font("../assets/PixelOperator8.ttf", 20)
font2 = pygame.font.Font("../assets/PixelOperator8.ttf", 80)
font3 = pygame.font.Font("../assets/PixelOperator8.ttf", 50)

padding = 10
scale = 1.5

spin_img = pygame.image.load("../assets/SpinButton.png")
spin_img_size = spin_img.get_size()
spin_img = pygame.transform.scale(spin_img, (spin_img_size[0] * scale, spin_img_size[1] * scale))
spin_img_size = spin_img.get_size()

next_img = pygame.image.load("../assets/NextButton.png")
next_img_size = next_img.get_size()
next_img = pygame.transform.scale(next_img, (next_img_size[0] * scale, next_img_size[1] * scale))
next_img_size = next_img.get_size()

button_spin = pygame.Rect((screen.get_width() / 2) - spin_img_size[0] - 60, 433, spin_img_size[0] + padding, spin_img_size[1] + padding)
button_next = pygame.Rect((screen.get_width() / 2) + next_img_size[0] - 60, 433, next_img_size[0] + padding, next_img_size[1] + padding)

background_img = pygame.image.load("../assets/BackgroundSlotMachine.png")
dash_img = pygame.image.load("../assets/ResultSlotDash.png")
dot_img = pygame.image.load("../assets/ResultSlotDot.png")
space_img = pygame.image.load("../assets/ResultSlotSpace.png")
slash_img = pygame.image.load("../assets/ResultSlotSlash.png")

def draw_button(button, texture):
    screen.blit(texture, (button.x + (padding / 2), button.y + (padding / 2)))

def main():
    client.setup_recieving()
    
    letter = ""
    while True:
        screen.fill((255, 255, 255))
    
        screen.blit(background_img, (0, -25))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_spin.collidepoint(event.pos):
                    letter = random.choice(string.ascii_lowercase + " ")
                elif button_next.collidepoint(event.pos):
                    pass

        draw_button(button_spin, spin_img)
        draw_button(button_next, next_img)
    
        for i in range(4):
            mc_letter = client.letters[letter]
            pos = (90 * i + (78 if i == 1 else 79), 232)
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
        
if __name__ == "__main__":
    main()