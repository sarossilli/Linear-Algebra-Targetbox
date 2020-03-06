# Sam Rossilli
# CS 2300:001
# Assigment 2
# Due 3/06/20
# 1. Reads in 5 lines from the file
# 2. Initializes a line object which hs a vector, 2 points,corner of target box, size of target box, and an implicit form 
#        An implicit form object has a vector (normal to the line) and the a 'c' value to hold the calculated c part of the equation 
# 4. Plots each line and prints the implicit line in the window


from tkinter import font
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None, name=None):
        super().__init__(master)
        self.master = master
        self.winfo_toplevel().title(name) #Set name of window to file
        self.pack()

class Implicit():
    def __init__(self, vector, point):
        # Vector is normal to the line vector
        self.vector = [-vector[1], vector[0]]
        self.cVal = (
            -(self.vector[0]) * point[0]) - ((self.vector[1]) * point[1])

    def eqString(self):
        return str(self.vector[0]) + "x₁ + " + str(self.vector[1]) + "x₂ + " + str(self.cVal) + " = 0"

class Line():
    def __init__(self, file):
        # Get all inputs and assign them to the correct variables
        inputs = self.read(file)
        self.local_origin = inputs[0:2]
        self.size = inputs[2]
        self.vector = inputs[5:7]
        
        
        # Point1 is the given point in the line. Converts to local coordinates (origin based on Target Box)
        self.point1 = (inputs[3:5])
        self.implicitEquation = Implicit(self.vector, self.point1)

        #Make sure point 1 is off the view (targetbox)
        if((self.point1[0] > 0) or (self.size-self.point1[1]) > 0):
            self.point1 = [self.point1[i] - (self.vector[i]*2000)
                           for i in range(len(self.point1))]

        self.point2 = [self.point1[i] + (self.vector[i]*self.size*2000)
                       for i in range(len(self.point1))]


    def read(self, fileName):
            # Function to read the variables fromthe file based on the format specified
            # fileName parameter is the name of the file to open
        with open(fileName) as file:
                # Read in whole file and split into array
            variables = file.read().split()
            variables = [int(variables[i]) for i in range(len(variables))]
        return variables


scale = 15 #Factor to scale the window by
winPos = 0  # Keep track of where to place the new window
for i in range(5):
    root = tk.Tk()  # New window
    line = Line('line' + str(i+1) + '.txt')  # Initialize line with file
    root.geometry('+%d+%d' % (winPos, 100))  # Set location of new window
    winPos += line.size*scale+25

    C = tk.Canvas(root, bg="#000000", height=(line.size)  # Setup Canvas
                  * scale, width=(line.size)*scale)

    C.create_line(line.point1[0]*scale, line.size*scale-line.point1[1]*scale, line.point2[0]
                  * scale, line.size*scale-line.point2[1]*scale, fill="#84bd00", width="2")  # Draw Line

    C.create_text(100, 20, fill="#84bd00", font=tk.font.Font(
        family='Helvetica'), text=str(line.implicitEquation.eqString()))  # Make EQ label

    C.pack()
    app = Application(master=root, name='line' + str(i+1) + '.txt')


app.mainloop()
