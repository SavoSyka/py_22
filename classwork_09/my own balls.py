import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 50
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    """Конструктор класса Ball"""
    def __init__(self):
        self.r = randint(15, 100)
        self.x = randint(2 * self.r, 1200 - 2 * self.r)
        self.y = randint(2 * self.r, 900 - 2 * self.r)
        self.vx = randint(-7, 7)
        self.vy = randint(-7, 7)
        self.color = COLORS[randint(0, 5)]

    def is_reflection(self):
        """Проверяет, сталкивааеися ли шар с краем экрана"""
        if self.x + self.r >= 1200:
            self.reflection_x()
        if self.x - self.r <= 0:
            self.reflection_x()
        if self.y + self.r >= 900:
            self.reflection_y()
        if self.y - self.r <= 0:
            self.reflection_y()

    def reflection_x(self):
        """Меняет горизонтальную составляющую скорости шара на противоположную"""
        self.vx = -self.vx

    def reflection_y(self):
        """Меняет вертикальную составляющую скорости шара на противоположную"""
        self.vy = -self.vy

    def move(self):
        """Равномерно двигает шар"""
        self.x += self.vx
        self.y += self.vy

    def draw_ball(self):
        """Рисует шар на экране"""
        circle(screen, self.color, (self.x, self.y), self.r)

    def is_hit(self):
        """Проверяет попал ли щелчок мыши по шару"""
        if (self.x - event.pos[0]) ** 2 + (self.y - event.pos[1]) ** 2 <= self.r ** 2:
            return True
        else:
            return False

    def is_miss(self):
        """Проверяет был ли промах по шару при щелчке мышью"""
        if (self.x - event.pos[0]) ** 2 + (self.y - event.pos[1]) ** 2 > self.r ** 2 and miss:
            return True
        else:
            return False


def score_of_gamer():
    """Выводит на экран количество набранных очков"""
    myfont = pygame.font.SysFont("monospace", 50)
    scoretext = myfont.render("Счет: " + str(balls_counter), 1, (255, 255, 255))
    screen.blit(scoretext, (10, 7))
    miss = myfont.render("Промахов: " + str(miss_counter), 1, (255, 255, 255))
    screen.blit(miss, (10, 60))


def ball_wave():
    """Выводит на экран порядковый номер волны шаров"""
    myfont = pygame.font.SysFont("monospace", 50)
    wavetext = myfont.render("Волна: " + str(wave), 1, (255, 255, 255))
    screen.blit(wavetext, (10, 110))


def stats():
    """Выводит на экран статистику игрока по окончанию игры"""
    myfont = pygame.font.SysFont("monospace", 50)
    wave_final = myfont.render(f'Пройденно волн: {str(wave)} ', 1, (255, 255, 255))
    screen.blit(wave_final, (270, 250))
    balls_final = myfont.render(
        f'Попаданий по шарам: {balls_counter}', 1,
        (255, 255, 255))
    screen.blit(balls_final, (270, 350))
    miss_final = myfont.render(
        f'Промахов: {miss_counter} ', 1,
        (255, 255, 255))
    screen.blit(miss_final, (270, 450))
    accuracy = myfont.render(
        f'Точность: {balls_counter / (miss_counter + balls_counter)} ', 1,
        (255, 255, 255))
    screen.blit(accuracy, (270, 550))


amount_of_balls = 5  # Начальное количество шаров на экране
balls = [0] * amount_of_balls  # Список шаров

pygame.display.update()
clock = pygame.time.Clock()
finished = False
balls_counter = 0  # Счетчик попаданий по шарам
miss_counter = 0  # Счетчик промахов
miss = True
amount_of_balls_on_the_display = 5  # Количество шаров на экране
live = [0] * amount_of_balls  # список "жизней" шаров
wave = 1  # Номер волны шаров

for i in range(amount_of_balls):
    balls[i] = Ball()
    balls[i].draw_ball()
    live[i] = True

while not finished:
    for i in range(amount_of_balls):
        balls[i].is_reflection()
    pygame.display.update()
    if 0 < amount_of_balls_on_the_display <= amount_of_balls:
        screen.fill(BLACK)
        for i in range(amount_of_balls):
            if live[i]:
                balls[i].draw_ball()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.fill(BLACK)
                stats()
                pygame.display.update()
                clock.tick(FPS / 150)
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(amount_of_balls):
                    if balls[i].is_hit():
                        live[i] = False
                        balls_counter += 1
                        amount_of_balls_on_the_display -= 1
                        miss = False
                for i in range(amount_of_balls):
                    if balls[i].is_miss():
                        miss_counter += 1
                        break
        for i in range(amount_of_balls):
            balls[i].move()
    else:
        amount_of_balls_on_the_display = amount_of_balls
        for i in range(amount_of_balls):
            balls[i] = Ball()
            balls[i].draw_ball()
            live[i] = True
        wave += 1
    miss = True
    score_of_gamer()
    ball_wave()

pygame.quit()
