import tkinter


window = tkinter.Tk()


def recordData():
    screenWidth = entryWidth.get()
    screenHeight = entryHeight.get()
    mazeWidth = mentryWidth.get()
    mazeHeight = mentryHeight.get()
    if screenHeight == '':
        screenHeight = 0
    if screenWidth == '':
        screenWidth = 0
    if mazeWidth == '':
        mazeWidth = 0
    if mazeHeight == '':
        mazeHeight = 0
    window.destroy()
    import maze
    maze.setupMaze(screenWidth,screenHeight,mazeWidth,mazeHeight)

window.title("GUI")
window.geometry("500x300")
label = tkinter.Label(window, text = "Width")
entryWidth = tkinter.Entry(width=50)
label2 = tkinter.Label(window, text = "Height")
entryHeight = tkinter.Entry(width=50)
mlabel = tkinter.Label(window, text = "Maze Width")
mentryWidth = tkinter.Entry(width=50)
mlabel2 = tkinter.Label(window, text = "Maze Height")
mentryHeight = tkinter.Entry(width=50)
button = tkinter.Button(
    text="Click me!",
    width = 25,
    height = 5,
    command = recordData
)
label.pack()
entryWidth.pack()
label2.pack()
entryHeight.pack()
mlabel.pack()
mentryWidth.pack()
mlabel2.pack()
mentryHeight.pack()
button.pack()
window.mainloop()
