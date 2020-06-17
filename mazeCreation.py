import tkinter
import values

def mazeDraw():
    def sendToMaze():
        values.insertLevelStr = list(TextIn.get("1.0",'end-1c'))
        newWindow.destroy()
        import maze
        maze.setupMaze()

    newWindow = tkinter.Tk()
    newWindow.title("GUI")
    height = values.mazeHeight * 24
    width = values.mazeWidth * 24
    newWindow.geometry(str(height) + "x" + str(width))
    insertLevel = ""
    for x in range(0, values.mazeWidth):
        for y in range(0, values.mazeWidth):
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