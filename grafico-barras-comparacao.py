# -*- coding: utf-8 -*-


# GRÁFICO DE BARRAS COMPARAÇÃO
#
#

# Importação dos pacotes
import numpy as np
import matplotlib.pyplot as plt

# Produtos vendidos nos mercados
produtos = ['Arroz', 'Feijão', 'Tomate', 'Batata', 'Carne', 'Suco']

# Valor dos produtos vendidos no mercado A
vlr_mercado1 = [10.78, 8.69, 6.5, 4.3, 29.9, 3.87]

# Valor dos produtos vendidos no mercado B
vlr_mercado2 = [10.10, 10.0, 7.5, 2.3, 25.9, 2.97]

# Array com o range de produtos
rp = np.arange(len(produtos))

# Define a largura das barras
largura_barra = 0.35

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
plt.bar(rp - (largura_barra / 2), vlr_mercado1,
        label='Mercado A', color='green', width=largura_barra, tick_label=produtos)

# Constrói as barras do mercado B
plt.bar(rp + (largura_barra / 2), vlr_mercado2,
        label='Mercado B', color='brown', width=largura_barra, tick_label=produtos)

# Inseri a legenda no gráfico
plt.legend(loc='best')

# Exibe o gráfico
plt.show()
