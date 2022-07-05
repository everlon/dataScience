import pandas as pd

dados_pessoas = pd.read_excel('dados.xlsx', sheet_name='pessoas')
print(dados_pessoas)

dados_notas = pd.read_excel('dados.xlsx', sheet_name='notas')
print(dados_notas)

dados_todos = dados_notas.set_index('nome').join(dados_pessoas.set_index('nome'))
print(dados_todos)

medias = dados_todos.groupby('nome').nota.mean()
print(medias)
medias.to_excel('saida_medias.xlsx')

