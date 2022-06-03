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

    def draw_gride(self, event=None): #Desenha a grade com retangulos
        for x in range(0, len(self.matriz)):
            for y in range(0, len(self.matriz)):
                x1 = (x * self.px_width)
                x2 = (x1 + self.px_width)
                y1 = (y * self.px_height)
                y2 = (y1 + self.px_height)
                self.grade.create_rectangle(x1,y1,x2,y2)
            self.grade.update()

    def mouse_click(self, event): #Pega a posição do clique do mouse
        x = int(self.grade.canvasx(event.x)//10)
        y = int(self.grade.canvasy(event.y)//10)
        coord = self.grade.find_closest(x*10, y*10)

        if coord:
            self.matriz[x][y] = coord
            self.pts.append([x,y])
            self.put_pixel(x, y, '#000000')

    def put_pixel(self, x, y, color): #Responsável por desenhar os retangulos marcados pela matriz
        if self.matriz[x][y] != 0:
                rect_id = self.matriz[x][y]
                self.grade.itemconfigure(rect_id, fill=color)
                
    def create_mat(self): #Cria a matriz de retangulos que controla o desenho da grade
        matriz = []

        for x in range(41):
            matriz.append([])
            for y in range(41):
                matriz[x].append(0)

        return matriz
    
    def set_point(self, pontos, color): #Dado pontos, marca o retangulo correspondente na matriz de controle
        self.pts = pontos
        
        for p in self.pts:
            if((p[0]<40 and p[1]<40) and (p[0]>=0 and p[1]>=0)):
                coord = self.grade.find_closest(p[0]*10, p[1]*10)
                self.matriz[p[0]][p[1]] = coord
                self.put_pixel(p[0],p[1], color)

    def clear(self):
        self.grade.delete("all")
        self.matriz = self.create_mat()
        self.draw_gride()
        self.pts = []