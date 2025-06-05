import os

"""
REUTILIZEI O QUE JÁ HAVIA FEITO NA ÚLTIMA ATIVIDADE DE CADASTRO DE NOTAS
ISSO INCLUI AS FUNÇÕES DE REGISTER_STUDENT E SHOW_REPORT, MANTIVE A MESMA LÓGICA PARA EXAME POIS O SENHOR NÃO PASSOU QUAL CONTA QUERIA
DEIXEI COMENTADO O QUE ACHO QUE SERIA RELEVANTE EXPLICAR PARA TI, QUALQUER DǗVIDA (OU SUSPEITA DE IA) POR FAVOR ME ENCAMINHE EM EMAIL EM 'devpereiralucas@gmail.com'
"""

TXT_PATH = "notas.txt"
CLEAR_TERMINAL = 'cls' if os.name == 'nt' else 'clear'
# eu uso linux, o 'cls' não funciona. então acho que não tem problema colocar essa varíavel de verificação aqui, vou explicar o motivo:
# os.name vai retornar o tipo de sistema operacional que você ta usando, 'nt' é windows e 'posix' vai ser sistemas unix.
# ele vai ver se o retorno é 'nt'. se der True, o comando p limpar o terminal tem que ser 'cls', se der False, o comando tem que ser 'clear'.

def get_students() -> list:
    students = []
    if not os.path.exists(TXT_PATH):
        open(TXT_PATH, 'x', encoding='utf-8') # 'x' cria o arquivo txt pra gente conseguir ler
        return students # a lista vai voltar vazia msm, não temos nd cadastrado
    
    with open(TXT_PATH, 'r', encoding='utf-8') as file:
        for student in file.readlines(): # readlines() pega linha por linha, retornando uma lista ond cada elemento é uma das linhas.
            student = student.strip() # strip() remove o '/n' da quebra de linha que sempre fica no final. 
            student_info = student.split(";") # split() separa com base nos ';', retornando uma lista de strings. 
            students.append(student_info) # adiciona na lista as informacoes que acabamos de ler.
            
    return students


def save_students(students: list) -> None:    
    with open(TXT_PATH, 'w', encoding='utf-8') as file: # 'w' apaga o conteudo do arquivo e escreve por cima.
        if not students: # se a lista estiver vazia, pode gerar um TypeError quando tentamos iterar ele no FOR abaixo, então vamos retornar antes.
            return 
        
        for student in students:
            # escreve o filme separando as informacoes com ";" e finalizando com uma quebra de linha "\n".
            file.write(f'{student[0]};{student[1]};{student[2]};{student[3]};{student[4]}\n') 
           
    
def show_report(students: list) -> None:
    print("ALUNOS CADASTRADOS:\n")
    
    if not students:
        print('Nenhum aluno cadastrado.')
        return
    
    for index, student in enumerate(students, start=1): 
        print(f"{index:03} - Aluno: {student[0]} | P1: {student[1]} | P2: {student[2]} | Exame: {student[3]} | Situação: {student[4]}")
    
    
def register_student() -> list:
    student = []
    student.append(input("Qual o nome do aluno? ").strip().upper())
    
    while True:
        try:
            p1 = float(input("Qual a nota da P1? "))
            if p1 >= 0 and p1 <= 10:
                student.append(p1)
                break
            print("Nota inválida!")
        except: 
            print("Nota inválida!")

    while True:
        try:
            p2 = float(input("Qual a nota da P2? "))
            if p2 >= 0 and p2 <= 10:
                student.append(p2)
                break
            print("Nota inválida!")
        except: 
            print("Nota inválida!")

    if ((p1 + p2) / 2) < 7:
        while True:
            try:
                exam_result = float(input("Qual a nota do exame? "))
                if exam_result >= 0 and exam_result <= 10:
                    student.append(exam_result)
                    break
                print("Nota inválida!")
            except: 
                print("Nota inválida!")
        
        if exam_result >= 7:
            student.append("Aprovado")
            return student
        
        student.append("Reprovado")
        return student
    
    student.append("N/A") 
    student.append("Aprovado")
    return student


def remove_student(students: list) -> list:
    if not students:
        print('Nenhum aluno foi cadastrado para ser removido.')
        return
    
    show_report(students)
    while True:
        try:
            student_index = int(input("\nDigite o número do aluno que deseja remover: ")) - 1
            if student_index < 0 or student_index > len(students) - 1:
                print("Número inválido.")
                continue
                
            removed_student = students.pop(student_index)
            print(F"Aluno '{removed_student[0]}' removido com sucesso!")
            break
        
        except ValueError:
            print("Número inválido.")
        
    return students

def menu() -> None:
    students = get_students()
    
    while True:
        print('\n1. Exibir alunos')
        print('2. Cadastrar aluno')
        print('3. Excluir aluno')
        print('0. Sair')
        
        option = input("Digite a opção desejada: ")
        if option == '1':
            os.system(CLEAR_TERMINAL)
            show_report(students)
            continue
        if option == '2':
            os.system(CLEAR_TERMINAL)
            students.append(register_student())
            continue
        if option == '3':
            os.system(CLEAR_TERMINAL)
            students = remove_student(students)
            continue
        if option == '0':
            os.system(CLEAR_TERMINAL)
            print("\nEncerrando...")
            break
        print("\nOpção inválida, tente novamente.")
    
    save_students(students)
    print(f"Alunos salvos com sucesso em '{TXT_PATH}'")
    
menu()