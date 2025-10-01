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

