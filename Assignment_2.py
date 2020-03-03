import tkinter as tk
scale = 15
class Application(tk.Frame):
    def __init__(self, master=None, name=None):
        super().__init__(master)
        self.master = master
        self.winfo_toplevel().title(name)
        #root.overrideredirect(1)
        self.pack()

class Line():
    def __init__(self,file):
        inputs = read(file)
        self.local_origin=inputs[0:2]
        self.size=inputs[2]
        self.vector=inputs[5:7]
        self.point1=(inputs[3:5])
        self.point1=[(self.point1[i] - self.local_origin[i]) for i in range(len(self.local_origin))]
        if((self.point1[0] > 0) or (self.size-self.point1[1])>0):
             self.point1=[self.point1[i] - (self.vector[i]*2000) for i in range(len(self.point1))]
        self.point2=[self.point1[i] + (self.vector[i]*self.size*2000) for i in range(len(self.point1))]
    def getPoints(self):
        points = [self.point1,self.point2]
        return points
    def getSize(self):
        return self.size
    def printLine(self):
        print(self.point1)
        print(self.point2)
        print(self.vector)
    

def read(fileName):
 # Function to read the variables fromthe file based on the format specified
 # fileName parameter is the name of the file to open
    with open(fileName) as file:
 # Read in whole file and split into array
        variables = file.read().split()
        variables = [int(variables[i]) for i in range(len(variables))]
    return variables





for i in range(5):
    root = tk.Tk()
    line = Line('line' + str(i+1) + '.txt')
    C = tk.Canvas(root,bg="black", height=(line.size)*scale, width=(line.size)*scale)
    C.create_line(line.point1[0]*scale, line.size*scale-line.point1[1]*scale, line.point2[0]*scale, line.size*scale-line.point2[1]*scale, fill="red", dash=(4, 4))
    C.pack()
    app = Application(master=root,name='line' + str(i+1) + '.txt')



app.mainloop()