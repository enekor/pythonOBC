import tkinter
from tkinter import ttk

lista = ['prueba', 'prueba1']


def add():
    new_elem = elemento.get()
    lista.append(new_elem)
    listbox.insert(tkinter.END, new_elem)


window = tkinter.Tk()
window.title("Lista de objetos")
elemento = tkinter.StringVar()
listbox = tkinter.Listbox(window)

elem_entry = ttk.Entry(textvariable=elemento).pack()
for elem in lista:
    listbox.insert(tkinter.END, elem)
listbox.pack()

boton = ttk.Button(window, text="añadir", command=add).pack()


window.mainloop()