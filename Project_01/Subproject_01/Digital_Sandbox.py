import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Sandbox")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, (0, 255, 0), (mouse_x, mouse_y), 20)

    pygame.display.flip()

pygame.quit()