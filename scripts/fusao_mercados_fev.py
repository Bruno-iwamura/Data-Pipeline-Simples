from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# EXTRACT

dados_empresaA = Dados(path_json,'json')
print(f"Colunas do banco de dados Empresa A: \n{dados_empresaA.nome_colunas}")

dados_empresaB = Dados(path_csv,'csv')
print(f"Colunas do banco de dados Empresa B: \n{dados_empresaB.nome_colunas}")

# TRANSFORM

key_mapping = {'Nome do Item': 'Nome do Produto',
                 'Classificação do Produto': 'Categoria do Produto',
                 'Valor em Reais (R$)': 'Preço do Produto (R$)',
                 'Quantidade em Estoque': 'Quantidade em Estoque',
                 'Nome da Loja': 'Filial',
                 'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)

print(f"Colunas renomeadas: \n{dados_empresaB.nome_colunas}")

print(f"Tamnho do arquivo A: {dados_empresaA.size}")
print(f"Tamnho do arquivo B: {dados_empresaB.size}")

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)

print(dados_fusao.nome_colunas)
print(dados_fusao.size)

# LOAD

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)

print(path_dados_combinados)