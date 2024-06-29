
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# criamos uma função para os gráficos

def grafico():
  # Dados
    vendas_em_milhoes = [15,20,30,6,89,1,20]
    meses =  ['JAN', 'FEV', 'MAR', 'ABR', ',MAI', 'JUN', 'JUL']

    # criando gráfico
    
    # ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
    #    wedgeprops=dict(width=size, edgecolor='w'))
    fig, ax = plt.subplots()
    # ax.plot(meses, vendas_em_milhoes, marker = 'o')
    # ax.bar(meses, vendas_em_milhoes, labels=vendas_em_milhoes) #marker = 'o')
    ax.pie(vendas_em_milhoes, labels=vendas_em_milhoes) #marker = 'o')
    
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