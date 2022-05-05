from tkinter import *
from tkinter import ttk
from BresenhamTela import teste

root = Tk()
root.title("CG")
root.geometry('600x400')

mainframe = ttk.Frame(root)
mainframe.grid()

s = ttk.Style()
s.configure('Danger.TFrame', borderwidth=5, relief='raised')

frame_inicio = ttk.Frame(mainframe, borderwidth=5, relief="ridge", padding='10', style='Danger.TFrame')
frame_inicio.grid()

label_titulo = ttk.Label(frame_inicio, text="Trabalho Prático 1")
label_titulo.grid(column=0, row=0, columnspan=3)

separador_bttn = 10

bttn_01 = ttk.Button(frame_inicio, text="Bresenham", command=teste)
bttn_01.grid(column=0, row=1, sticky=(W,E), padx=separador_bttn, pady=separador_bttn)

bttn_02 = ttk.Button(frame_inicio, text="Círculos")
bttn_02.grid(column=1, row=1, sticky=(W,E), padx=separador_bttn, pady=separador_bttn)

bttn_03 = ttk.Button(frame_inicio, text="Curvas")
bttn_03.grid(column=2, row=1, sticky=(W,E), padx=separador_bttn, pady=separador_bttn)

bttn_04 = ttk.Button(frame_inicio, text="Polilinha")
bttn_04.grid(column=0, row=2, sticky=(W,E), padx=separador_bttn, pady=separador_bttn)

bttn_05 = ttk.Button(frame_inicio, text="Preenchimento Rec. - Varredura")
bttn_05.grid(column=1, row=2, sticky=(W,E),padx=separador_bttn, pady=separador_bttn)

bttn_06 = ttk.Button(frame_inicio, text="Recorte de linha")
bttn_06.grid(column=2, row=2, sticky=(W,E), padx=separador_bttn, pady=separador_bttn)

bttn_07 = ttk.Button(frame_inicio, text="Recorte de Poligono")
bttn_07.grid(column=0, row=3, sticky=(W,E), padx=separador_bttn, pady=separador_bttn)

bttn_08 = ttk.Button(frame_inicio, text="Transformações")
bttn_08.grid(column=1, row=3, sticky=(W,E), padx=separador_bttn, pady=separador_bttn)

bttn_09 = ttk.Button(frame_inicio, text="Projeção Orto. e Perspectiva")
bttn_09.grid(column=2, row=3, sticky=(W,E), padx=separador_bttn, pady=separador_bttn)

bttn_10 = ttk.Button(frame_inicio, text="Sair", command=root.destroy)
bttn_10.grid(column=1, row=4, sticky=(W,E), padx=separador_bttn, pady=separador_bttn)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()