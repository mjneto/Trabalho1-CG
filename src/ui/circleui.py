import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

from framebuffer import buffer
from functions.midpoint_circle import circle_mid

class circle_screen:
    def __init__(self, master=None):
        # build ui
        self.circle = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame_circle = ttk.Frame(self.circle)
        self.frame_input = ttk.Frame(self.frame_circle)
        self.frame_grade = ttk.Frame(self.frame_circle)

        self.lb_text = ttk.Label(self.frame_input)
        self.lb_text.configure(
            text="Círculo:\nClique em um ponto na grade\ne aperte no botão abaixo.\n\n (1 ponto = raio padrão 5\n2 pontos = raio calculado de\nacordo com o segundo ponto)",
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
        self.bttn_back.configure(text="Voltar", command=self.circle.destroy)
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

        self.frame_circle.configure(borderwidth="5",
            height="400",
            padding="10",
            relief="ridge",
            width="600"
            )
        self.frame_circle.grid(column="0", row="0")

        self.circle.configure(height="400", padx="10", pady="10", width="600")
        self.circle.title("CG")

        # Main widget
        self.mainwindow = self.circle
    
    def bttn_click(self, event=None): #evento do clique do botao
        if len(self.g.pts) >= 1:
            radius = 0

            if len(self.g.pts) == 1: radius = 5
            else: radius = abs(self.g.pts[0][0]-self.g.pts[1][0])

            pts = circle_mid(radius, self.g.pts[0][0], self.g.pts[0][1])
            for p in pts:
                self.g.set_point(p, '#000000')
            self.g.pts = []
        else:
            messagebox.showerror("Atenção", "Clique em um ponto.", parent=self.circle)
            self.g.clear()
            
    def run(self):
        self.mainwindow.mainloop()