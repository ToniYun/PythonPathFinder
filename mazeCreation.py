import tkinter




def mazeDraw(screenWidth,screenHeight,mazeWidth,mazeHeight):
    insertLevel = ""
    def sendToMaze():
        import maze
        maze.setupMaze(screenWidth, screenHeight, mazeWidth, mazeHeight, insertLevel)
    newWindow = tkinter.Tk()
    newWindow.title("GUI")
    height = mazeHeight * 24
    width = mazeWidth * 24
    newWindow.geometry(str(height) + "x" + str(width))
    for x in range(0, int(25)):#mazeWidth)):
        for y in range(0, int(25)):#mazeHeight)):
            insertLevel += "X"
        insertLevel += "\n"
    TextIn = tkinter.Text(newWindow)
    button = tkinter.Button(
        text="Set Maze",
        width = 25,
        height = 3,
        command = sendToMaze
    )
    TextIn.pack()
    TextIn.insert(tkinter.END,insertLevel)
    button.pack()
    newWindow.mainloop()