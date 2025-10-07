#%%

import zipfile
import os

arquivo_zip = 'ml-latest-small.zip'
destino = 'ml-latest-small'

if not os.path.exists(destino):
    os.makedirs(destino)

with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
    zip_ref.extractall(destino)

print(f'Conteúdo extraído para: {destino}')

# %%

import pandas as pd

notas = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/ratings.csv')
notas

# %%

notas.shape

#%%

notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']
notas.head()

# %%

notas['nota'].unique()

# %%

notas['nota'].value_counts()

# %%

notas['nota'].mean()

# %%

notas['nota'].plot(kind='hist')

# %%

mediana = notas['nota'].median()
media = notas['nota'].mean()
print(f'Mediana é {mediana}')
print(f'Média é {media}')

# %%

notas['nota'].describe()

# %%

import seaborn as sns

sns.boxplot(notas['nota'])

# %%

filmes = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/movies.csv")
filmes.columns = ['filmeId', 'titulo', 'generos']
filmes.head()

# %%

notas.head()

# %%

notas.query('filmeId==1')['nota'].mean()

# %%

notas.query('filmeId==2')['nota'].mean()

# %%

medias_por_filme = notas.groupby('filmeId')['nota'].mean()
medias_por_filme.head()

# %%

medias_por_filme.plot(kind='hist')

# %%

sns.boxplot(medias_por_filme)

# %%

medias_por_filme.describe()
# %%

import matplotlib.pyplot as plt

sns.displot(medias_por_filme, kde=True)
plt.title('Histograma de médias dos filmes')

# %%

tmdb = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/tmdb_5000_movies.csv")
tmdb.head()

# %%

sns.displot(tmdb['revenue'])
plt.title('Distribuição da receita dos filmes')

# %%

sns.displot(tmdb['budget'])
plt.title('Distribuição da orçamento filmes')

# %%

tmdb.info()

# %%

tmdb.describe()

# %%

tmdb.query('revenue < 500')

# %%

com_faturamento = tmdb.query('revenue > 0')
sns.displot(com_faturamento['revenue'])

# %%

tmdb['original_language'].unique()

# %%

tmdb['original_language'].value_counts()

# %%

tmdb['original_language'].value_counts().index

# %%

tmdb['original_language'].value_counts().values

# %%

contagem_de_lingua = tmdb['original_language'].value_counts().to_frame().reset_index()
contagem_de_lingua.columns = ['original_language', 'total']
contagem_de_lingua.head()

# %%

contagem_de_lingua.plot()

# %%

sns.barplot(data = contagem_de_lingua, x='original_language', y='total')

# %%

sns.countplot(data=tmdb, x='original_language')

# %%

contagem_de_lingua.plot(kind='pie', y='total', labels=contagem_de_lingua['original_language'])

# %%

total_por_lingua = tmdb['original_language'].value_counts()
total_geral = total_por_lingua.sum()
total_ingles = total_por_lingua.loc['en']
total_do_resto = total_geral - total_ingles

#%%

dados = {
    'lingua' : ['ingles', 'outros'],
    'total' : [total_ingles, total_do_resto]
}
dados = pd.DataFrame(dados)
dados

# %%

sns.barplot(data=dados, x='lingua', y='total')

# %%

dados.plot(kind='pie', y='total', labels=dados['lingua'])

# %%

tmdb.query("original_language != 'en'")

# %%

total_de_outros_filmes_por_lingua = tmdb.query("original_language != 'en'")['original_language'].value_counts()
total_de_outros_filmes_por_lingua.head()

# %%

sns.countplot(data=tmdb.query("original_language != 'en'"), 
              x='original_language')

# %%

sns.countplot(data=tmdb.query("original_language != 'en'"), 
              x='original_language', 
              order=total_de_outros_filmes_por_lingua.index)

# %%

sns.countplot(data=tmdb.query("original_language != 'en'"), 
              x='original_language', 
              order=total_de_outros_filmes_por_lingua.index,
              hue='original_language')

# %%

sns.countplot(data=tmdb.query("original_language != 'en'"), 
              x='original_language', 
              order=total_de_outros_filmes_por_lingua.index,
              hue='original_language',
              palette='mako')

# %%

sns.countplot(data=tmdb.query("original_language != 'en'"), 
              x='original_language', 
              order=total_de_outros_filmes_por_lingua.index,
              hue='original_language',
              palette='mako',
              hue_order=total_de_outros_filmes_por_lingua.index)
plt.title('Distribuição de língua original excluindo inglês')
plt.show()

# %%

sns.countplot(data=tmdb.query("original_language != 'en'"), 
              x='original_language', 
              order=total_de_outros_filmes_por_lingua.index,
              hue='original_language',
              palette='mako',
              hue_order=total_de_outros_filmes_por_lingua.index,
              stat='percent')
plt.title('Distribuição de língua original excluindo inglês')
plt.show()

# %%

plt.figure(figsize=(16,8))
sns.countplot(data=tmdb.query("original_language != 'en'"), 
              x='original_language', 
              order=total_de_outros_filmes_por_lingua.index,
              hue='original_language',
              palette='mako',
              hue_order=total_de_outros_filmes_por_lingua.index,
              stat='percent')
plt.title('Distribuição de língua original excluindo inglês')
plt.show()

# %%

filmes.head(2)

# %%

notas_toy_story = notas.query('filmeId==1')['nota']
notas_jumanji = notas.query('filmeId==2')['nota']

media_toy_story = notas_toy_story.mean()
media_jumanji = notas_jumanji.mean()

print(media_toy_story, media_jumanji)

# %%

mediana_toy_story = notas_toy_story.median()
mediana_jumanji = notas_jumanji.median()

print(mediana_toy_story, mediana_jumanji)

# %%

plt.boxplot([notas_toy_story, notas_jumanji])

# %%

sns.boxplot(data=notas.query('filmeId in [1,2]'), 
            x='filmeId', 
            y='nota')

# %%

sns.boxplot(data=notas.query('filmeId in [1,2]'), 
            x='filmeId', 
            y='nota',
            palette='mako')

# %%

notas.groupby('filmeId').count()

# %%

notas['filmeId'].value_counts().tail()

# %%

notas.groupby('filmeId').count().query('nota == 1')


