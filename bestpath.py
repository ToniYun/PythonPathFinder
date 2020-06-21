import pens
import values
class path:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

def follow(path):
    penpath = pens.best()
    while path.nextval != None:
        screen_x = ((values.screenWidth) / 2) + ((-1 * (values.screenWidth) - (24 * (values.mazeWidth))) / 2) + (path.dataval[0] * 24)
        screen_y = (-1 * (values.screenHeight) / 2) + (((values.screenHeight) + (24 * (values.mazeHeight))) / 2) - (path.dataval[1] * 24)
        penpath.goto(screen_x, screen_y)
        penpath.stamp()
        path = path.nextval