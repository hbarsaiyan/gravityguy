import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (100, 100, 255)

restart = True
vel = 0.5
FPS = 60
i = 0

bg = pg.image.load("bg.png")
char = [[pg.image.load("char_0.png"), pg.image.load("char_01.png")], [pg.image.load("char_1.png"), pg.image.load("char_11.png")]]


class Player:
    def __init__(self):
        self.y_co = 410
        self.vel = 0
        self.i = 0
        self.j = 0

    def change_gravity(self):
        if self.y_co == 200:
            self.vel = 10
            self.i = 0
        elif self.y_co == 410:
            self.vel = -10
            self.i = 1

    def render(self):
        # pg.draw.rect(ROOT, RED, (100, self.y_co, 40, 40))
        ROOT.blit(char[self.i][self.j], (100, self.y_co))
        if self.j == 0:
            self.j = 1
        else:
            self.j = 0

    def move(self):
        self.y_co += self.vel


ROOT = pg.display.set_mode((800, 600))


def main_loop():
    global restart
    p1 = Player()
    clock = pg.time.Clock()

    OVER = False
    while not OVER:
        # Event Loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                OVER = True
                restart = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    p1.change_gravity()

        # Logic Section

        p1.move()

        if p1.y_co == 200 or p1.y_co == 410:
            p1.vel = 0

        # Rendering Section
        ROOT.fill(WHITE)
        # pg.draw.rect(ROOT, WHITE, (0, 0, 800, 350))
        # pg.draw.rect(ROOT, WHITE, (0, 350, 800, 250))

        # pg.draw.rect(ROOT, BLACK, (0, 180, 800, 20))
        pg.draw.rect(ROOT, BLACK, (0, 0, 800, 200))
        pg.draw.rect(ROOT, BLACK, (0, 450, 800, 200))
        ROOT.blit(bg, (0, 180))
        p1.render()
        # pg.time.delay(15)
        clock.tick(FPS)
        pg.display.update()


while True:
    if restart:
        main_loop()
    else:
        break
pg.quit()
quit()
