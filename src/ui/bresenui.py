import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from framebuffer import buffer
from functions.bresenham import bresenham

class bresen_screen:
    def __init__(self, master=None):
        # build ui
        self.bresenham = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame_bres = ttk.Frame(self.bresenham)
        self.frame_input = ttk.Frame(self.frame_bres)
        self.frame_grade = ttk.Frame(self.frame_bres)

        self.lb_text = ttk.Label(self.frame_input)
        self.lb_text.configure(
            text="Algoritmo de Bresenham:\nClique em dois pontos na grade\ne aperte no botão abaixo.",
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
        self.bttn_back.configure(text="Voltar", command=self.bresenham.destroy)
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
        self.g = buffer(self.frame_grade) #instância da grade

        self.frame_bres.configure(borderwidth="5",
            height="400",
            padding="10",
            relief="ridge",
            width="600"
            )
        self.frame_bres.grid(column="0", row="0")

        self.bresenham.configure(height="400", padx="10", pady="10", width="600")
        self.bresenham.title("CG")

        # Main widget
        self.mainwindow = self.bresenham
    
    def bttn_click(self, event=None): #evento do clique do botao
        if len(self.g.pts) == 2:
            pts = bresenham(self.g.pts)
            self.g.set_point(pts, '#000000')
            self.g.pts = []
        elif len(self.g.pts) > 2: #> 2 pts
            messagebox.showerror("Atenção", "Mais de dois pontos encontrados.", parent=self.bresenham)
            self.g.clear()
        else: # < 2 pts
            messagebox.showerror("Atenção", "Clique em dois pontos.", parent=self.bresenham)
            self.g.clear()

    def run(self):
        self.mainwindow.mainloop()