import tkinter as tk

class framebuffer:
    def __init__(self, frame):
        self.px_width = 10
        self.px_height = 10
        self.pts = []

        self.matriz = self.criarMatriz()
        self.grade = tk.Canvas(frame, height=400, width=400, bg='white')
        self.grade.grid(column="0", row="0")

        self.grade.bind('<Configure>', self.desenhaGrade)
        self.grade.bind('<ButtonPress-1>', self.mouseClick)

    def desenhaGrade(self, event=None):
        for x in range(0, self.grade.winfo_width()):
            for y in range(0, self.grade.winfo_height()):
                x1 = (x * self.px_width)
                x2 = (x1 + self.px_width)
                y1 = (y * self.px_height)
                y2 = (y1 + self.px_height)
                self.grade.create_rectangle(x1,y1,x2,y2)
            self.grade.update()

    def mouseClick(self, event):
        coord = self.grade.find_closest(event.x, event.y)
        if coord:
            rect_id = coord[0]
            self.pts.append([self.grade.canvasx(event.x)//10, self.grade.canvasy(event.y)//10])
            print(self.pts)
            self.grade.itemconfigure(rect_id, fill='red')
    
    def criarMatriz(self):
        matriz = []

        for row in range(40):
            matriz.append([])
            for column in range(40):
                matriz[row].append(0)
                
        return matriz
    
    def putPixel(self):
        pixel = 10
        width = self.grade.winfo_width() # Get current width of canvas
        height = self.grade.winfo_height() # Get current height of canvas
        self.grade.delete('grid_line') # Will only remove the grid_line

        for row in range(40):
            for column in range(40):
                if self.matriz[row][column] == 1:
                    pass