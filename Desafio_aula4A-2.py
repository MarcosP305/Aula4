import tkinter as tk # Pacote de interface gráfica
import matplotlib.pyplot as plt #ativa a biblioteca do Python para utilização de gráficos.
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

    # Plota o gráfico com cores diferentes para cada estado
    plt.bar(estados, vendas, color=['b', 'g', 'r', 'c', 'm', 'y', 'k'])
    plt.xlabel('Estados')
    plt.ylabel('Vendas')
    plt.title('Vendas por Estado')

    # Exibe estatísticas sobre os dados
    total_vendas = sum(vendas)
    media_vendas = np.mean(vendas)
    plt.text(0.5, 0.9, f'Total de Vendas: R${total_vendas:.2f}', transform=plt.gca().transAxes)
    plt.text(0.5, 0.85, f'Média de Vendas: R${media_vendas:.2f}', transform=plt.gca().transAxes)

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

root.mainloop()
