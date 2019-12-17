import pygame as pg
import random as rand

obstacle_list = [pg.image.load("spike_s.png"), pg.image.load("spike_l.png")]


def random():
    obstacle_no = rand.randrange(0, 2)
    obstacle_side = rand.randrange(0, 2)
    return obstacle_no, obstacle_side


def rand_obstacle(ROOT, obstacle_x, rand):
    if rand[1] == 0:
        tilt = 0
    else:
        tilt = 180
        ob_y = 200
    if rand[0] == 0:
        if rand[1] == 0:
            ob_y = 390
        blitRotateCenter(ROOT, obstacle_list[rand[0]], (obstacle_x, ob_y), tilt)
    if rand[0] == 1:
        if rand[1] == 0:
            ob_y = 350
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
