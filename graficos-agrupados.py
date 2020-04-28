# GRAFICOS AGRUPADOS EM UM ÚNICO GRID
#
#

# Importação dos pacotes
import matplotlib.pyplot as plt
import pandas as pd

# Fonte de dados
fonte = 'https://raw.githubusercontent.com/Mekylei-Belchior/visualizacao-dados/master/dados/filmes.csv'

# Importa os dados para um DataFrame ignorando as duas primeiras linhas
# e as últimas dezoito
dados = pd.read_csv(fonte, sep=';', encoding='utf-8',
                    engine='python', skiprows=2, skipfooter=18)

""" TRATAMENTO DOS DADOS """

# Removendo coluna
dados.drop('CPB/ROE', inplace=True, axis=1)

colunas = {
    'Ano de exibição': 'ano_exibicao',
    'Semana de exibição': 'semana_exibicao',
    'Título da obra': 'titulo',
    'Gênero': 'genero',
    'País(es) produtor(es) da obra': 'pais_produtor',
    'Nacionalidade da obra': 'nacionalidade',
    'Data de Lançamento': 'lancamento',
    'Origem da empresa distribuidora': 'origem',
    'Número de Salas na semana dos dados': 'salas',
    'Público na semana dos dados': 'publico',
    'Renda (R$) na semana dos dados': 'renda'
}

# Renomeando as colunas
dados.rename(columns=colunas, inplace=True)

# Reajustando valores de semana de exibição
dados['semana_exibicao'] = dados['semana_exibicao'].apply(
    lambda x: str(x).replace('semana ', ''))

dados['semana_exibicao'] = dados['semana_exibicao'].astype('int64')

# Removendo as aspas dos títulos dos filmes e deixando o texto em
# maiúsculo
dados['titulo'] = dados['titulo'].str.upper().str.replace('"', '')

# Removendo dados inconsistentes e criando um novo DataFrame
# somente com os dados que serão utilizados
filmes = dados[dados['lancamento'] != 'Relançamento'].copy()

# Convertendo a coluna para o formato de data
filmes['lancamento'] = pd.to_datetime(filmes['lancamento'])

# Reajustando valores de origem
origens = {
    'Distribuição Nacional': 'Nacional',
    'Distribuição Internacional': 'Internacional',
    'Codistribuição Internacional-Nacional': 'Internacional-Nacional'
}

filmes['origem'] = [origens.get(origem, None) for origem in filmes['origem']]

# Convertendo a coluna para o formato de número inteiro
filmes['salas'] = filmes['salas'].astype('int64')

# Removendo o separador de milhar e convertendo a coluna para o tipo inteiro
filmes['publico'] = filmes['publico'].apply(lambda x: str(x).replace('.', ''))
filmes['publico'] = filmes['publico'].astype('int64')

# Reajustando e convertendo a coluna renda para tipo inteiro
filmes['renda'] = filmes['renda'].str.replace('.', '').str.replace(',', '.')
filmes['renda'] = filmes['renda'].astype('float64')

""" ANÁLISES """

# Top 10 filmes mais rentáveis
top5_filmes = filmes.groupby(['titulo'])['renda'].sum().nlargest(5) / 1000000
# Top 10 anos mais rentáveis
top10_anos = filmes.groupby(['ano_exibicao'])[
    'renda'].sum().nlargest(10) / 1000000

origem = filmes.groupby(['origem'])['renda'].sum() / 1000000

publico = filmes.groupby('ano_exibicao')['publico'].sum() / 1000000

""" GRÁFICOS """

# Definição da quantidade de gráfico (2 linha x 2 coluna)
fig, axs = plt.subplots(2, 2, figsize=(12, 6), constrained_layout=True)

# Gráfico de pizza
axs[1, 0].pie(origem, labels=origem.index, explode=(0.1, 0, 0),
              autopct='%1.1f%%', shadow=False, startangle=45)
axs[1, 0].set(title='Representatividade por Origem da Produção')

# Gráfico de barra horizontal
axs[0, 0].barh(top5_filmes.index, top5_filmes.values, color='brown')
axs[0, 0].set(title='Top 5 Filmes Rentáveis (R$ Mi)')

# Gráfico de barra
axs[0, 1].bar(top10_anos.index, top10_anos.values, color='purple')
axs[0, 1].set(title='Renda por Ano (R$ Mi)')

# Gráfico de linha
axs[1, 1].plot(publico.index, publico.values, color='green',
               marker='o', linestyle='dashed', linewidth=1.5, markersize=6)
axs[1, 1].set(title='Público por Ano (Milhões)')

plt.show()
