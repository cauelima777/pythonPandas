import pandas as pd


uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv'


notas = pd.read_csv(uri)


print("Os 12 primeiros registros:")
print(notas.head(12))


print("\nOs 6 últimos registros:")
print(notas.tail(6))


print("\nTamanho da massa de dados:", notas.size)
