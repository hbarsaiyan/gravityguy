import pygame as pg
import obstacle as ob

pg.init()
# Program Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (100, 100, 255)
char = [[pg.image.load("char_0.png"), pg.image.load("char_01.png")],
        [pg.image.load("char_1.png"), pg.image.load("char_11.png")]]
bg = pg.image.load("bg.png")
bg_block = pg.image.load("bgblock1.png")
display_width, display_height = 800, 600
block_thickness = 40
char_VEL = 21

restart = True
FPS = 30  # if u want to change this u have to change values in Player.render too
i = 0


class Player:  # Rambo
    def __init__(self):
        self.x_co = 162
        self.y_co = display_height / 3 + 250 - block_thickness
        self.vel = 0
        self.i = 0
        self.j = 0
        self.hitbox = (self.x_co + 16, self.y_co, 22, 37)

    def change_gravity(self):
        if self.y_co == display_height / 3:
            self.vel = char_VEL
            self.i = 0
        elif self.y_co == display_height / 3 + 250 - block_thickness:
            self.vel = -char_VEL
            self.i = 1

    def render(self):
        global char_mask
        ROOT.blit(char[self.i][self.j], (self.x_co, self.y_co))
        char_mask = pg.mask.from_surface(char[self.i][self.j])
        if char_walk_index in range(0, 5) or char_walk_index in range(10, 15) or char_walk_index in range(20, 25):
            self.j = 1
        else:
            self.j = 0
        self.hitbox = (self.x_co + 16, self.y_co + 3, 22, 37)

    def move(self):
        self.y_co += self.vel

    '''def get_mask(self):
        """
        gets the mask for the current image of the player
        """
        return pg.mask.from_surface(char[self.i][self.j])'''

'''
def collide(p1, rand, obstacle_x):
    if obstacle_x == 180 or obstacle_x == 220:
        if rand[0] == 1:  # 1
            if rand[1] == 1:  # UP
                ob_y_co = 200
                if ob_y_co <= p1.hitbox[1] <= ob_y_co + 10:
                    print("HIT1")
                    return True
            else:  # DOWN
                ob_y_co = 450
                if ob_y_co - 10 <= p1.y_co + 40 <= ob_y_co:
                    print("HIT2")
                    return True
    if obstacle_x == 200:
        if rand[0] == 1:  # 1
            if rand[1] == 1:  # UP
                ob_y_co = 200
                if ob_y_co <= p1.hitbox[1] <= ob_y_co + 40:
                    print("HIT3")
                    return True
            else:  # DOWN
                ob_y_co = 450
                if ob_y_co - 40 <= p1.y_co + 40 <= ob_y_co:
                    print("HIT4")
                    return True
    else:
        return False
'''


ROOT = pg.display.set_mode((display_width, display_height))


def main_loop():
    # Game Loop Variables
    global restart, char_walk_index, OVER
    p1 = Player()
    clock = pg.time.Clock()
    BG_VEL = 10
    bg_X, char_walk_index = 0, 0
    # obstacle Part

    obstacle_x = 800
    obstacle_x1 = 1000
    obstacle_x2 = 1200
    obstacle_x3 = 1400
    rand1 = ob.random()
    rand2 = ob.random()
    rand3 = ob.random()
    rand4 = ob.random()
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
        if p1.y_co == display_height / 3 or p1.y_co == display_height / 3 + 250 - block_thickness:
            p1.vel = 0

        # Rendering Section
        ROOT.fill((13, 13, 13))
        pg.draw.rect(ROOT, BLACK, (0, 0, display_width, display_height / 3))
        pg.draw.rect(ROOT, BLACK, (0, display_height / 3 + 250, display_width, display_height / 3))

        if bg_X >= -20:  # Background Render + animation
            ROOT.blit(bg_block, (bg_X, display_height / 3 - 20))
            bg_X -= BG_VEL

        else:
            ROOT.blit(bg_block, (bg_X, display_height / 3 - 20))
            bg_X = 0

        ROOT.blit(bg, (0, display_height / 3 - 20))
        p1.render()  # Player Render
        obstacle_x = ob.rand_obstacle(ROOT, obstacle_x, rand1)
        obstacle_x1 = ob.rand_obstacle(ROOT, obstacle_x1, rand2)
        obstacle_x2 = ob.rand_obstacle(ROOT, obstacle_x2, rand3)
        obstacle_x3 = ob.rand_obstacle(ROOT, obstacle_x3, rand4)
        obstacle_x -= BG_VEL
        obstacle_x1 -= BG_VEL
        obstacle_x2 -= BG_VEL
        obstacle_x3 -= BG_VEL
        '''if not OVER:
            OVER = collide(p1, rand1, obstacle_x)
        if not OVER:
            OVER = collide(p1, rand2, obstacle_x1)
        if not OVER:
            OVER = collide(p1, rand3, obstacle_x2)
        if not OVER:
            OVER = collide(p1, rand4, obstacle_x3)'''

        if obstacle_x < 0:
            obstacle_x = 800
            rand1 = ob.random()
        if obstacle_x1 < 0:
            obstacle_x1 = 800
            rand2 = ob.random()
        if obstacle_x2 < 0:
            obstacle_x2 = 800
            rand3 = ob.random()
        if obstacle_x3 < 0:
            obstacle_x3 = 800
            rand4 = ob.random()

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
