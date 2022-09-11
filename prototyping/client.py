import pygame
from network import Network
from player import Player

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redraw_window(window, p1, p2):
    window.fill((255, 255, 255))
    p1.draw(window)
    p2.draw(window)
    pygame.display.update()


def main():
    run = True
    net = Network()
    p1 = net.getP()
    while run:

        p2 = net.send(p1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move()
        redraw_window(window, p1, p2)


if __name__ == "__main__":
    main()
