import json
from typing import Any

def salvar_dados(arquivo: str, dados:any) -> None: # dados vai receber diversos tipos de dados. e arquivo recebendo uma string.
    """
    salvar dados fornecidos em um arquivo em json
    :param arquivo: caminho para o arquivo json
    param: dados: os dados que serao armazenados no arquivo
    """
    
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f,indent=4, ensure_ascii=False)

def carregar_dados(arquivo: str) -> Any:
    """ 
    le os dados do arquivo json 
    :param arquivo: caminho para o arquivo json
    :return: dados carregados e lidos do arquivo json
    """
    
    try:
        with open(arquivo, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("o arquivo não foi encontrado, caminho do arquivo {arquivo}")
        return {}
    
dados_exemplos = {"nome": "Breno", "cidade": "imperatriz", "cargo": "Programador"}

nome_arquivo = "nome_breno.json"

salvar_dados(nome_arquivo, dados_exemplos)

dados_carregados = carregar_dados(nome_arquivo)

print("Dados carregados:", dados_carregados)