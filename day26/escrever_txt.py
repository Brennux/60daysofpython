def escrever_arquivo(nome_arquivo, conteudo):
    """
    escreve o conteudo em um arquivo txt
    
    arg:
    nome_arquivo(str): O nome do arquvo a ser criado ou subescrito
    conteudo (str): o texto que vai ser escrito no arquivo
    """
    
    with open(nome_arquivo, 'w') as arquivo: #w = write
        arquivo.write(conteudo)
        
    print(f"O conteudo foi salvo no arquivo")

def ler_arquivo(nome_arquivo):
    """
    le o conteudo do arquivo .txt
    
    arg:
    nome_arquivo(str): o nome do arquivo a ser lido
    """
    
    try:
        with open(nome_arquivo, 'r') as arquivo: #r = read ler
            conteudo = arquivo.read()
        print(f"Conteudo do arquivo: {conteudo}")
    except FileNotFoundError:
        print("o arquivo nao foi encontrado tente novamente")
        
def main(nome_arquivo, conteudo):
    """
    funcao principal que demonstra escrita e leitura do nosso arquivo
    
    args:
     nome_arquivo (str) : o nome do arquivo a ser criado e lido.
     conteudo (str): o texto a ser salvo no arquivo.
    """
    
    print("Bem vindos ao nosso programa de escrita e leitura")
    
    #escrevendo no arquivo
    escrever_arquivo(nome_arquivo, conteudo)
    
    #leitura do arquivo
    print("fazendo a leitura do arquivo...")
    ler_arquivo(nome_arquivo)
    
if __name__ == "__main__":
    arquivo ="exemplo.txt"
    texto = "Breno nascimento o lindo"
    
    main(arquivo, texto)