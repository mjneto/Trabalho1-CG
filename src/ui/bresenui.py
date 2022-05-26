#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

from framebuffer import buffer
from functions.bresenham import bresenham

class bresen_screen:
    def __init__(self, master=None):
        # build ui
        self.Bresenham = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame_bres = ttk.Frame(self.Bresenham)
        self.frame_input = ttk.Frame(self.frame_bres)
        self.frame_grade = ttk.Frame(self.frame_bres)

        self.lb_descricao = ttk.Label(self.frame_input)
        self.lb_descricao.configure(
            text="Algoritmo de Bresenham:\nClique em dois pontos na grade\ne aperte no botão abaixo.",
            justify="center")
        self.lb_descricao.grid(column="0", padx="5", pady="5", row="0")

        self.bttn_do = ttk.Button(self.frame_input)
        self.bttn_do.configure(text="Desenhar")
        self.bttn_do.grid(
            column="0",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="1"
        )
        self.bttn_do.bind("<ButtonPress-1>", self.bttn_click)

        self.bttn_back = ttk.Button(self.frame_input)
        self.bttn_back.configure(text="Voltar", command=self.Bresenham.destroy)
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

        self.frame_bres.configure(borderwidth="5",
            height="400",
            padding="10",
            relief="ridge",
            width="600"
            )
        self.frame_bres.grid(column="0", row="0")

        self.Bresenham.configure(height="400", padx="10", pady="10", width="600")
        self.Bresenham.title("CG")

        # Main widget
        self.mainwindow = self.Bresenham
    
    def bttn_click(self, event=None):
        if len(self.g.pts) >= 2 and len(self.g.pts) < 3:
            pts = bresenham(self.g.pts)
            self.g.set_point(pts)
        else: print('< 2 pts')

    def run(self):
        self.mainwindow.mainloop()