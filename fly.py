from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import mcpi.block as block
import time

directions = (
    (0, 0, 0),
    (1, 0, 0),
    (1, 0, 1),
    (0, 0, 1),
    (-1, 0, 1),
    (-1, 0, 0),
    (-1, 0, -1),
    (0, 0, -1),
    (1, 0, -1),
    (2,0,-1),
    (2,0,0),
    (2,0,1),
    (2,0,2),
    (1,0,2),
    (0,0,2),
    (-1,0,2),
    (-2,0,2),
    (-2,0,1),
    (-2,0,0),
    (-2,0,-1),
    (-2,0,-2),
    (-1,0,-2),
    (0,0,-2),
    (1,0,-2),
    (2,0,-2)
)

mc = Minecraft.create()
cbps = []

while True:
    position = mc.player.getTilePos() + Vec3(0, -1, 0)
    new_pos = []
    for direction in directions:
        new_po = position+Vec3(*direction)
        new_pos.append(new_po)
        byi = mc.getBlock(new_po)
        if byi == block.AIR.id:
            mc.setBlock(new_po, block.GLASS)
            cbps.append(new_po)

    for cbp in cbps:
        if cbp not in new_pos:
            mc.setBlock(cbp, block.AIR)

    time.sleep(0.016)
