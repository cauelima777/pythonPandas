import pandas as pd
import matplotlib.pyplot as plt


url = 'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv'
dados = pd.read_csv(url)


cidade_mais_casos = dados.loc[dados['totalCases'] == dados['totalCases'].max(), 'city'].iloc[0]


cidade_menos_casos = dados.loc[dados['totalCases'] == dados['totalCases'].min(), 'city'].iloc[0]


estado_mais_casos = dados.groupby('state')['totalCases'].sum().idxmax()


estado_menos_casos = dados.groupby('state')['totalCases'].sum().idxmin()


cidade_mais_mortes = dados.loc[dados['deaths'] == dados['deaths'].max(), 'city'].iloc[0]


cidade_menos_mortes = dados.loc[dados['deaths'] == dados['deaths'].min(), 'city'].iloc[0]


estado_mais_mortes = dados.groupby('state')['deaths'].sum().idxmax()


estado_menos_mortes = dados.groupby('state')['deaths'].sum().idxmin()


total_casos_brasil = dados['totalCases'].sum()


total_mortes_brasil = dados['deaths'].sum()


top_estados_mortes = dados.groupby('state')['deaths'].sum().nlargest(5)
top_estados_mortes.plot(kind='bar', title='5 Estados com Mais Mortes por Covid')
plt.xlabel('Estado')
plt.ylabel('Número de Mortes')
plt.show()

bottom_estados_mortes = dados.groupby('state')['deaths'].sum().nsmallest(5)
bottom_estados_mortes.plot(kind='bar', title='5 Estados com Menos Mortes por Covid')
plt.xlabel('Estado')
plt.ylabel('Número de Mortes')
plt.show()

# Imprimir resultados
print("1. Cidade com mais casos de covid:", cidade_mais_casos)
print("2. Cidade com menos casos de covid:", cidade_menos_casos)
print("3. Estado com mais casos de covid:", estado_mais_casos)
print("4. Estado com menos casos de covid:", estado_menos_casos)
print("5. Cidade com mais mortes por covid:", cidade_mais_mortes)
print("6. Cidade com menos mortes por covid:", cidade_menos_mortes)
print("7. Estado com mais mortes por covid:", estado_mais_mortes)
print("8. Estado com menos mortes por covid:", estado_menos_mortes)
print("9. Total de casos de covid no Brasil:", total_casos_brasil)
print("10. Total de mortes por covid no Brasil:", total_mortes_brasil)
