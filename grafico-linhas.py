# GRÁFICO DE LINHAS
#
#

# Importação dos pacotes
import matplotlib.pyplot as plt
import pandas as pd

# Fonte de dados
base = 'https://raw.githubusercontent.com/Mekylei-Belchior/visualizacao-dados/master/dados/populacao-brasileira.csv'

# Importação da base de dados para um DataFrame
dados = pd.read_csv(base, sep=';', encoding='cp1252')

# TRATAMENTO DOS DADOS
#

# Renomeando coluna
dados.rename(columns={'Taxa de crescimento': 'Crescimento'}, inplace=True)

# Alterando o tipo de dado da coluna população
dados['População'] = dados['População'].apply(
    lambda x: str(x).replace(' ', ''))
dados['População'] = dados['População'].astype('int64')

# Alterando o tipo de dado da coluna crescimento
dados['Crescimento'] = dados['Crescimento'].apply(
    lambda x: str(x).replace(' %', ''))
dados.iloc[0, 2] = 0
dados['Crescimento'] = dados['Crescimento'].astype('float64')

# GRÁFICO
#

# Define o tamanho do gráfico em polegadas
plt.figure(figsize=(12, 5))

# Definição do período de análise
p_anos = dados['Ano'][1:]
p_taxa = dados['Crescimento'][1:]

# Define o título do gráfico e rótulos dos eixos
titulo = 'Crescimento Populacional (1952 - 2020)'

eixoX = 'Ano'
eixoY = 'Taxa de Crescimento (%)'

# Inseri o título e os rótulos de eixos no gráfico
plt.title(titulo)

plt.xlabel(eixoX)
plt.ylabel(eixoY)

# Constrói e mostra o gráfico
plt.plot(p_anos, p_taxa, color='green', linestyle='dashed')
plt.show()
