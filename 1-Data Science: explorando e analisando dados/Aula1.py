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

