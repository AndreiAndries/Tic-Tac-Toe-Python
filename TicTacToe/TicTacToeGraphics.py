import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


def draw_circle(circle):
    circle_radius = 75
    border_width = 10
    pygame.draw.circle(screen, BLUE, circle, circle_radius, border_width)


def draw_X(x, y):
    if x == 0 and y == 0:
        pygame.draw.line(screen, RED, (150, 40), (280, 180), 20)
        pygame.draw.line(screen, RED, (280, 40), (150, 180), 20)
    elif x == 0 and y == 1:
        pygame.draw.line(screen, RED, (340, 40), (470, 180), 20)
        pygame.draw.line(screen, RED, (470, 40), (340, 180), 20)
    elif x == 0 and y == 2:
        pygame.draw.line(screen, RED, (530, 40), (660, 180), 20)
        pygame.draw.line(screen, RED, (660, 40), (530, 180), 20)
    elif x == 1 and y == 0:
        pygame.draw.line(screen, RED, (150, 230), (280, 370), 20)
        pygame.draw.line(screen, RED, (280, 230), (150, 370), 20)
    elif x == 1 and y == 1:
        pygame.draw.line(screen, RED, (340, 230), (470, 370), 20)
        pygame.draw.line(screen, RED, (470, 230), (340, 370), 20)
    elif x == 1 and y == 2:
        pygame.draw.line(screen, RED, (530, 230), (660, 370), 20)
        pygame.draw.line(screen, RED, (660, 230), (530, 370), 20)
    elif x == 2 and y == 0:
        pygame.draw.line(screen, RED, (150, 420), (280, 560), 20)
        pygame.draw.line(screen, RED, (280, 420), (150, 560), 20)
    elif x == 2 and y == 1:
        pygame.draw.line(screen, RED, (340, 420), (470, 560), 20)
        pygame.draw.line(screen, RED, (470, 420), (340, 560), 20)
    elif x == 2 and y == 2:
        pygame.draw.line(screen, RED, (530, 420), (660, 560), 20)
        pygame.draw.line(screen, RED, (660, 420), (530, 560), 20)


def draw_O(x, y):
    if x == 0 and y == 0:
        circle = (200, 100)
        draw_circle(circle)
    elif x == 0 and y == 1:
        circle = (410, 100)
        draw_circle(circle)
    elif x == 0 and y == 2:
        circle = (600, 100)
        draw_circle(circle)
    elif x == 1 and y == 0:
        circle = (200, 300)
        draw_circle(circle)
    elif x == 1 and y == 1:
        circle = (410, 300)
        draw_circle(circle)
    elif x == 1 and y == 2:
        circle = (600, 300)
        draw_circle(circle)
    elif x == 2 and y == 0:
        circle = (200, 500)
        draw_circle(circle)
    elif x == 2 and y == 1:
        circle = (410, 500)
        draw_circle(circle)
    elif x == 2 and y == 2:
        circle = (600, 500)
        draw_circle(circle)


def start():
    running = True
    icon = pygame.image.load('Res/TicTacTocLogo.png')
    pygame.display.set_caption("Tic Tac Toe")
    pygame.display.set_icon(icon)
    screen.fill(WHITE)
    pygame.display.update()
    pygame.draw.rect(screen, BLACK, pygame.Rect(300, 20, 10, 560))
    pygame.draw.rect(screen, BLACK, pygame.Rect(500, 20, 10, 560))
    pygame.draw.rect(screen, BLACK, pygame.Rect(130, 200, 560, 10))
    pygame.draw.rect(screen, BLACK, pygame.Rect(130, 400, 560, 10))
    draw_X(0, 0)
    draw_X(0, 1)
    draw_X(0, 2)
    draw_X(1, 0)
    draw_X(1, 1)
    draw_X(1, 2)
    draw_X(2, 0)
    draw_X(2, 1)
    draw_X(2, 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


start()
