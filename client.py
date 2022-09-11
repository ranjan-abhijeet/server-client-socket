import pygame
from network import Network

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


class Player(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 1

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    try:
        str = str.split(",")
        return int(str[0]), int(str[1])
    except Exception as err:
        print(str)
        print("[-] Error")


def make_pos(tup):
    return str(tup[0]) + ","+str(tup[1])


def redraw_window(window, p1, p2):
    window.fill((255, 255, 255))
    p1.draw(window)
    p2.draw(window)
    pygame.display.update()


def main():
    run = True
    net = Network()
    start_pos = read_pos(net.getPos())
    p1 = Player(start_pos[0], start_pos[1], 50, 50, (0, 255, 0))
    p2 = Player(0, 0, 50, 50, (255, 0, 0))

    while run:

        p2_pos = read_pos(net.send(make_pos((p1.x, p1.y))))
        p2.x = p2_pos[0]
        p2.y = p2_pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move()
        redraw_window(window, p1, p2)


if __name__ == "__main__":
    main()
