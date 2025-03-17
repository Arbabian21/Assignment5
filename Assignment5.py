import tkinter as tk

class CustomCanvas:
    def __init__(self, height: int, width: int):
        # constructor for the CustomCanvas class.
        # creates a tkinter Canvas with input height and width.
        
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=height, width=width)
        self.canvas.pack()

    def draw_rectangle(self, rectangle, outline_color="black", fill_color="blue"):
        # draw a rectangle on the canvas
        x1, y1 = rectangle.x, rectangle.y
        x2, y2 = rectangle.x + rectangle.width, rectangle.y + rectangle.height
        self.canvas.create_rectangle(x1, y1, x2, y2, outline=outline_color, fill=fill_color)
        
    def display(self):
        # display the tkinter window with the drawn rectangles
        self.root.mainloop()

class Rectangle:
    def __init__(self, height, width, x=0, y=0):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
