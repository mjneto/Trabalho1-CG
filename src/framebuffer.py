import tkinter as tk

class buffer:
    def __init__(self, frame):
        self.px_width = 10
        self.px_height = 10
        self.pts = []

        self.matriz = self.create_mat()

        self.grade = tk.Canvas(frame, height=400, width=400, bg='white')
        self.grade.grid(column="0", row="0")

        self.grade.bind('<Configure>', self.draw_gride)
        self.grade.bind('<ButtonPress-1>', self.mouse_click)

    def draw_gride(self, event=None):
        for x in range(0, self.grade.winfo_width()):
            for y in range(0, self.grade.winfo_height()):
                x1 = (x * self.px_width)
                x2 = (x1 + self.px_width)
                y1 = (y * self.px_height)
                y2 = (y1 + self.px_height)
                self.grade.create_rectangle(x1,y1,x2,y2)
            self.grade.update()

    def mouse_click(self, event):
        coord = self.grade.find_closest(event.x, event.y)
        row = int(self.grade.canvasx(event.x)//10)
        column = int(self.grade.canvasy(event.y)//10)

        if coord:
            self.matriz[row][column] = coord
            self.pts.append([row,column])
            self.put_pixel()

    def put_pixel(self):
        for i in self.pts:
            if self.matriz[i[0]][i[1]] != 0:
                    rect_id = self.matriz[i[0]][i[1]]
                    self.grade.itemconfigure(rect_id, fill='black')
                    
    def create_mat(self):
        matriz = []

        for row in range(40):
            matriz.append([])
            for column in range(40):
                matriz[row].append(0)

        return matriz
    
    def set_point(self, pontos):
        self.pts = pontos
        
        for i in self.pts:
            coord = self.grade.find_closest(i[0]*10, i[1]*10)
            self.matriz[i[0]][i[1]] = coord
            self.put_pixel()
        