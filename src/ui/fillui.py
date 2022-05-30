import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

from framebuffer import buffer
from functions.polyline import poli
from functions.floodfill import recursive_fill

class fill_screen:
    def __init__(self, master=None):
        # build ui
        self.fill = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame_fill = ttk.Frame(self.fill)
        self.frame_input = ttk.Frame(self.frame_fill)
        self.frame_grade = ttk.Frame(self.frame_fill)

        self.lb_text = ttk.Label(self.frame_input)
        self.lb_text.configure(
            text="Preenchimento:\n1) Especifique pontos para um polígno qualquer e\nclique no botão para desenhá-lo\n",
            justify="center")
        self.lb_text.grid(column="0", padx="5", pady="5", row="0", columnspan="2")

        self.bttn_do = ttk.Button(self.frame_input, command=self.bttn_click)
        self.bttn_do.configure(text="Desenhar")
        self.bttn_do.grid(
            column="0",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="2",
            columnspan="2"
        )

        self.bttn_back = ttk.Button(self.frame_input)
        self.bttn_back.configure(text="Voltar", command=self.fill.destroy)
        self.bttn_back.grid(
            column="0",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="3",
            columnspan="2"
        )

        #Radio buttons
        self.select_fill = tk.IntVar(self.fill)
        self.select_fill.set(2)

        self.select_recursive = tk.Radiobutton(self.frame_input)
        self.select_recursive.configure(text="Recursivo", variable=self.select_fill, value=0)

        self.select_scanline = tk.Radiobutton(self.frame_input)
        self.select_scanline.configure(text="Varredura", variable=self.select_fill, value=1)
        #------------------
        self.frame_input.configure(height="600", width="400")
        self.frame_input.grid(column="0", row="0")

        self.frame_grade.configure(height="400", relief="ridge", width="400")
        self.frame_grade.grid(column="1", row="0")
        self.g = buffer(self.frame_grade)

        self.frame_fill.configure(borderwidth="5",
            height="400",
            padding="10",
            relief="ridge",
            width="600"
            )
        self.frame_fill.grid(column="0", row="0")

        self.fill.configure(height="400", padx="10", pady="10", width="600")
        self.fill.title("CG")

        # Main widget
        self.mainwindow = self.fill

    def bttn_click(self, event=None): #evento do clique do botao
        if self.select_fill.get() == 0: # Recursive
            try:
                if len(self.g.pts) == 1:
                    self.bttn_do.configure(state="disabled")
                    self.select_recursive.configure(state="disabled")
                    self.select_scanline.configure(state="disabled")
                    pts_recursive = []

                    self.g.matriz[self.g.pts[0][0]][self.g.pts[0][1]] = 0
                    self.g.matriz, pts_recursive = recursive_fill(self.g.matriz, self.g.pts[0][0], self.g.pts[0][1], pts_recursive)
                    self.g.set_point(pts_recursive, '#00b0f0')
                else:
                    messagebox.showerror("Atenção", "Selecione um ponto para preenchimento", parent=self.fill)
            except RecursionError:
                messagebox.showinfo("Atenção", "Recusividade máxima alcançada", parent=self.fill)
        
        elif self.select_fill.get() == 1: # Scanline
            if len(self.g.pts) == 1:
                #self.bttn_do.configure(state="disabled")
                #self.select_recursive.configure(state="disabled")
                #self.select_scanline.configure(state="disabled")
                
                messagebox.showerror("Atenção", "Função não implementada", parent=self.fill)

        elif self.select_fill.get() == 2: #Poligono
            if len(self.g.pts) >= 3:
                self.lb_text.configure(text="Preenchimento:\n2) Especifique um ponto para preenchimento\ne selecione o tipo.\n")
                self.select_scanline.grid(column="1", row="1")
                self.select_recursive.grid(column="0", row="1")
                self.bttn_do.configure(text="Preencher")

                pts_recursive = poli(self.g.pts)
                for p in pts_recursive: self.g.set_point(p, '#000000')

                self.select_fill.set(0)
                self.g.pts = []
            else: #< 2 pontos
                messagebox.showerror("Atenção", "Clique em pelo menos 3 pontos", parent=self.fill)

    def run(self):
        self.mainwindow.mainloop()