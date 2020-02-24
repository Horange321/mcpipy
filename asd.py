import mcpi.minecraft as mcc
import mcpi.block as block
mc = mcc.Minecraft.create()
mc.setBlock(mc.player.getTilePos(), block.GLASS)
