#Игра Дуель
from pygame import *
from time import time as timer
from random import randint
#модули пайгейм и времени
window = display.set_mode((800, 450))
display.set_caption('Duel')
background = transform.scale(image.load('fonn.png'), (800, 450))
#экран

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, life):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.lifes = life
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#прородитель класов

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450 - 60:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet('pyla2.png', self.rect.x + 60, self.rect.centery -8, 22, 15, 16, 0)
        bullets.add(bullet)
#клас левого игрока

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450 - 60:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet('pyla.png', self.rect.x - 5, self.rect.centery -8, 22, 15, -16, 0)
        bullets.add(bullet)
#клас правого игрока

class Bullet(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.kill()
        elif self.rect.x > 800:
            self.kill()
#клас пули

class Cactuss(GameSprite):
    def update(self):
        #keys = key.get_pressed()
        if self.lifes == 4:
            self.image = transform.scale(image.load('cactus4.png'), (75, 75))
        if self.lifes == 3:
            self.image = transform.scale(image.load('cactus3.png'), (75, 75))
        if self.lifes == 2:
            self.image = transform.scale(image.load('cactus2.png'), (75, 75))
        if self.lifes == 1:
            self.image = transform.scale(image.load('cactus1.png'), (75, 75))
        if self.lifes <= 0:
            cactus_d = GameSprite('cactus0.png', self.rect.x, self.rect.y, 75, 75, 0, 0)
            cactusi_dead.add(cactus_d)
            self.kill()
#клас кактуса

player1 = Player1("igrok2.png", 10, 175, 60, 50, 7, 5)
player2 = Player2("igrok.png", 730, 175, 60, 50, 7, 5)

bochki = sprite.Group()
for i in range(5):
    x = randint(100, 625)
    y = randint(25, 350)
    bochka = GameSprite("bockla1.png", x, y, 75, 75, 0, 1)
    bochki.add(bochka)

cactusi = sprite.Group()
for i in range(5):
    xx = randint(100, 625)
    yy = randint(25, 350)
    cactus = Cactuss("cactus5.png", xx, yy, 75, 75, 0, 5)
    cactusi.add(cactus)

cactusi_dead = sprite.Group()
bullets = sprite.Group() 

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player1.fire()
            if e.key == K_RCTRL:
                player2.fire()
    if finish != True:
        window.blit(background, (0,0))
        player1.reset()
        player2.reset()
        player1.update()
        player2.update()
        bullets.update()
        cactusi.update()
        bochki.draw(window)
        cactusi.draw(window)
        cactusi_dead.draw(window)
        bullets.draw(window)
        sprite.groupcollide(bullets, bochki, True, True)
        ccc = sprite.groupcollide(cactusi, bullets, False, True)
        for c in ccc:
            c.lifes -= 1 
        display.update()
        time.delay(20)