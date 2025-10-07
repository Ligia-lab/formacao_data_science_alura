#%%

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('imigrantes_canada.csv')
df

# %%

df.info()

# %%

df.set_index('País', inplace=True)

# %%

anos = list(map(str, range(1980, 2014)))
anos

# %%

brasil = df.loc['Brasil', anos]
brasil

# %%

brasil_dict = {'ano' : brasil.index.tolist(), 'imigrantes' : brasil.values.tolist()}
dados_brasil = pd.DataFrame(brasil_dict)
dados_brasil

# %%

plt.figure(figsize=(8,4))
plt.title('Imigração do Brasil pro Canadá')
plt.xlabel('Ano')
plt.ylabel('Nº de imigrantes')
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
plt.show()

# %%
