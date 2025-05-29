from os import system

"""
AQUI FICAM AS FUNCOES QUE ENVOLVEM EXIBIR ALGO PARA O USUARIO  
"""

def boas_vindas() -> None:
    system('clear')
    print("BEM VINDO AO SEU CATÁLOGO DE FILMES")
    print("SELECIONE UMA DAS OPÇÕES ABAIXO PARA COMEÇAR")

def opcoes() -> None:
    print()
    print('1 -> Listar filmes pendentes')
    print('2 -> Listar filmes assistidos')
    print('3 -> Adicionar um filme para assistir')
    print('4 -> Marcar um filme como assistido')
    print('5 -> Remover um filme')
    print('0 -> Sair\n')

def filmes_pendentes(pendentes: list) -> None:
    system('cls')
    if not pendentes:
        print("Nenhum filme pendente!")
        return
    
    print("EXIBINDO FILMES PENDENTES")
    for num, filme in enumerate(pendentes, start=1):
        print(f'{num} - Nome: {filme[0]} | Duração: {filme[1]}min | Categoria: {filme[2]} | Ano: {filme[3]}')

def filmes_assistidos(assistidos: list) -> None:
    system('cls')
    if not assistidos:
        print("Nenhum filme assistido!")
        return
    
    print("EXIBINDO FILMES ASSISTIDOS")
    for num, filme in enumerate(assistidos, start=1):
        print(f'{num} - Nome: {filme[0]} | Duração: {filme[1]}min | Categoria: {filme[2]} | Ano: {filme[3]} | Nota: {filme[4]} | Comentário: {filme[5]}')
