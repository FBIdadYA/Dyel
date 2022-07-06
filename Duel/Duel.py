#Игра Дуель
from pygame import *
from time import time as timer
from random import randint
#модули пайгейм и времени
window = display.set_mode((800, 450))
display.set_caption('Duel')
background = transform.scale(image.load('fonn.png'), (800, 450))
#экран

mixer.init()
mixer.music.load('pust.ogg')
mixer.music.play()
vust_sound = mixer.Sound('vust.ogg')
perez_sound = mixer.Sound('perez.ogg')
wood_sound = mixer.Sound('wood.ogg')
cacts_sound = mixer.Sound('cacts.ogg')
#звуки

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
        bullet = Bullet('pyla.png', self.rect.x - 15, self.rect.centery -8, 22, 15, -16, 0)
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
#настройки игроков

bochki = sprite.Group()
for i in range(5):
    x = randint(100, 625)
    y = randint(25, 350)
    bochka = GameSprite("bockla1.png", x, y, 75, 75, 0, 1)
    bochki.add(bochka)
#расположение бочек

cactusi = sprite.Group()
for i in range(5):
    xx = randint(100, 625)
    yy = randint(25, 350)
    cactus = Cactuss("cactus5.png", xx, yy, 75, 75, 0, 5)
    cactusi.add(cactus)
#расположение кактусов

cactusi_dead = sprite.Group()
bullets = sprite.Group() 
#група объектов

finish = False
game = True

life_l = 6
life_r = 6
#жизни

rel_time1 = False
num_fire1 = 0
rel_time2 = False
num_fire2 = 0
#контроль перезарядки игроков

font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 22)
lose1 = font1.render('player L win', True, (180, 0, 0))
lose2 = font1.render('player R win', True, (180, 0, 0))
#тексты и шрифты

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if finish != True:
                if e.key == K_SPACE:
                    if num_fire1 < 6 and rel_time1 == False:
                        num_fire1 += 1
                        player1.fire()
                        vust_sound.play()
                    if num_fire1 >= 6 and rel_time1 == False:
                        last_time1 = timer()
                        perez_sound.play()
                        rel_time1 = True
                if e.key == K_RCTRL:
                    if num_fire2 < 6 and rel_time2 == False:
                        num_fire2 += 1
                        player2.fire()
                        vust_sound.play()
                    if num_fire2 >= 6 and rel_time2 == False:
                        last_time2 = timer()
                        perez_sound.play()
                        rel_time2 = True
                #контроль клавиш
    if finish != True:
        window.blit(background, (0,0))
        player1.reset()
        player2.reset()
        text_life_1 = font2.render(str(life_l), 1, (150, 0, 0,))
        text_life_2 = font2.render(str(life_r), 1, (150, 0, 0,))
        window.blit(text_life_1, (player1.rect.x + 25, player1.rect.y + 50))
        window.blit(text_life_2, (player2.rect.x + 25, player2.rect.y + 50))
        player1.update()
        player2.update()
        bullets.update()
        cactusi.update()
        bochki.draw(window)
        cactusi.draw(window)
        cactusi_dead.draw(window)
        bullets.draw(window)
        #отображение фона, объектов и игроков на экране
        bbb = sprite.groupcollide(bochki, bullets, False, False)
        for b in bbb:
            sprite.groupcollide(bochki, bullets, False, True)
            wood_sound.play()
            bochka_dead = GameSprite("bockla0.png", b.rect.x, b.rect.y, 75, 75, 0, 0)
            cactusi_dead.add(bochka_dead)
            b.kill()
            #разрушение бочек
        ccc = sprite.groupcollide(cactusi, bullets, False, True)
        for c in ccc:
            c.lifes -= 1
            cacts_sound.play()
            #разрушение кактусов
        if sprite.spritecollide(player1, bullets, True):
            life_l -= 1
        if sprite.spritecollide(player2, bullets, True):
            life_r -= 1
        if life_l <= 0:
            window.blit(lose2, (300, 250))
            finish = True
        if life_r <= 0:
            window.blit(lose1, (300, 250))
            finish = True
            #условие победы
        if rel_time1 == True:
            now_time1 = timer()
            if now_time1 - last_time1 < 5:
                reload = font2.render('reload', 1, (150, 0, 0,))
                window.blit(reload, (player1.rect.x, player1.rect.y - 25))
            else:
                num_fire1 = 0
                rel_time1 = False
        if rel_time2 == True:
            now_time2 = timer()
            if now_time2 - last_time2 < 5:
                reload = font2.render('reload', 1, (150, 0, 0,))
                window.blit(reload, (player2.rect.x, player2.rect.y - 25))
            else:
                num_fire2 = 0
                rel_time2 = False
         #перезарадка двух игроков
        display.update()
        time.delay(20)