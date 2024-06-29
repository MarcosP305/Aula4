# import tkinter as tk
# from tkinter import ttk
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import statistics
# from matpotlib import Figure
# from tkinter import messagbox
# from tkinter import 


# def calcular_estatistica(lista):

#     media = statistics.mean(lista)
#     moda = statistics.mode(lista)
#     mediana = statistics.median(lista)
#     desvio = statistics.stdev(lista)
#     varianca = statistics.variance(lista)
#     return media, mediana, moda, desvio, varianca

# def mostra_analise():
#     empresa1 = [1000,6000,1200,8000,1400]
#     empresa2 = [5000,4000,3000,2000,7000]
#     empresa3 = [1200,1300,8000,3000,15000]
#     empresa4 = [1400,1750,2000,4500,5900]
    
#     cargos = ['A', 'B', 'C', 'D', 'E']


#     empresa_selecionada = empresa var.get()
#     if  empresa_selecionada == 'Empresa ':
#         dado = empresa1
#     elif empresa_selecionada == 'Empresa 2':    
#         dado = empresa2
#     elif empresa_selecionada == 'Empresa 3':
#         dado = empresa3
#     elif empresa_selecionada == 'Empresa 4':
#         dado = empresa4
#     else:
#         messagebox.showerro('erro - Esse dado não existe')
#         return
#     media, moda, mediana, desvio, varianca = calcular_estatisitca(dado)

#     resultado_text = (f'''
#                       MEDIA {media}
#                       MODA {moda}
#                       MEDIANA {mediana}
#                       DESVIO {desvio}
#                       VARIANÇA {variaca}

#                      '''    )
    

    
# resultado_label.config(text = resultado_text )

#     fig = Figure(figsize=(6,4), dpi = 100)
#     ax = fig.add_subplot(111)
#     ax = set_title('CARGOS E SALARIOS')
#     ax = set_xlabel('CARGOS')
#     ax = set_ylabel('SALÁRIOS')
#     ax.plot(cargos, dados)
#     ax.grid(True)
    
#     canvas = FiguraCanvasTkAgg(fig, master=root)
#     canvas.draw()
#     canvas.get_tk_widfet()pack()

# root = ttk.Tk()
# root.title('Cargos e sálatios')
# empresa_var =  tk.StringVar(value=Empresa 1)



# resultado_label = tk.Label(root)
# resultado

# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# import matplotlib.pyplot as plot


# #Criando a função de soma
# def soma():
#     n1 = float(input_entry.get())
#     n2 = float(input_entry2.get())
#     soma  =  n1 + n2
#     label_resultado.config(text=soma)

# # Criando a tela
# janela  = tk.Tk()
# janela.geometry('500x500')
# janela.title('TESTANDO TKINTER')

# #Criando um título para a tela
# text_label = tk.Label(janela, text='calculadora' )
# text_label.pack()

# #inserir dados
# input_entry = tk.Entry(janela)
# input_entry.pack()
# input_entry2 = tk.Entry(janela)
# input_entry2.pack()

# #Criando um botão
# botao = tk.Button(janela, text ='clique aqui', command=soma)
# botao.pack()

# #Visualizando o resltado na tela
# label_resultado = tk.Label(janela, text='Resultado')
# label_resultado.pack()

# # Mantendo a tela em loop 
# janela.mainloop()




# --------------------------------------------------



# # importar libs

# import tkinter as tk
# from tkinter import ttk
# import matplotlib.pyplot as plt
# import matplotlib.pyplot as plot
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# # criamos uma função para os graficos

# def grafico():
#   # dados
#     vendas_em_milhoes  =  [15,20,30,6,89,15, 20]
#     meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAIO', 'JUN', 'JUL']

#    # criando o grafico
#     fig, ax = plt.subplots()
#     ax.bar(meses, vendas_em_milhoes)

#    # rótulos
#     ax.set_xlabel('MESES')
#     ax.set_ylabel('VENDAS')
#     ax.set_title('GRAFICO DE VENDAS')
#     ax.grid(True)
    
#    # Integração do grafico com o TKINTER
#     canvas =  FigureCanvasTkAgg(fig, master=frame_grafico)
#     canvas.draw()
#     canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


# janela = tk.Tk()
# janela.title('Vendas')

# frame_grafico = tk.Frame(janela)
# frame_grafico.pack()

# btn = tk.Button(janela, text='mostrar grafico', command=grafico)
# btn.pack(padx=10)


# janela.mainloop()


# ------------------------------------------


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

    empresa1 = [1000,6000,1200,8000,1400]
    empresa1.sort()
    empresa2 = [5000,4000,3000,2000,7000]
    empresa2.sort()
    empresa3 = [1200,1300,8000,3000,15000]
    empresa3.sort()
    empresa4 = [1400,1750,2000,4500,5900]
    empresa4.sort()
    cargos =  ['Estagiário', 'Vendedor', 'Supervisor', 'Gestor', 'CEO']

    empresa_selecionada = empresa_var.get()
    if  empresa_selecionada == 'Empresa 1':
        dado = empresa1
    elif empresa_selecionada == 'Empresa 2':
        dado = empresa2
    elif empresa_selecionada == 'Empresa 3':
        dado = empresa3
    elif empresa_selecionada == 'Empresa 4':
        dado = empresa4
    else: 
         messagebox.showwarning('erro - Esse dado não existe')
         return  
    
    media, moda, mediana, desvio, varianca = calcular_estatistica(dado)





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
    ax.plot(cargos, dado)
    ax.grid(True)

    canvas =  FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    

root = tk.Tk()
root.title('Cargos e Sálarios')
empresa_var = tk.StringVar(value='Empresa 1')
empresa_opcoes = ['Empresa 1', 'Empresa 2', 'Empresa 3', 'Empresa 4']
menu = ttk.Combobox(root, textvariable =empresa_var, values = empresa_opcoes )
menu.pack()

btn = tk.Button(root, text='Analise', command=mostrar_analise)
btn.pack(pady=10)

resultado_label = tk.Label(root, text='')
resultado_label.pack(pady=10)



root.mainloop()