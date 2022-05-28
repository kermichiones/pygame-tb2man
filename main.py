import pygame
import sys
import random
from pygame.locals import *

pygame.init()

class Character:
    def __init__(self, image_dir):
        self.Character_movement = 0
        self.Character = pygame.image.load(image_dir).convert_alpha()
        self.Character = pygame.transform.flip(self.Character, True, False)
        self.Character = pygame.transform.scale(self.Character, (135, 50))
        self.rec_Character = self.Character.get_rect(center=(120, 100))
        self.collission_rect = self.rec_Character
    def check_collision(self, list_of_rects_tank):
        for tank in list_of_rects_tank:
            if tank.colliderect(self.collission_rect):
                return True
        if self.rec_Character.top <= -50 or self.rec_Character.bottom >= 510:
            return True
        for missile in missile_list:
            if missile.Missile_Rect.colliderect(self.collission_rect):
                return True
        return False
class Missiles:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Missile = pygame.image.load('assets/missile.png').convert_alpha()
        self.Missile = pygame.transform.scale(self.Missile, (30, 8))
        self.Missile = pygame.transform.rotate(self.Missile, 30)
        self.Missile = pygame.transform.flip(self.Missile, True, False)
        self.Missile_Rect = self.Missile.get_rect(center=(x, y))
        self.rand = random.uniform(1.0, 5.0)

    def movemissiles(self):
        self.Missile_Rect.centery -= self.rand
        self.Missile_Rect.centerx -= self.rand
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        s1 = random.randint(30,60)
        s2 = random.randint(150,200)
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 10):
            img = pygame.image.load(f"assets/exp{num}.png")
            if size == 2:
                img = pygame.transform.scale(img, (s1, s1))
            if size == 3:
                img = pygame.transform.scale(img, (s2, s2))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0
    def update(self):
        explosion_speed = 3
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()
class CharacterMissiles:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Missile = pygame.image.load('assets/umtas.png').convert_alpha()
        self.Missile = pygame.transform.scale(self.Missile, (40, 10))
        self.Missile_Rect = self.Missile.get_rect(center=(x+20, y+10))
    def movemissiles(self):
        self.Missile_Rect.centery += 4

    def check_collision(self, list_of_rects_tank):
        for tank in list_of_rects_tank:
            if tank.colliderect(self.Missile_Rect):
                return True
        return False

def createtank():
    new_tank = tank_img.get_rect(center=(900, 470))
    return new_tank

def movetank(tanks):
    for tank in tanks:
        tank.centerx -= 1
    return tanks

def drawtanks(tanks):
    for tank in tanks:
        screen.blit(tank_img, tank)

def drawfloor():
    global floor_x
    screen.blit(floor, (floor_x, 500))
    screen.blit(floor, (floor_x + 800, 500))
    floor_x -= 1
    if floor_x == -800:
        floor_x = 0

def game_over():
    global missilenum, bayraktar, score, tank_list, missile_list, missile_character_list, background, screen, clock

    screen.blit(background, (0, 0))
    font = pygame.font.SysFont("Comicsans", 32)
    text = font.render("Çarptınız, Skorunuz : " + str(score), True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)
    replay = pygame.font.SysFont("Comicsans", 32)
    text = replay.render("Tekrar oynamak için R tuşuna basınız", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 350))
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tank_list.clear()
                missile_list.clear()
                missile_character_list.clear()
                score = 0
                bayraktar = Character("assets/bayraktar.png")
                missilenum = 6
    pygame.display.update()
    clock.tick(60)


def game_win(bg, flr, mslnum, finishbg, end=False):
    global bayraktar, score, tank_list, missile_list, missile_character_list, background, screen, clock, started, missilenum, win, floor, explosion_group
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                pygame.time.set_timer(SPAWNTANK, 4500)
                win = False
                tank_list.clear()
                missile_list.clear()
                missile_character_list.clear()
                score = 0
                bayraktar = Character("assets/bayraktar.png")
                missilenum = mslnum
                floor = pygame.image.load(flr).convert_alpha()
                explosion_group.empty()
                background = pygame.image.load(bg)
                background = pygame.transform.scale(background, (800, 600))
                if end == False:
                    level2()
                else:
                    level3()
    screen.blit(pygame.image.load(finishbg), (0, 0))
    pygame.display.update()
    clock.tick(60)

def start_screen():
    global bayraktar, score, tank_list, missile_list, missile_character_list, background, screen, clock, started, missilenum
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tank_list.clear()
                missile_list.clear()
                missile_character_list.clear()
                score = 0
                bayraktar = Character("assets/bayraktar.png")
                started = True
    screen.blit(intro, (0, 0))
    pygame.display.update()
    clock.tick(60)
def events():
    global missilenum
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and missilenum > 0:
                missile_character_list.append(
                    CharacterMissiles(bayraktar.rec_Character.centerx, bayraktar.rec_Character.centery))
                missilenum -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE:
                bayraktar.Character_movement = 0
                bayraktar.Character_movement = -5
            if event.key == pygame.K_f:
                missile_character_list.append(
                    CharacterMissiles(bayraktar.rec_Character.centerx, bayraktar.rec_Character.centery))
                missilenum -= 1
        if event.type == SPAWNTANK and bayraktar.check_collision(tank_list) == False:
            tank_list.append(createtank())
        if event.type == SPAWNMISSILE and bayraktar.check_collision(tank_list) == False:
            for tanknum in tank_list:
                missile_list.append(Missiles(tanknum.x, tanknum.y))

explosion_group = pygame.sprite.Group()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TB2MAN")
icon = pygame.image.load("assets/icon.jpg")
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)
background = pygame.image.load("assets/Background_01.png").convert()
intro = pygame.image.load("assets/intro.png").convert()
background = pygame.transform.scale(background, (800, 600))

bayraktar = Character("assets/bayraktar.png")
missilenum = 6
win = False
count = 0
started = False
score = 0
gravity = 0.25
clock = pygame.time.Clock()
floor = pygame.image.load("assets/floor (2).png").convert()
floor_x = 0
pygame.mixer.music.load('assets/bayraktartheme.mp3')
pygame.mixer.music.play(-1)
SPAWNMISSILE = pygame.USEREVENT
pygame.time.set_timer(SPAWNMISSILE, 1000)
SPAWNTANK = pygame.USEREVENT
pygame.time.set_timer(SPAWNTANK, 7000)
tank_img = pygame.image.load("assets/tank.png").convert_alpha()
tank_img = pygame.transform.scale(tank_img, (173, 86))
tank_list = []
missile_list = []
missile_character_list = []
def level1():
    print("level 1")
    while True:
        def main():
            global text, count, screen, background, bayraktar, score, gravity, clock, tank_list, missile_list, missile_character_list, missilenum, win
            events()
            screen.blit(background, (0, 0))
            font = pygame.font.SysFont("", 36)
            if missilenum != 0:
                text = font.render("Kalan Füze: " + str(missilenum), True, (255, 255, 255))
            else:
                if count%5 != 0:
                    text = font.render(" FÜZE YOK! KAMIKAZE YAP", True, (255,0,0))
                else:
                    text = font.render("", True, (255, 255, 255))
                count += 1

            screen.blit(text, (0, 0))
            text2 = font.render("Yok Edilen Tank Sayısı: " + str(score), True, (255, 255, 255))
            screen.blit(text2, (460, 0))

            bayraktar.Character_movement += gravity
            bayraktar.rec_Character.y += bayraktar.Character_movement
            screen.blit(bayraktar.Character, bayraktar.rec_Character)
            if score == 4:
                win = True
            for missile_num in missile_list:
                screen.blit(missile_num.Missile, missile_num.Missile_Rect)
                missile_num.movemissiles()
                if missile_num.Missile_Rect.y < -50:
                    missile_list.remove(missile_num)
            for character_m in missile_character_list:
                screen.blit(character_m.Missile, character_m.Missile_Rect)
                character_m.movemissiles()
                character_m.check_collision(tank_list)
                for tank_num in tank_list:
                    if character_m.Missile_Rect.colliderect(tank_num):
                        tank_list.remove(tank_num)
                        missile_character_list.remove(character_m)
                        explosion = Explosion(tank_num.centerx, tank_num.centery, 3)
                        explosion_group.add(explosion)
                        explosion2 = Explosion(character_m.Missile_Rect.centerx, character_m.Missile_Rect.centery, 2)
                        explosion_group.add(explosion2)
                        score += 1
                if character_m.Missile_Rect.bottom >= 500:
                    missile_character_list.remove(character_m)
                    explosion3 = Explosion(character_m.Missile_Rect.centerx, character_m.Missile_Rect.centery, 3)
                    explosion_group.add(explosion3)
            for tank_num in tank_list:
                if tank_num.x <= -180:
                    tank_list.remove(tank_num)
            drawfloor()
            tank_list = movetank(tank_list)
            drawtanks(tank_list)
            explosion_group.update()
            explosion_group.draw(screen)
            pygame.display.update()
            clock.tick(60)
        if bayraktar.check_collision(tank_list) == True:
            game_over()
        if started == False:
            start_screen()
        if win == True:
            game_win("assets/Background_02.png", "assets/floorl2.png",7 ,"assets/firstwin.png")
        if bayraktar.check_collision(tank_list) == False and started == True and win==False:
            main()
def level2():
    print("level 2")
    while True:
        def main():
            global text, count, screen, background, bayraktar, score, gravity, clock, tank_list, missile_list, missile_character_list, missilenum, win
            events()
            screen.blit(background, (0, 0))
            font = pygame.font.SysFont("", 36)
            if missilenum != 0:
                text = font.render("Kalan Füze: " + str(missilenum), True, (255, 255, 255))
            else:
                if count % 5 != 0:
                    text = font.render(" FÜZE YOK! KAMIKAZE YAP", True, (255, 0, 0))
                else:
                    text = font.render("", True, (255, 255, 255))
                count += 1

            screen.blit(text, (0, 0))
            text2 = font.render("Yok Edilen Tank Sayısı: " + str(score), True, (255, 255, 255))
            screen.blit(text2, (460, 0))

            bayraktar.Character_movement += gravity
            bayraktar.rec_Character.y += bayraktar.Character_movement
            screen.blit(bayraktar.Character, bayraktar.rec_Character)
            if score == 5:
                win = True
            for missile_num in missile_list:
                screen.blit(missile_num.Missile, missile_num.Missile_Rect)
                missile_num.movemissiles()
                if missile_num.Missile_Rect.y < -50:
                    missile_list.remove(missile_num)
            for character_m in missile_character_list:
                screen.blit(character_m.Missile, character_m.Missile_Rect)
                character_m.movemissiles()
                character_m.check_collision(tank_list)
                for tank_num in tank_list:
                    if character_m.Missile_Rect.colliderect(tank_num):
                        tank_list.remove(tank_num)
                        missile_character_list.remove(character_m)
                        explosion = Explosion(tank_num.centerx, tank_num.centery, 3)
                        explosion_group.add(explosion)
                        explosion2 = Explosion(character_m.Missile_Rect.centerx, character_m.Missile_Rect.centery, 2)
                        explosion_group.add(explosion2)
                        score += 1
                if character_m.Missile_Rect.bottom >= 500:
                    missile_character_list.remove(character_m)
                    explosion3 = Explosion(character_m.Missile_Rect.centerx, character_m.Missile_Rect.centery, 3)
                    explosion_group.add(explosion3)
            for tank_num in tank_list:
                if tank_num.x <= -180:
                    tank_list.remove(tank_num)
            drawfloor()
            tank_list = movetank(tank_list)
            drawtanks(tank_list)
            explosion_group.update()
            explosion_group.draw(screen)
            pygame.display.update()
            clock.tick(60)
        if bayraktar.check_collision(tank_list) == True:
            game_over()
        if started == False:
            start_screen()
        if win == True:
            game_win("assets/background_03.png", "assets/floorl2.png", 6, "assets/secondwin.png", True)
        if bayraktar.check_collision(tank_list) == False and started == True and win == False:
            main()
def level3():
    print("level 3")
    while True:
        def main():
            global text, count, screen, background, bayraktar, score, gravity, clock, tank_list, missile_list, missile_character_list, missilenum, win
            events()
            screen.blit(background, (0, 0))
            font = pygame.font.SysFont(None, 36)
            if missilenum != 0:
                text = font.render("Kalan Füze: " + str(missilenum), True, (255, 255, 255))
            else:
                if count % 5 != 0:
                    text = font.render(" FÜZE YOK! KAMIKAZE YAP", True, (255, 0, 0))
                else:
                    text = font.render("", True, (255, 255, 255))
                count += 1

            screen.blit(text, (0, 0))
            text2 = font.render("Yok Edilen Tank Sayısı: " + str(score), True, (255, 255, 255))
            screen.blit(text2, (460, 0))
            bayraktar.Character_movement += gravity
            bayraktar.rec_Character.y += bayraktar.Character_movement
            screen.blit(bayraktar.Character, bayraktar.rec_Character)
            if score == 5:
                win = True
            for missile_num in missile_list:
                screen.blit(missile_num.Missile, missile_num.Missile_Rect)
                missile_num.movemissiles()
                if missile_num.Missile_Rect.y < -50:
                    missile_list.remove(missile_num)
            for character_m in missile_character_list:
                screen.blit(character_m.Missile, character_m.Missile_Rect)
                character_m.movemissiles()
                character_m.check_collision(tank_list)
                for tank_num in tank_list:
                    if character_m.Missile_Rect.colliderect(tank_num):
                        tank_list.remove(tank_num)
                        missile_character_list.remove(character_m)
                        explosion = Explosion(tank_num.centerx, tank_num.centery, 3)
                        explosion_group.add(explosion)
                        explosion2 = Explosion(character_m.Missile_Rect.centerx, character_m.Missile_Rect.centery, 2)
                        explosion_group.add(explosion2)
                        score += 1
                if character_m.Missile_Rect.bottom >= 500:
                    missile_character_list.remove(character_m)
                    explosion3 = Explosion(character_m.Missile_Rect.centerx, character_m.Missile_Rect.centery, 3)
                    explosion_group.add(explosion3)
            for tank_num in tank_list:
                if tank_num.x <= -180:
                    tank_list.remove(tank_num)
            drawfloor()
            tank_list = movetank(tank_list)
            drawtanks(tank_list)
            explosion_group.update()
            explosion_group.draw(screen)
            pygame.display.update()
            clock.tick(60)
        def game_finish():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        pygame.quit()
                        sys.exit()

            screen.blit(pygame.transform.scale(pygame.image.load("assets/outro.png"), (800,600)), (0, 0))
            pygame.display.update()
            clock.tick(60)
        if bayraktar.check_collision(tank_list) == True:
            game_over()
        if started == False:
            start_screen()
        if win == True:
            game_finish()
        if bayraktar.check_collision(tank_list) == False and started == True and win == False:
            main()
level1()