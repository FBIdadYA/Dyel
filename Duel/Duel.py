#Игра Дуель
from pygame import *
from time import time as timer
from random import randint
#модули пайгейм и времени
window = display.set_mode((800, 450))
display.set_caption('Duel')
background = transform.scale(image.load('fonn.png'), (800, 450))




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450 - 60:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450 - 60:
            self.rect.y += self.speed

player1 = Player1("igrok2.png", 10, 175, 60, 50, 10)
player2 = Player2("igrok.png", 730, 175, 60, 50, 10)
#myachik = GameSprite("Myachik.png", 360, 210, 49, 49, 2)
bochki = sprite.Group()
for i in range(5):
    x = randint(100, 625)
    y = randint(25, 350)
    bochka = GameSprite("bockla.png", x, y, 75, 75, 0)
    bochki.add(bochka)

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player1.reset()
        player2.reset()
        player1.update()
        player2.update()
        bochki.draw(window)



        display.update()
        time.delay(20)