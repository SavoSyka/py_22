import pygame
from pygame.draw import circle
from random import randint
from math import cos, sin, radians

pygame.init()

# Настройка экрана
FPS = 150
display_size = (1000, 700)
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption('Catch my big nice balls')

# Настройка размеров шаров
max_ball_size = 100
min_ball_size = 10

# Настройка цветов
RED = (255, 100, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# Счётчик попаданий
counter = 0


# Определение необходимых функций
def new_ball():
    """Создаёт новый шарик со случайным радиусом в случайном месте"""
    x_ball = randint(max_ball_size, display_size[0] - max_ball_size)
    y_ball = randint(max_ball_size, display_size[1] - max_ball_size)
    r_ball = randint(min_ball_size, max_ball_size)
    alpha = randint(0, 359)
    color = COLORS[randint(0, 5)]
    params = [color, [x_ball, y_ball], r_ball, alpha]
    return params


def get_starting_objects(obj_count=3):
    """Создаёт список первых шаров"""
    starting_objects = []
    for _ in range(obj_count):
        ball = new_ball()
        starting_objects.append(ball)
    return starting_objects


def objects_draw():
    """Рисует шары из списка на экране"""
    for object in objects_on_screen:
        circle(screen, *object[:-1])


def is_catch(x_ball, y_ball, r):
    """Проверяет, есть ли попадание по объекту
    x_ball —  координата центра объекта по оси X
    y_ball — координата центра объекта по оси Y
    ro — радиус объекта"""
    x_mouse, y_mouse = pygame.mouse.get_pos()
    return (x_ball - x_mouse) ** 2 + (y_ball - y_mouse) ** 2 <= r ** 2


def is_collision_with_wall(obiect):
    """Проверяет, сталкивается ли объект с краем экрана и изменяет направление его движения с учетом ЗСИ"""
    if obiect[1][0] + cos(radians(obiect[3])) - obiect[2] < 0:
        obiect[3] = 180 - obiect[3]
    elif obiect[1][0] + cos(radians(obiect[3])) + obiect[2] > display_size[0]:
        obiect[3] = 180 - obiect[3]
    elif obiect[1][1] + sin(radians(obiect[3])) + obiect[2] > display_size[1]:
        obiect[3] = -obiect[3]
    elif obiect[1][1] + sin(radians(obiect[3])) - obiect[2] < 0:
        obiect[3] = -obiect[3]


def move_objects():
    """Перемещает объекты"""
    for j in range(len(objects_on_screen)):
        is_collision_with_wall(objects_on_screen[j])
        x_move = cos(radians(objects_on_screen[j][3]))
        y_move = sin(radians(objects_on_screen[j][3]))
        objects_on_screen[j][1][0] += x_move
        objects_on_screen[j][1][1] += y_move


pygame.display.update()
clock = pygame.time.Clock()
finished = False
objects_on_screen = get_starting_objects()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for obj in objects_on_screen:
                x, y, r = obj[1][0], obj[1][1], obj[2]
                if is_catch(x, y, r):
                    counter += 1
                    if counter == 1:
                        print('Oh, you catch', counter, ' of my ball!')
                    else:
                        print('Oh, you catch', counter, ' of my balls!')
                    new_object = new_ball()
                    objects_on_screen[objects_on_screen.index(obj)] = new_object
                    break
            else:
                print('Missed')

    move_objects()
    objects_draw()
    pygame.display.update()
    screen.fill(BLACK)

print()
print('So,  you catch only ', counter, ' of my balls')

pygame.quit()
