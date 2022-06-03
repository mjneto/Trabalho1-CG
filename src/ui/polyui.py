import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

from framebuffer import buffer
from functions.polyline import poli

class polyline_screen:
    def __init__(self, master=None):
        # build ui
        self.polyline = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame_poly = ttk.Frame(self.polyline)
        self.frame_input = ttk.Frame(self.frame_poly)
        self.frame_grade = ttk.Frame(self.frame_poly)

        self.lb_text = ttk.Label(self.frame_input)
        self.lb_text.configure(
            text="Polilinhas:\nClique em três ou mais pontos na grade\ne aperte no botão abaixo.",
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
        self.bttn_back.configure(text="Voltar", command=self.polyline.destroy)
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

        self.frame_poly.configure(borderwidth="5",
            height="400",
            padding="10",
            relief="ridge",
            width="600"
            )
        self.frame_poly.grid(column="0", row="0")

        self.polyline.configure(height="400", padx="10", pady="10", width="600")
        self.polyline.title("CG")

        # Main widget
        self.mainwindow = self.polyline
    
    def bttn_click(self, event=None): #evento do clique do botao
        if len(self.g.pts) >= 3:
            pts = poli(self.g.pts)
            for p in pts:
                self.g.set_point(p, '#000000')
            self.g.pts = []
        else: # < 3 pts
            messagebox.showerror("Atenção", "Clique em três ou mais pontos.", parent=self.polyline)
            self.g.clear()

    def run(self):
        self.mainwindow.mainloop()