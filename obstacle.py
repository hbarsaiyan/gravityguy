import pygame as pg
import random as rand

obstacle_list = [pg.image.load("spike_s.png"), pg.image.load("spike_l.png"),
                 pg.image.load("spike_xl.png"), pg.image.load("spike_double.png")]

r = 0

def ob_yco(rand):
    if rand[0] == 0:  # render obstacle
        if rand[1] == 0:
            ob_y = 390
        else:
            ob_y = 200
    elif rand[0] == 1:
        if rand[1] == 0:
            ob_y = 350
        else:
            ob_y = 200
    elif rand[0] == 2:
        if rand[1] == 0:
            ob_y = 310
        else:
            ob_y = 200
    elif rand[0] == 3:
        if rand[1] == 0:
            ob_y = 200
        else:
            ob_y = 200
    return ob_y


def neat_yco(rand):
    if rand[0] == 0:  # render obstacle
        if rand[1] == 0:
            ob_y = 390
        else:
            ob_y = 260
    elif rand[0] == 1:
        if rand[1] == 0:
            ob_y = 350
        else:
            ob_y = 300
    elif rand[0] == 2:
        if rand[1] == 0:
            ob_y = 310
        else:
            ob_y = 340
    elif rand[0] == 3:
        if rand[1] == 0:
            ob_y = 200
        else:
            ob_y = 200
    return ob_y


def random(ran=(0, 0)):
    global r
    '''
    Comment line below to enable randomness
    '''
    rand.seed(100 + r)
    r += 1
    if ran[0] > 2:
        obstacle_no = rand.randrange(0, 2)
    else:
        obstacle_no = rand.randrange(0, 3)
    obstacle_side = rand.randrange(0, 2)
    return obstacle_no, obstacle_side

def reset_r():
    global r
    r = 0


def get_ob_mask(rand, no):
    if rand[1] == 0:
        if no == 1:
            ob_mask = pg.mask.from_surface(obstacle_list[rand[0]])
        elif no == 2:
            ob_mask = pg.mask.from_surface(obstacle_list[rand[0]])
        elif no == 3:
            ob_mask = pg.mask.from_surface(obstacle_list[rand[0]])
        elif no == 4:
            ob_mask = pg.mask.from_surface(obstacle_list[rand[0]])
        return ob_mask
    if rand[1] == 1:
        rotated_image = pg.transform.rotate(obstacle_list[rand[0]], 180)
        if no == 1:
            ob_mask = pg.mask.from_surface(rotated_image)
        elif no == 2:
            ob_mask = pg.mask.from_surface(rotated_image)
        elif no == 3:
            ob_mask = pg.mask.from_surface(rotated_image)
        elif no == 4:
            ob_mask = pg.mask.from_surface(rotated_image)
        return ob_mask


def rand_obstacle(ROOT, obstacle_x, rand):
    if rand[1] == 0:  # obstacle side
        tilt = 0
    else:
        tilt = 180

    # render obstacle

    ob_y = ob_yco(rand)
    blitRotateCenter(ROOT, obstacle_list[rand[0]], (obstacle_x, ob_y), tilt)
    return obstacle_x


def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect.topleft)


''' s
def simple_spike(ROOT, obstacle_x, side="DOWN"):  # 1
    if side == "UP":
        obstacle_y = 200
        tilt = 180
        blitRotateCenter(ROOT, spike, (obstacle_x, obstacle_y + 20), tilt)
    else:
        obstacle_y = 430
        tilt = 0
        blitRotateCenter(ROOT, spike, (obstacle_x, obstacle_y - 20), tilt)
    blitRotateCenter(ROOT, spike, (obstacle_x - 20, obstacle_y), 90)
    ROOT.blit(block, (obstacle_x, obstacle_y))
    blitRotateCenter(ROOT, spike, (obstacle_x + 20, obstacle_y), 270)

    #spikes.append((obstacle_x, obstacle_y))
    return obstacle_x


def big_spike(ROOT, obstacle_x, side="DOWN"):  # 2
    if side == "UP":
        obstacle_y = 200
        tilt = 180
        for i in range(1, 5):  # block
            blitRotateCenter(ROOT, spike, (obstacle_x - 20, obstacle_y), 90)
            ROOT.blit(block, (obstacle_x, obstacle_y))
            blitRotateCenter(ROOT, spike, (obstacle_x + 20, obstacle_y), 270)
            obstacle_y += 20
        blitRotateCenter(ROOT, spike, (obstacle_x, obstacle_y), tilt)  # spike
    else:
        obstacle_y = 430
        tilt = 0
        for i in range(1, 5):  # block
            blitRotateCenter(ROOT, spike, (obstacle_x - 20, obstacle_y), 90)
            ROOT.blit(block, (obstacle_x, obstacle_y))
            blitRotateCenter(ROOT, spike, (obstacle_x + 20, obstacle_y), 270)
            obstacle_y -= 20
        blitRotateCenter(ROOT, spike, (obstacle_x, obstacle_y), tilt)  # spike
    return obstacle_x
'''
