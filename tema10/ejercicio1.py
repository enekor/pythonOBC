import tkinter
from tkinter import ttk


def reiniciar():
    escogido.set(None)


def seleccionar():
    escogido.get()


window = tkinter.Tk()
escogido = tkinter.StringVar()
escogido.set(None)

r1 = ttk.Radiobutton(window, text="opcion1", value="opcion1",
                     variable=escogido, command=seleccionar).pack()
r2 = ttk.Radiobutton(window, text="opcion2", value="opcion2",
                     variable=escogido, command=seleccionar).pack()
r3 = ttk.Radiobutton(window, text="opcion3", value="opcion3",
                     variable=escogido, command=seleccionar).pack()

boton = ttk.Button(window, text="reiniciar", command=reiniciar).pack()

window.mainloop()