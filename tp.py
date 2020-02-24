import mcpi.minecraft as mcc
import mcpi.vec3 as vec
import mcpi.block as blo

mc = mcc.Minecraft.create()
while True:
    if mc.getBlock(mc.player.getTilePos()+vec.Vec3(0,-1,0)) == blo.TNT.id:
        mc.player.setTilePos(-459,81,277)

