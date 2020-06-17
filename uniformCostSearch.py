import queue
import pens
import values
import time
import math

def ucs(characterposition, treasureposition):
    movement = pens.Movement()
    ucsqueue = queue.PriorityQueue()
    ucsqueue.put(1,(1,(characterposition[0],characterposition[1])))
    #print(insertLevelStr[(26 * int(y)) + int(x)], end=" ")
    def move(pri,x,y):
        screen_x = ((values.screenWidth) / 2) + ((-1 * (values.screenWidth) - (24 * (values.mazeWidth))) / 2) + (x * 24)
        screen_y = (-1 * (values.screenHeight) / 2) + (((values.screenHeight) + (24 * (values.mazeHeight))) / 2) - (
                    y * 24)
        values.insertLevelStr[(26 * int(y)) + int(x)] = "M"
        movement.goto(screen_x, screen_y)
        movement.stamp()
        magx = (x + treasureposition[0])
        magy = (y + treasureposition[1])
        mag = (magx*magx) + (magy*magy)
        ucsqueue.put((pri+math.sqrt(mag)),((pri+math.sqrt(mag)),(x, y)))
        time.sleep(.2)
    while ucsqueue.qsize() != 0:
        pri,(x, y) = ucsqueue.get()
        print(x)
        print(y)
        print(pri)
        if values.insertLevelStr[(26 * int(y+1)) + int(x)] == "T":
            break
        if values.insertLevelStr[(26 * int(y)) + int(x + 1)] == "T":
            break
        if values.insertLevelStr[(26 * int(y - 1)) + int(x)] == "T":
            break
        if values.insertLevelStr[(26 * int(y)) + int(x - 1)] == "T":
            break
        if values.insertLevelStr[(26 * int(y+1)) + int(x)] == " ":
            move(pri,x,y + 1)
        if values.insertLevelStr[(26 * int(y)) + int(x + 1)] == " ":
            move(pri,x + 1,y)
        if values.insertLevelStr[(26 * int(y - 1)) + int(x)] == " ":
            move(pri,x,y - 1)
        if values.insertLevelStr[(26 * int(y)) + int(x - 1)] == " ":
            move(pri,x - 1,y)