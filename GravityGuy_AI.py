import pygame as pg
import obstacle as ob
import neat
import os
import pickle

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
GEN = -1
NOJ = 10
HIGH_SCORE = 0

try:
    with open('high_score_AI.pickle', 'rb') as f:
        HIGH_SCORE = pickle.load(f)
except (OSError, IOError) as e:
    HIGH_SCORE = 0

restart = True
FPS = 60  # if u want to change this u have to change values in Player.render too
i = 0


def blit_msg(txt, color, size, pos):
    FONT = pg.font.Font("freesansbold.ttf", size)
    text = FONT.render(txt, True, color)
    ROOT.blit(text, (pos[0], pos[1]))


def give_block_dist(rand):
    if rand[0] == 2:
        block_spawn_dist = 1000
    else:
        block_spawn_dist = 1000
    return block_spawn_dist


class Player:  # Rambo
    def __init__(self, x):
        self.x_co = x
        self.y_co = display_height / 3 + 250 - block_thickness
        self.vel = 0
        self.i = 0
        self.j = 0
        self.side = 0
        self.char_mask = None
        self.hit = False
        self.off1 = 0
        self.off2 = 0
        self.off3 = 0
        self.off4 = 0
        self.NOJ = NOJ

    def change_gravity(self):
        if self.NOJ > 0:
            if self.y_co == display_height / 3:
                self.vel = char_VEL
                self.i = 0
            elif self.y_co == display_height / 3 + 250 - block_thickness:
                self.vel = -char_VEL
                self.i = 1
            self.NOJ -= 0.5
        else:
            self.hit = True

    def render(self):
        ROOT.blit(char[self.i][self.j], (self.x_co, self.y_co))
        self.char_mask = pg.mask.from_surface(char[self.i][self.j])
        if char_walk_index in range(0, 5) or char_walk_index in range(10, 15) or char_walk_index in range(20, 25):
            self.j = 1
        else:
            self.j = 0

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


def main_loop(genomes, config):
    # Game Loop Variables
    global GEN, NOJ, HIGH_SCORE
    GEN += 1
    NOJ += GEN//10
    global restart, char_walk_index, OVER
    nets = []
    ge = []
    Players = []

    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        Players.append(Player(162))
        ge.append(genome)

    for x, p1 in enumerate(Players):
        ge[x].fitness = 0

    # p1 = Player()

    clock = pg.time.Clock()
    BG_VEL = 20
    bg_X, char_walk_index = 0, 0
    Score = 0

    # obstacle Part
    obstacle_x1 = 1000
    obstacle_x2 = 1250
    obstacle_x3 = 1500
    obstacle_x4 = 1750
    a_obs_x = [obstacle_x1, obstacle_x2, obstacle_x3, obstacle_x4]
    rand1 = ob.random()
    rand2 = ob.random()
    rand3 = ob.random()
    rand4 = ob.random()
    aran = [rand1, rand2, rand3, rand4]
    # Game Loop
    OVER = False
    while not OVER:
        # Event Loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        if len(Players) == 0:
            OVER = True

        # Logic Section ***************************************************************
        for x, p1 in enumerate(Players):
            p1.move()
            if p1.y_co == display_height / 3 or p1.y_co == display_height / 3 + 250 - block_thickness:
                p1.vel = 0
                if p1.y_co == display_height / 3:
                    p1.side = 1
                if p1.y_co == display_height / 3 + 250 - block_thickness:
                    p1.side = 0

                for ran in aran:
                    if ran[1] == p1.side and a_obs_x[aran.index(ran)] > 200 :
                        fran = ran
                        obs_x = a_obs_x[aran.index(ran)]
                        break
                    else:
                        fran = (0, abs(p1.side - 1))
                        obs_x = 800

            output = nets[x].activate((p1.side, fran[1], abs(obs_x - p1.y_co)))
            # (p1.side, rand1[1], rand2[1], rand3[1], rand4[1], abs(p1.y_co - obstacle_x1),
            #                                        abs(p1.y_co - obstacle_x2),
            #                                        abs(p1.y_co - obstacle_x3), abs(p1.y_co - obstacle_x4))
            if output[0] > 0.5:
                p1.change_gravity()
                # if 0 < abs(obs_x - p1.y_co) < 90:
                #     ge[x].fitness += 2
        # Rendering Section
        ROOT.fill(BLACK)
        pg.draw.rect(ROOT, BLACK, (0, 0, display_width, display_height / 3))
        pg.draw.rect(ROOT, BLACK, (0, display_height / 3 + 250, display_width, display_height / 3))
        blit_msg("Score : " + str(Score), WHITE, 32, (0, 0))
        blit_msg("GEN : " + str(GEN), WHITE, 32, (0, 35))
        blit_msg("Alive : " + str(len(Players)), WHITE, 32, (0, 70))
        blit_msg("High Score : " + str(HIGH_SCORE), WHITE, 32, (550, 0))
        if bg_X >= -20:  # Background Render + animation
            ROOT.blit(bg_block, (bg_X, display_height / 3 - 20))
            bg_X -= 0

        else:
            ROOT.blit(bg_block, (bg_X, display_height / 3 - 20))
            bg_X = 0

        ROOT.blit(bg, (0, display_height / 3 - 20))

        obstacle_x1 = ob.rand_obstacle(ROOT, obstacle_x1, rand1)  # Obstacle Motion + Render
        obstacle_x2 = ob.rand_obstacle(ROOT, obstacle_x2, rand2)
        obstacle_x3 = ob.rand_obstacle(ROOT, obstacle_x3, rand3)
        obstacle_x4 = ob.rand_obstacle(ROOT, obstacle_x4, rand4)
        obstacle_x1 -= BG_VEL
        obstacle_x2 -= BG_VEL
        obstacle_x3 -= BG_VEL
        obstacle_x4 -= BG_VEL

        # collision DETECTION
        for x, p1 in enumerate(Players):
            # if p1.y_co == 200 or p1.y_co == 410:
            #     ge[x].fitness += 0.01

            p1.off1 = (round(obstacle_x1 - p1.x_co), round(ob.ob_yco(rand1) - p1.y_co))
            p1.off2 = (round(obstacle_x2 - p1.x_co), round(ob.ob_yco(rand2) - p1.y_co))
            p1.off3 = (round(obstacle_x3 - p1.x_co), round(ob.ob_yco(rand3) - p1.y_co))
            p1.off4 = (round(obstacle_x4 - p1.x_co), round(ob.ob_yco(rand4) - p1.y_co))
            p1.render()  # Player Render
            if not p1.hit:
                mask = ob.get_ob_mask(rand1, 1)
                p1.hit = p1.char_mask.overlap(mask, p1.off1)
            if not p1.hit:
                p1.hit = p1.char_mask.overlap(ob.get_ob_mask(rand2, 2), p1.off2)
            if not p1.hit:
                p1.hit = p1.char_mask.overlap(ob.get_ob_mask(rand3, 3), p1.off3)
            if not p1.hit:
                p1.hit = p1.char_mask.overlap(ob.get_ob_mask(rand4, 4), p1.off4)

            if p1.hit:
                ge[x].fitness -= 10
                Players.pop(x)
                nets.pop(x)
                ge.pop(x)

        '''if not OVER:
            OVER = collide(p1, rand1, obstacle_x)
        if not OVER:
            OVER = collide(p1, rand2, obstacle_x1)
        if not OVER:
            OVER = collide(p1, rand3, obstacle_x2)
        if not OVER:
            OVER = collide(p1, rand4, obstacle_x3)'''
        '''if obstacle_x1 < 200:
            obs_x = obstacle_x2
            fran = rand2
        if obstacle_x2 < 200:
            obs_x = obstacle_x3
            fran = rand3
        if obstacle_x2 < 200:
            obs_x = obstacle_x4
            fran = rand4
        if obstacle_x4 < 200:
            obs_x = obstacle_x1
            fran = rand4'''

        if obstacle_x1 < -30:  # obstacle DESTROYER!!!
            obstacle_x1 = give_block_dist(rand4)
            rand1 = ob.random(ran=rand4)
            Score += 1
            for g in ge:
                g.fitness += 1
        if obstacle_x2 < -30:
            obstacle_x2 = give_block_dist(rand1)
            rand2 = ob.random(ran=rand1)
            Score += 1
            for g in ge:
                g.fitness += 1
        if obstacle_x3 < -30:
            obstacle_x3 = give_block_dist(rand2)
            rand3 = ob.random(ran=rand2)
            Score += 1
            for g in ge:
                g.fitness += 1
        if obstacle_x4 < -30:
            obstacle_x4 = give_block_dist(rand3)
            rand4 = ob.random(ran=rand3)
            Score += 1
            for g in ge:
                g.fitness += 1
        if Score > HIGH_SCORE:
            HIGH_SCORE = Score
            with open('high_score_AI.pickle', 'wb') as f:
                pickle.dump(Score, f)
        aran = [rand1, rand2, rand3, rand4]
        a_obs_x = [obstacle_x1, obstacle_x2, obstacle_x3, obstacle_x4]

        clock.tick_busy_loop(FPS)
        pg.display.update()

        char_walk_index += 1  # animating Player
        if char_walk_index == FPS:
            char_walk_index = 0


'''
while True:
    if restart:
        main_loop()
    else:
        break
pg.quit()
quit()
'''


def run(config_file):
    """
    runs the NEAT algorithm to train a neural network to play flappy bird.
    :param config_file: location of config file
    :return: None
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    winner = p.run(main_loop, 500)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'neat-config.txt')
    run(config_path)
