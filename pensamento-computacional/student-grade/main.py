from os import system
import pandas as pd


def register_student() -> list:
    system('cls')
    student = []
    student.append(input("Qual o nome do aluno? "))
    
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
    
    student.append("") # equivalente a nota do exame, index 3
    student.append("Aprovado")
    return student

def show_report(students: list) -> None:
    system('cls')
    print("RELATÓRIO DE ALUNOS:")

    for i in range(len(students)): # é completamente banal utilizar o enumerate aqui, não vi sentido algum nisso
        exam = students[i][3]
        if not exam: # quer dizer que exam = "", o python considera isso como um "vazio", quase um Null
            exam = 'N/A' # nesse caso, vamos exibir como N/A, acho melhor do que colocar um espaço vázio, N/A = Não Atribuído

        print(f"Aluno: {students[i][0]} | P1: {students[i][1]} | P2: {students[i][2]} | Exame: {exam} | Situação: {students[i][4]}")

    #seria muito mais fácil dessa forma aqui, mas como não acho que é o que você queria, fiz com um range(len())
    
    # for student in students:
    #     print(f"Aluno: {student[0]} | P1: {student[1]} | P2: {student[2]} | Exame: {exam} | Situação: {student[4]}")

students = []

while True:
    option = input("Digite 1 para cadastrar as notas de um novo aluno ou 0 para sair: ") # acho melhor do que tratar como int, evita um try-except

    if option == '0':
        break

    if option == '1':
        students.append(register_student())
        continue

    print("Opção inválida!")

show_report(students)

headers = ['NOME', 'P1', 'P2', 'EXAME', 'SITUAÇÃO']
df = pd.DataFrame(students)

df.to_csv("notas_alunos.csv", encoding='utf-8', index=False, header=headers)

