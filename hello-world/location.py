from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = mc.player.getPos()

mc.postToChat('X Pos = ' + str(x))
mc.postToChat('Y Pos = ' + str(y))
mc.postToChat('Z Pos = ' + str(z))
