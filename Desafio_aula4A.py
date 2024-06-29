
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# Dados iniciais
pib = [150, 300, 500, 800, 150, 300, 900]
estados = ['SP', 'RS', 'BA', 'PE', 'ES', 'MT', 'MS']

# Função para criar o gráfico de barras
def criar_grafico():
    # Lê os dados inseridos nas caixas de entrada
    vendas = []
    for i in range(len(estados)):
        try:
            valor = float(entrada_vendas[i].get())
            vendas.append(valor)
        except ValueError:
            # Tratamento de erro caso o usuário insira um valor inválido
            vendas.append(0.0)

    # Plota o gráfico
    plt.bar(estados, vendas)
    plt.xlabel('Estados')
    plt.ylabel('Vendas')
    plt.title('Vendas por Estado')
    plt.show()

# Configuração da interface gráfica
root = tk.Tk()
root.title('Sistema de Visualização de Dados')

# Cria as caixas de entrada de texto
entrada_vendas = []
for i in range(len(estados)):
    label = tk.Label(root, text=estados[i])
    label.grid(row=i, column=0)
    entrada = tk.Entry(root)
    entrada.grid(row=i, column=1)
    entrada_vendas.append(entrada)

# Botão para criar o gráfico
botao = tk.Button(root, text='Criar Gráfico', command=criar_grafico)
botao.grid(row=len(estados), columnspan=2)

# resultado_text = (f'''
#                       MEDIA {media}
#                       MODA {moda}
#                       MEDIANA {mediana}
#                       DESVIO {desvio}
#                       VARIANÇA {varianca}
                      
#                        '''    ) 
    
#     resultado_label.config(text = resultado_text )

# resultado_label = tk.Label(root, text='')
# resultado_label.pack(pady=10)


root.mainloop()