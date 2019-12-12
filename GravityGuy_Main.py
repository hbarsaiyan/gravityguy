import pygame as pg
import obstacle as ob

# Program Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (100, 100, 255)
char = [[pg.image.load("char_0.png"), pg.image.load("char_01.png")],
        [pg.image.load("char_1.png"), pg.image.load("char_11.png")]]
spike = pg.image.load("spike.png")
bg = pg.image.load("bg.png")
bg_block = pg.image.load("bgblock1.png")
display_width, display_height = 800, 600
block_thickness = 40
char_VEL = 15

restart = True
FPS = 30 #if u want to change this u have to change values in Player.render too
i = 0


class Player:
    def __init__(self):
        self.y_co = display_height/3 + 250 - block_thickness
        self.vel = 0
        self.i = 0
        self.j = 0

    def change_gravity(self):
        if self.y_co == display_height / 3:
            self.vel = char_VEL
            self.i = 0
        elif self.y_co == display_height/3 + 250 - block_thickness:
            self.vel = -char_VEL
            self.i = 1

    def render(self):
        ROOT.blit(char[self.i][self.j], (100, self.y_co))
        if char_walk_index in range(0, 5) or char_walk_index in range(10, 15) or char_walk_index in range(20, 25):
            self.j = 1
        else:
            self.j = 0

    def move(self):
        self.y_co += self.vel


ROOT = pg.display.set_mode((display_width, display_height))


def main_loop():
    # Game Loop Variables
    global restart, char_walk_index
    p1 = Player()
    clock = pg.time.Clock()
    BG_VEL = 4
    obstacle_x = 800
    obstacle_x1 = 780
    bg_X, char_walk_index = 0, 0

    # Game Loop
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
        if p1.y_co == display_height / 3 or p1.y_co == display_height/3 + 250 - block_thickness:
            p1.vel = 0

        # Rendering Section
        ROOT.fill((13, 13, 13))
        pg.draw.rect(ROOT, BLACK, (0, 0, display_width, display_height/3))
        pg.draw.rect(ROOT, BLACK, (0, display_height/3 + 250, display_width, display_height/3))

        if bg_X >= -20:  # Background Render + animation
            ROOT.blit(bg_block, (bg_X, display_height/3 - 20))
            bg_X -= BG_VEL
            #ob.simple_spike()
        else:
            ROOT.blit(bg_block, (bg_X, display_height/3 - 20))
            bg_X = 0

        ROOT.blit(bg, (0, display_height / 3 - 20))
        p1.render()  # Player Render
        obstacle_x = ob.big_spike(ROOT, obstacle_x )
        obstacle_x -= BG_VEL

        clock.tick_busy_loop(FPS)
        pg.display.update()

        char_walk_index += 1  # animating Player
        if char_walk_index == FPS:
            char_walk_index = 0


while True:
    if restart:
        main_loop()
    else:
        break
pg.quit()
quit()
