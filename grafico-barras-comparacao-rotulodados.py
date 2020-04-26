# GRÁFICO DE BARRAS COMPARAÇÃO COM RÓTULO DE DADOS
#
#

# Importação dos pacotes
import numpy as np
import matplotlib.pyplot as plt

# Define o tamanho do gráfico em polegadas
plt.figure(figsize=(8, 6))


def rotulo_dados(barras):
    """
    Adiciona o rótulo de dados para cada barra do gráfico

    param:
            barras: objeto que contém as barras
    """
    for barra in barras:
        altura = barra.get_height()
        plt.annotate('{}'.format(altura),
                     xy=(barra.get_x() + barra.get_width() / 2, altura),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom')


# Produtos vendidos nos mercados
produtos = ['Arroz', 'Feijão', 'Tomate', 'Batata', 'Carne', 'Suco']

# Valor dos produtos vendidos no mercado A
vlr_mercado1 = [10.78, 8.69, 6.5, 4.3, 29.9, 3.87]

# Valor dos produtos vendidos no mercado B
vlr_mercado2 = [10.10, 10.0, 7.5, 2.3, 25.9, 2.97]

# Array com o range de produtos
rp = np.arange(len(produtos))

# Define a largura das barras
largura_barra = 0.4

# Título do gráfico
titulo = 'Compração Mercados (Preço x Produto)'

# Rótulo dos eixos
eixox = 'Produtos'
eixoy = 'Preço'

# Inseri o título do gráfico
plt.title(titulo)

# Inseri o rótulo dos eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Constrói as barras do mercado A
# Passa o objeto como parâmetro para a função que inseri os rótulos de dados
rotulo_dados(plt.bar(rp - (largura_barra / 2), vlr_mercado1,
                     label='Mercado A', color='green', width=largura_barra, tick_label=produtos))

# Constrói as barras do mercado B
# Passa o objeto como parâmetro para a função que inseri os rótulos de dados
rotulo_dados(plt.bar(rp + (largura_barra / 2), vlr_mercado2,
                     label='Mercado B', color='brown', width=largura_barra, tick_label=produtos))

# Encaixa o sub-gráfico na área da figura
plt.tight_layout()

# Inseri a legenda no gráfico
plt.legend(loc='upper left')

# Exibe o gráfico
plt.show()
