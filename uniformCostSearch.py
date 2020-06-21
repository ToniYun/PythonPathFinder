import queue
import pens
import values
import time
import math
import bestpath

def ucs(characterposition, treasureposition):
    best = bestpath.path(characterposition)
    movement = pens.Movement()
    ucsqueue = queue.PriorityQueue()
    ucsqueue.put((1,(characterposition),best))
    #print(ucsqueue.get()[1])
    #print(insertLevelStr[(26 * int(y)) + int(x)], end=" ")
    def move(pri,x,y,pbest):
        current = bestpath.path((x,y))
        current.nextval = pbest
        screen_x = ((values.screenWidth) / 2) + ((-1 * (values.screenWidth) - (24 * (values.mazeWidth))) / 2) + (x * 24)
        screen_y = (-1 * (values.screenHeight) / 2) + (((values.screenHeight) + (24 * (values.mazeHeight))) / 2) - (
                    y * 24)
        values.insertLevelStr[(26 * int(y)) + int(x)] = "M"
        movement.goto(screen_x, screen_y)
        movement.stamp()
        magx = (x - treasureposition[0])
        magy = (y - treasureposition[1])
        mag = (magx*magx) + (magy*magy)
        ucsqueue.put(((pri+math.sqrt(mag)),(x, y),current))
        time.sleep(.2)
    while ucsqueue.qsize() != 0:
        (pri,(x, y),pbest) = ucsqueue.get()
        if values.insertLevelStr[(26 * int(y+1)) + int(x)] == "T":
            bestpath.follow(pbest)
            break
        if values.insertLevelStr[(26 * int(y)) + int(x + 1)] == "T":
            bestpath.follow(pbest)
            break
        if values.insertLevelStr[(26 * int(y - 1)) + int(x)] == "T":
            bestpath.follow(pbest)
            break
        if values.insertLevelStr[(26 * int(y)) + int(x - 1)] == "T":
            bestpath.follow(pbest)
            break
        if values.insertLevelStr[(26 * int(y+1)) + int(x)] == " ":
            move(pri,x,y + 1,pbest)
        if values.insertLevelStr[(26 * int(y)) + int(x + 1)] == " ":
            move(pri,x + 1,y,pbest)
        if values.insertLevelStr[(26 * int(y - 1)) + int(x)] == " ":
            move(pri,x,y - 1,pbest)
        if values.insertLevelStr[(26 * int(y)) + int(x - 1)] == " ":
            move(pri,x - 1,y,pbest)