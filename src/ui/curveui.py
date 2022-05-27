#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

from framebuffer import buffer
from functions.bezier_curve import bezier

class curve_screen:
    def __init__(self, master=None):
        # build ui
        self.curve = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame_curve = ttk.Frame(self.curve)
        self.frame_input = ttk.Frame(self.frame_curve)
        self.frame_grade = ttk.Frame(self.frame_curve)

        self.lb_text = ttk.Label(self.frame_input)
        self.lb_text.configure(
            text="Curvas de Bezier:\nClique em pontos na grade\ne aperte no botão abaixo.\n\n(P1 -> P3, P2 = controle)",
            justify="center")
        self.lb_text.grid(column="0", padx="5", pady="5", row="0")

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
        self.bttn_back.configure(text="Voltar", command=self.curve.destroy)
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

        self.frame_curve.configure(borderwidth="5",
            height="400",
            padding="10",
            relief="ridge",
            width="600"
            )
        self.frame_curve.grid(column="0", row="0")

        self.curve.configure(height="400", padx="10", pady="10", width="600")
        self.curve.title("CG")

        # Main widget
        self.mainwindow = self.curve
    
    def bttn_click(self, event=None):
        if len(self.g.pts) >= 3:
            pts = bezier(self.g.pts)
            self.g.set_point(pts)

    def run(self):
        self.mainwindow.mainloop()