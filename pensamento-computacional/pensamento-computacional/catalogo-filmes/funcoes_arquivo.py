import os

"""
AQUI FICAM AS FUNCOES QUE ENVOLVEM A MANIPULACAO DOS ARQUIVOS
"""

CAMINHO_FILMES_PENDENTES = "filmes/pendentes.txt"
CAMINHO_FILMES_ASSISTIDOS = "filmes/assistidos.txt"
PASTA_FILMES = 'filmes'

def iniciar_pasta_e_arquivos():
    if not os.path.exists(PASTA_FILMES): # cria a pasta caso o caminho nao exista.
        os.makedirs(PASTA_FILMES) 
        
    open(CAMINHO_FILMES_PENDENTES, 'a') # o "a" (append) cria o arquivo se ele nao existir.
    open(CAMINHO_FILMES_ASSISTIDOS, 'a') 
    
def pegar_filmes() -> list:
    pendentes = []
    assistidos = []
    
    with(open(CAMINHO_FILMES_PENDENTES, 'r', encoding='utf-8')) as arquivo: # 'r' (read) vai ler o arquivo.
        for filme in arquivo.readlines(): # readlines() le linha por linha, retornando uma lista com todos os filmes sem formatacao.
            
            filme = filme.strip() # strip() remove o '/n' da quebra de linha. ex: 'filme1;100;acao;1989'.
            informacoes_filme = filme.split(";") # split() separa com base nos ';', retornando uma lista de strings. ex: ['filme1', '100', 'acao', '1989'].
            
            pendentes.append(informacoes_filme) # adiciona na lista as informacoes que acabamos de ler.
            
    with(open(CAMINHO_FILMES_ASSISTIDOS, 'r', encoding='utf-8')) as arquivo: # faz a mesma coisa que o de cima, mas para os filmes assistidos.
        for filme in arquivo.readlines(): 
            
            filme = filme.strip() 
            informacoes_filme = filme.split(";") 
            
            assistidos.append(informacoes_filme)
    
    return pendentes, assistidos

def salvar_filmes(filmes_pendentes: list, filmes_assistidos: list) -> None:
    with(open(CAMINHO_FILMES_PENDENTES, 'w', encoding='utf-8')) as arquivo: # 'w' (write) quer dizer que ele apaga o conteudo do arquivo e escreve por cima.
        for filme in filmes_pendentes:
            # escreve o filme separando as informacoes com ";" e finalizando com uma quebra de linha "\n".
            arquivo.write(f'{filme[0]};{filme[1]};{filme[2]};{filme[3]}\n') 
            
    with(open(CAMINHO_FILMES_ASSISTIDOS, 'w', encoding='utf-8')) as arquivo: 
        for filme in filmes_assistidos: 
            arquivo.write(f'{filme[0]};{filme[1]};{filme[2]};{filme[3]};{filme[4]};{filme[5]}\n') 
