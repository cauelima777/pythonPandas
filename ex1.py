import pandas as pd



uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"


notas = pd.read_csv(uri)



notas_filme_32 = notas[notas['movieId'] == 32]



media= notas_filme_32['rating'].mean()


limiar_bom = 3


if media> limiar_bom:
    print("O filme com ID=32 é considerado bom, com média de notas:", round(media,2))
else:
    print("O filme com ID=32 não atende ao critério de ser considerado bom, com média de notas:",round(media,2))