import queue
import pens
import values
import time
import bestpath

def dfs(characterposition, treasureposition):
    best = bestpath.path(characterposition)
    movement = pens.Movement()
    dfsqueue = queue.LifoQueue()
    dfsqueue.put((characterposition,best))
    #print(insertLevelStr[(26 * int(y)) + int(x)], end=" ")
    def move(x,y,pbest):
        current = bestpath.path((x,y))
        current.nextval = pbest
        screen_x = ((values.screenWidth) / 2) + ((-1 * (values.screenWidth) - (24 * (values.mazeWidth))) / 2) + (x * 24)
        screen_y = (-1 * (values.screenHeight) / 2) + (((values.screenHeight) + (24 * (values.mazeHeight))) / 2) - (
                    y * 24)
        values.insertLevelStr[(26 * int(y)) + int(x)] = "M"
        movement.goto(screen_x, screen_y)
        movement.stamp()
        dfsqueue.put(((x, y),current))
        time.sleep(.2)
    while dfsqueue.qsize() != 0:
        ((x,y),pbest) = dfsqueue.get()
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
            move(x,y + 1,pbest)
        if values.insertLevelStr[(26 * int(y)) + int(x + 1)] == " ":
            move(x + 1,y,pbest)
        if values.insertLevelStr[(26 * int(y - 1)) + int(x)] == " ":
            move(x,y - 1,pbest)
        if values.insertLevelStr[(26 * int(y)) + int(x - 1)] == " ":
            move(x - 1,y,pbest)