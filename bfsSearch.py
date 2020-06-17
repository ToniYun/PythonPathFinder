import queue
import pens
import values
import time

def bfs(characterposition, treasureposition):
    movement = pens.Movement()
    bfsqueue = queue.Queue()
    bfsqueue.put(characterposition)
    #print(insertLevelStr[(26 * int(y)) + int(x)], end=" ")
    def move(x,y):
        screen_x = ((values.screenWidth) / 2) + ((-1 * (values.screenWidth) - (24 * (values.mazeWidth))) / 2) + (x * 24)
        screen_y = (-1 * (values.screenHeight) / 2) + (((values.screenHeight) + (24 * (values.mazeHeight))) / 2) - (
                    y * 24)
        values.insertLevelStr[(26 * int(y)) + int(x)] = "M"
        movement.goto(screen_x, screen_y)
        movement.stamp()
        bfsqueue.put((x, y))
        time.sleep(.2)
    while bfsqueue.qsize() != 0:
        x,y = bfsqueue.get()
        if values.insertLevelStr[(26 * int(y+1)) + int(x)] == " ":
            move(x,y + 1)
        if values.insertLevelStr[(26 * int(y)) + int(x + 1)] == " ":
            move(x + 1,y)
        if values.insertLevelStr[(26 * int(y - 1)) + int(x)] == " ":
            move(x,y - 1)
        if values.insertLevelStr[(26 * int(y)) + int(x - 1)] == " ":
            move(x - 1,y)