import tkinter as tk
import tkinter.ttk as ttk

from ui.bresenui import bresen_screen
from ui.polyui import polyline_screen
from ui.circleui import circle_screen
from ui.curveui import curve_screen
from ui.fillui import fill_screen
from ui.clip_lineui import clip_line_screen

class main:
    def __init__(self, master=None):
        # build ui
        self.root = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame_inicio = ttk.Frame(self.root)

        self.label_titulo = ttk.Label(self.frame_inicio)
        self.label_titulo.configure(
            justify="center", padding="10", text="Trabalho Prático 1"
        )
        self.label_titulo.grid(column="0", columnspan="3", row="0", rowspan="1")

        self.bttn_linha = ttk.Button(self.frame_inicio, command=bresen_screen)
        self.bttn_linha.configure(text="Linhas")
        self.bttn_linha.grid(
            column="0",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="1",
            sticky="nesw",
        )

        self.bttn_circulo = ttk.Button(self.frame_inicio, command=circle_screen)
        self.bttn_circulo.configure(text="Círculos")
        self.bttn_circulo.grid(
            column="1",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="1",
            sticky="nesw",
        )

        self.bttn_curvas = ttk.Button(self.frame_inicio, command=curve_screen)
        self.bttn_curvas.configure(text="Curvas")
        self.bttn_curvas.grid(
            column="2",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="1",
            sticky="nesw",
        )

        self.bttn_linha_poli = ttk.Button(self.frame_inicio, command=polyline_screen)
        self.bttn_linha_poli.configure(text="Polilinhas")
        self.bttn_linha_poli.grid(
            column="0",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="2",
            sticky="nesw",
        )

        self.bttn_preen = ttk.Button(self.frame_inicio, command=fill_screen)
        self.bttn_preen.configure(text="Preenchimento")
        self.bttn_preen.grid(
            column="1",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="2",
            sticky="nesw"
        )

        self.bttn_linha_cut = ttk.Button(self.frame_inicio, command=clip_line_screen)
        self.bttn_linha_cut.configure(text="Recorte\nde Linha")
        self.bttn_linha_cut.grid(
            column="2",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="2",
            sticky="nesw"
        )

        self.bttn_linha_poli_cut = ttk.Button(self.frame_inicio)
        self.bttn_linha_poli_cut.configure(text="Recorte\nde Polígono")
        self.bttn_linha_poli_cut.grid(
            column="0",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="3",
            sticky="nesw"
        )

        self.bttn_trans = ttk.Button(self.frame_inicio)
        self.bttn_trans.configure(text="Transformações")
        self.bttn_trans.grid(
            column="1",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="3",
            sticky="nesw"
        )

        self.bttn_orto = ttk.Button(self.frame_inicio)
        self.bttn_orto.configure(text="Proj. Ortográficas\ne Perspectiva")
        self.bttn_orto.grid(
            column="2",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="3",
            sticky="nesw"
        )

        self.bttn_sair = ttk.Button(self.frame_inicio, command=self.root.destroy)
        self.bttn_sair.configure(text="Sair")
        self.bttn_sair.grid(
            column="1",
            ipadx="10",
            ipady="10",
            padx="10",
            pady="10",
            row="4",
            sticky="nesw"
        )

        self.frame_inicio.configure(
            borderwidth="5", height="200", padding="10", relief="ridge"
        )

        self.frame_inicio.configure(width="200")
        self.frame_inicio.grid(column="0", row="0")
        self.frame_inicio.grid_anchor("center")

        self.root.configure(height="400", padx="10", pady="10", width="600")
        self.root.maxsize(600, 400)
        self.root.title("CG")
        self.root.grid_anchor("center")

        # Main widget
        self.mainwindow = self.root

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = main()
    app.run()