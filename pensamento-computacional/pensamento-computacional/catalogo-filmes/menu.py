from funcoes_arquivo import iniciar_pasta_e_arquivos, pegar_filmes, salvar_filmes
import exibir 
from os import system

"""
AQUI FICA A LOGICA PRINCIPAL DO CATALOGO DE FILMES (MENU, CADASTRO E REMOCAO)
"""

def menu() -> None:
    while True:
        filmes_pendentes, filmes_assistidos = pegar_filmes() # carrega nossos filmes
        
        exibir.opcoes()
        
        opcao = input("Insira uma opção: ")
        if opcao == '1':
            exibir.filmes_pendentes(filmes_pendentes)
        elif opcao == '2':
            exibir.filmes_assistidos(filmes_assistidos)
        elif opcao == '3':
            adicionar_filme_pendente(filmes_pendentes)
        elif opcao == '4':
            marcar_filme_como_assistido(filmes_pendentes, filmes_assistidos)
        elif opcao == '5':
            remover_filme(filmes_pendentes, filmes_assistidos)
        elif opcao == '0':
            print("\nEncerrando...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")
        
        salvar_filmes(filmes_pendentes, filmes_assistidos) # guarda os filmes nos seus respectivos arquivos

def adicionar_filme_pendente(filmes_pendentes: list) -> None:
    system('cls')
    # um novo filme precisa dos campos "NOME | DURACAO EM MINUTOS | CATEGORIA | ANO DE LANÇAMENTO"
    
    nome = input("Nome: ")
    
    while True:
        try:
            duracao = int(input("Duração em minutos: "))
            break
        except ValueError:
            print("Número inválido!")
            
    categoria = input("Categoria: ")
    
    while True:
        try:
            ano = int(input("Ano de lançamento: "))
            break
        except ValueError:
            print("Número inválido!")
    
    novo_filme = [nome, duracao, categoria, ano]
    filmes_pendentes.append(novo_filme)
    print(f'{novo_filme} adicionado com sucesso!')
    

def marcar_filme_como_assistido(filmes_pendentes: list, filmes_assistidos: list) -> None:
    # um filme que foi assisitdo precisa ter os campos "NOTA | COMENTÁRIO" adicionados em cima dos 4 originais
    
    exibir.filmes_pendentes(filmes_pendentes)
    try:
        index_filme = int(input("Digite o número do filme que foi assistido: ")) - 1
        novo_filme = filmes_pendentes.pop(index_filme) # pop() remove um elemento pelo index que a gente passar
    except IndexError: # index fora da lista
        print("Filme não encontrado.")
        return
    except ValueError: # valor digitado não é um número inteiro
        print("Número inválido.")
        return
    
    while True:
        try:
            nota = float(input("Digite uma nota de 0 a 10 para o filme: "))
            if not (nota > 10 or nota < 0): # se ela for menor que 0 ou maior que 10, a expressão retorna True, que ao inverter fica False e não quebra o loop
                break
            print("Nota inválida!")
        except ValueError:
            print("Nota inválida!")
            
    comentario = input("Digite um comentário (enter para pular): ")
    
    if not comentario: # se ele apertou enter o comentario é "", entao atribuimos o valor None (que é nulo/vazio) ao inves de ""
        comentario = "N/A"
        
    novo_filme.append(nota)
    novo_filme.append(comentario)
    filmes_assistidos.append(novo_filme)
    

def remover_filme(filmes_pendentes: list, filmes_assistidos: list) -> None:
    system('cls')
    while True:
        opcao = input("1 -> Remover filme pendente ou 2 -> Remover filme assistido? ")
        
        if opcao == '1':
            if not filmes_pendentes:
                print("Nenhum filme para remover.")
                break
            
            exibir.filmes_pendentes(filmes_pendentes)
            try:
                index_filme = int(input('\nDigite o número do filme que deseja remover: ')) - 1
                filme_removido = filmes_pendentes.pop(index_filme) # pop() remove um elemento pelo index que a gente passar
            except IndexError: # index fora da lista
                print("Filme não encontrado.")
            except ValueError: # valor digitado não é um número inteiro
                print("Número inválido.")
            print(f"{filme_removido} removido com sucesso!")
            break
        
        elif opcao == '2':
            if not filmes_assistidos:
                print("Nenhum filme para remover.")
                break
            
            exibir.filmes_assistidos(filmes_assistidos)
            try:
                index_filme = int(input('\nDigite o número do filme que deseja remover: ')) - 1
                filme_removido = filmes_assistidos.pop(index_filme) # pop() remove um elemento pelo index que a gente passar
            except IndexError: # index fora da lista
                print("Filme não encontrado.")
            except ValueError: # valor digitado não é um número inteiro
                print("Número inválido.")
            print(f"{filme_removido} removido com sucesso!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

iniciar_pasta_e_arquivos() # cria a pasta e os arquivos, caso não existam

exibir.boas_vindas() # exibe uma mensagem de boas vindas
menu() # inicia o loop do menu
