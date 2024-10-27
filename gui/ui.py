# GUI CPF
# 26/10/2024, 27/10/2024

import tkinter as tk
from tkinter import ttk
from tkinter import *

import pyperclip as pc

import main as cpf
from main import gera_cpf

# entrada
window = tk.Tk()
window.title('CPF')
window.geometry('440x320')

def outro():
    output_string.set(gera_cpf())

def copiar_cpf():
    pc.copy(output_string.get())

# ########################## widgets ##########################
# titulo
title = ttk.Label(master = window,
                  text = 'Gerador de CPF',
                  font = 'Comfortaa 20 bold'
                )
title.pack(pady = 20)

# campo de saída
output_string = tk.StringVar()
output = ttk.Label(master = window,
                   font = 'Arial 14',
                   textvariable = output_string,
                )
output.pack(pady = 20)

# botoes
frame = ttk.Frame(master = window)
botao_gerar = ttk.Button(master = frame,
                         text = 'Gerar',
                         command = outro,
                         )

botao_copiar = ttk.Button(master = frame,
                          text = 'Copiar',
                          command = copiar_cpf,
                          )


botao_gerar.pack(side = 'left', padx = (0, 10))
botao_copiar.pack(side = 'left', padx = (10, 0))
frame.pack(pady = 20)






window.mainloop()