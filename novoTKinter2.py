import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import statistics

def moda1(lista):
    moda = statistics.mode(lista)
    print('Moda: ', moda)

def mediana1(lista):
    mediana = statistics.median(lista)
    print('Mediana: ', mediana)

def varianca1(lista):
    varianca = statistics.variance(lista)
    print('Variança: ', varianca)

def desvio1(lista):
    desvio = statistics.stdev(lista)
    print(f'Desvio padrão:  {desvio:.2f}')

def media1(lista):
    media = statistics.mean(lista)
    print('Media: ', media)
 
def grafico():
    cargo = ['A','B','C','D','E']
    empresa1 = [1000,6000,1200,8000,1400]
    empresa2 = [5000,4000,3000,2000,7000]
    empresa3 = [1200,1300,8000,3000,15000]
    empresa4 = [1400,1750,2000,4500,5900]

def handle(lista, salarios):

    print('EMPRESA', salarios)
    print('----------------------------')
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)

handle(empresa1, empresa1)  
handle(empresa2, empresa2)   
handle(empresa3, empresa3) 
handle(empresa4, empresa4)

plt.bar(cargo, empresa1)
plt.bar(cargo, empresa2)
plt.bar(cargo, empresa3)
plt.bar(cargo, empresa4)


plt.plot(True)

plt.show()

import matplotlib.pyplot as plt

plt.title('TESTANDO GRÁFICOS')
ano = ['2021','2022','2023','2024','2025','2026']
vendas = [10000,2000,30000,10000,5000,20000]

plt.plot(ano, vendas)
# plt.bar(labels, frequencia)
# plt.pie(frequencia, labels=labels)

plt.grid(True)

plt.show()

# parte da inclusão de Janela

# Inserindo Gráfico
def grafico():
    cargo = ['A','B','C','D','E']
    empresa1 = [1000,6000,1200,8000,1400]
    # empresa2 = [5000,4000,3000,2000,7000]
    # empresa3 = [1200,1300,8000,3000,15000]
    # empresa4 = [1400,1750,2000,4500,5900]

# criando gráfico
    fig, ax = plt.subplots()
    ax.plot(cargo, empresa1)
    # ax.bar(meses, vendas_em_milhoes, labels=vendas_em_milhoes) #marker = 'o')
    # ax.pie(vendas_em_milhoes, labels=vendas_em_milhoes) #marker = 'o')


# rótulos
    ax.set_xlabel('MESES')
    ax.set_ylabel('VENDAS')
    ax.set_title('GRÁFICO DE VENDAS')
    ax.grid(True)

    # integração
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico) 
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

janela = tk.Tk() #normalmente chamado de root, para esse exemplo utilizado como janela para ficar facil de entender.
janela.title('Vendas')

frame_grafico = tk.Frame(janela)
frame_grafico.pack()

btn = tk.Button(janela, text='mostrar grafico', command=grafico)
btn.pack(padx=10)

janela.mainloop()