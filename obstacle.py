import pygame as pg

spike = pg.image.load("spike.png")
block = pg.image.load("block.png")


def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect.topleft)


def simple_spike(ROOT, obstacle_x, side="DOWN"):
    if side == "UP":
        obstacle_y = 200
        tilt = 180
    else:
        obstacle_y = 430
        tilt = 0
    blitRotateCenter(ROOT, spike, (obstacle_x, obstacle_y), tilt)
    return obstacle_x


def big_spike(ROOT, obstacle_x, side="DOWN"):
    if side == "UP":
        obstacle_y = 200
        tilt = 180
        for i in range(1, 4):
            ROOT.blit(block, (obstacle_x, obstacle_y))
            obstacle_y += 20
        blitRotateCenter(ROOT, spike, (obstacle_x, obstacle_y), tilt)
    else:
        obstacle_y = 430
        tilt = 0
        for i in range(1, 4):
            ROOT.blit(block, (obstacle_x, obstacle_y))
            obstacle_y -= 20
        blitRotateCenter(ROOT, spike, (obstacle_x, obstacle_y), tilt)
    return obstacle_x
