import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import statistics
from matplotlib.figure import Figure
from tkinter import messagebox
# from tkinter import Combobox



def calcular_estatistica(lista):
    media = statistics.mean(lista)
    moda = statistics.mode(lista)
    mediana =  statistics.median(lista)
    desvio = statistics.stdev(lista)
    varianca = statistics.variance(lista)
    return media, mediana, moda, desvio, varianca


def mostrar_analise():

    # Dados iniciais
    pib = [150, 300, 500, 800, 150, 300, 900]
    estados = ['SP', 'RS', 'BA', 'PE', 'ES', 'MT', 'MS']

    # pib_selecionado = pib_var.get()
    # if  pib == 'Empresa 1':
    #     dado = empresa1
    # elif estados == 'Empresa 2':
    # else: 
    #      messagebox.showwarning('erro - Esse dado não existe')
    #      return  
    
    media, moda, mediana, desvio, varianca = calcular_estatistica(pib)



    resultado_text = (f'''
                      MEDIA {media}
                      MODA {moda}
                      MEDIANA {mediana}
                      DESVIO {desvio}
                      VARIANÇA {varianca}
                      
                       '''    ) 
    
    resultado_label.config(text = resultado_text )



    fig = Figure(figsize=(6,4), dpi = 100)
    ax = fig.add_subplot(111)
    ax.set_title('CARGOS E SALARIOS')
    ax.set_xlabel('CARGOS')
    ax.set_ylabel('SALARIOS')
    ax.plot(estados, pib)
    ax.grid(True)

    canvas =  FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    

root = tk.Tk()
root.title('Cargos e Sálarios')
# pib_var = tk.StringVar(value='Empresa 1')
# empresa_opcoes = ['Empresa 1', 'Empresa 2', 'Empresa 3', 'Empresa 4']
# menu = ttk.Combobox(root, textvariable =empresa_var, values = empresa_opcoes )
# menu.pack()

btn = tk.Button(root, text='Analise', command=mostrar_analise)
btn.pack(pady=10)

resultado_label = tk.Label(root, text='')
resultado_label.pack(pady=10)



root.mainloop()