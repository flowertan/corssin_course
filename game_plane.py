import pygame, random
from sys import exit

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('bullet.png').convert_alpha()
    def move(self):
        if self.y < 0:
            mouseX, mouseY = pygame.mouse.get_pos()
            self.x = mouseX - self.image.get_width() / 2
            self.y = mouseY - self.image.get_height() / 2
        else:
            self.y -= 5

class Enemy:
    def restart(self):
        self.x = random.randint(50, 400)
        self.y = random.randint(-200, -50)
        self.speed = random.random() + 0.05

    def __init__(self):
        self.restart()
        self.image = pygame.image.load('enemy.png').convert_alpha()
    def move(self):
        if self.y < 650:
            self.y += self.speed
        else:
            self.restart()

pygame.init()
screen = pygame.display.set_mode((450, 650), 0, 32)
pygame.display.set_caption("plane")
background = pygame.image.load('back.jpg').convert()
plane = pygame.image.load('plane.png').convert_alpha()
bullet = Bullet()
enemy = Enemy()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0, 0))
    bullet.move()
    screen.blit(bullet.image, (bullet.x, bullet.y))
    enemy.move()
    screen.blit(enemy.image, (enemy.x, enemy.y))

    x, y = pygame.mouse.get_pos()
    x -= plane.get_width() / 2
    y -= plane.get_height() / 2
    screen.blit(plane, (x, y))
    pygame.display.update()
