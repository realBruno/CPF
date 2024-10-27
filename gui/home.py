# GUI CPF
# 26/10/2024

import tkinter as tk
from tkinter import ttk

# entrada
window = tk.Tk()
window.title('CPF')
window.geometry('440x320')

# ########################## widgets ##########################
# titulo
title = ttk.Label(master = window,
                  text = 'Gerador de CPF',
                  font = 'Comfortaa 20 bold'
                )
title.pack(pady = 20)

# campo de saída
output = ttk.Label(master = window,
                   text = '123.456.789-00',
                   font = 'Arial 14'
                )
output.pack(pady = 20)

# botoes
""" UMA ALTERNATIVA PARA O SPINBOX É UM MENU SUSPENSO (DROPDOWN) """
frame = ttk.Frame(master = window)
estado = ttk.Spinbox(master = frame)
botao_gerar = ttk.Button(master = frame, text = 'Gerar')
botao_copiar = ttk.Button(master = frame, text = 'Copiar')

estado.pack()
botao_gerar.pack(side = 'left', padx = (0, 10))
botao_copiar.pack(side = 'left', padx = (10, 0))
frame.pack(pady = 20)











window.mainloop()
