# GRÁFICO DE BARRAS
# 
# 

# Importação do pacote
import matplotlib.pyplot as plt

# Eixo eixo das abscissas (x) e eixo das ordenadas (y)
produtos = ['Arroz', 'Feijão', 'Tomate', 'Batata', 'Carne', 'Suco']
valores = [10.78, 8.69, 6.5, 4.3, 29.9, 3.87]

# título do gráfico
titulo = 'Produto x Valor'

# Rótulo dos eixos
eixoX = 'Eixo X'
eixoY = 'Eixo Y'

# Inseri o título do gráfico
plt.title(titulo)

# Inseri o rótulo dos eixos
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# Constrói o gráfico de barras
plt.bar(produtos, valores, color = 'green')

# Exibe o gráfico
plt.show()
