import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

from framebuffer import buffer
from functions.polyline import poli
from functions.polyline_clip import sutherland_hodgman

class clip_poly_screen:
    def __init__(self, master=None):
        # build ui
        self.clip_poli = tk.Tk() if master is None else tk.Toplevel(master)
        self.clip = ttk.Frame(self.clip_poli)
        self.frame_input = ttk.Frame(self.clip)
        self.frame_grade = ttk.Frame(self.clip)
        
        self.lb_text = ttk.Label(self.frame_input)
        self.lb_text.configure(
            text="Recorte de Poligono:\nClique em três pontos na grade e clique no botão.\n",
            justify="center")
        self.lb_text.grid(column="0", padx="5", pady="5", row="0")

        self.bttn_do = ttk.Button(self.frame_input)
        self.bttn_do.configure(text="Desenhar", command=self.bttn_click)
        self.bttn_do.grid(
            column="0",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="1"
        )

        self.bttn_back = ttk.Button(self.frame_input)
        self.bttn_back.configure(text="Voltar", command=self.clip_poli.destroy)
        self.bttn_back.grid(
            column="0",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="2"
        )

        self.frame_input.configure(height="600", width="400")
        self.frame_input.grid(column="0", row="0")

        self.frame_grade.configure(height="400", relief="ridge", width="400")
        self.frame_grade.grid(column="1", row="0")
        self.g = buffer(self.frame_grade)

        self.clip.configure(borderwidth="5",
            height="400",
            padding="10",
            relief="ridge",
            width="600"
            )
        self.clip.grid(column="0", row="0")

        self.clip_poli.configure(height="400", padx="10", pady="10", width="600")
        self.clip_poli.title("CG")
        
        self.clip_poli.after(100, self.draw_area)
        self.poligon_area = [[6, 6], [33,6], [33, 33], [6, 33]]

        # Main widget
        self.mainwindow = self.clip_poli
    
    def bttn_click(self, event=None): #evento do clique do botao
        if len(self.g.pts) >= 3:
            clip_points = sutherland_hodgman(self.g.pts, self.poligon_area)
            clip_points = poli(clip_points)
            for pt in clip_points:
                self.g.set_point(pt, '#ff0000')

            self.g.pts = []
        else:
            messagebox.showerror("Atenção", "Clique em três ou mais pontos.", parent=self.clip_poli)
            self.g.clear()
            self.draw_area()
    
    def draw_area(self, event=None): #Desenhar caixa de recorte
        draw_box = poli(self.poligon_area)
        for pt in draw_box:
            self.g.set_point(pt, '#000000')
        self.g.pts = []
            
    def run(self):
        self.mainwindow.mainloop()