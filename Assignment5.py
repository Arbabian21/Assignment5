import tkinter as tk
import sys
from rectpack import newPacker
# the keyword 'self' refers to the instance of the class itself
# allows you to access instance variables and methods within class definitions
# when defining methods, 'self' must be the first parameter, even though it's implicitly passed by Python when calling methods

class CustomCanvas:
    def __init__(self, height: int, width: int):
        # constructor for the CustomCanvas class
        # creates a tkinter Canvas with input height and width
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
        # constructor for the Rectangle class
        # creates a rectangle with input height, width, x and y coordinates
        self.height = height
        self.width = width
        self.x = x
        self.y = y

def pack(allRect, canvasSize):
    # pack rectangles using the rectpack library to ensure the rectangles don't overlap within canvas
    packer = newPacker()

    # add rectangles to the packer
    for rect in allRect:
        packer.add_rect(rect.width, rect.height)

    # define the canvas as the bin for packing
    packer.add_bin(canvasSize[1], canvasSize[0])

    packer.pack()

    positions = packer.rect_list()
    packed_rectangles = []

    # create new rectangles based on packed positions
    for rect in positions:
        bin_index, x, y, w, h, rid = rect
        packed_rectangles.append(Rectangle(h, w, x, y))

    return packed_rectangles

def main():
    # read file path from terminal
    if len(sys.argv) < 2:
        print("Usage: python Assignment5.py <filepath>")
        return

    filepath = sys.argv[1]

    with open(filepath, 'r') as file:
        lines = file.readlines()

    # parse canvas size
    canvas_height, canvas_width = map(int, lines[0].strip().split(','))
    canvas_size = (canvas_height, canvas_width)

    # create rectangles from file data
    rectangles = []
    for line in lines[1:]:
        height, width = map(int, line.strip().split(','))
        rectangles.append(Rectangle(height, width))

    # pack rectangles
    packed_rectangles = pack(rectangles, canvas_size)

    # draw rectangles on the canvas
    custom_canvas = CustomCanvas(canvas_height, canvas_width)
    for rect in packed_rectangles:
        custom_canvas.draw_rectangle(rect)

    # display the canvas
    custom_canvas.display()

if __name__ == '__main__':
    main()
