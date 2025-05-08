from functions import *

while True:
    try:
        print()
        print("1. soma de dois números")
        print("2. conversor de temperatura")
        print("3. fatorial de um número")
        print("4. verificar palindromo")
        print("5. sequência de fibonnaci")
        print("0. sair")
        option: int = int(input("digite a opção desejada: "))

        if option == 1:
            while True:
                try:
                    first_num: float = float(input("digite o primeiro número: "))
                    second_num: float = float(input("digite o segundo número: "))
                    print(f"{first_num} + {second_num} = {sum_two_nums(first_num, second_num)}!")
                    break
                except:
                    print("número inválido!")

        elif option == 2:
            while True:
                try:
                    temperature: float = float(input("digite a temperatura que você deseja converter: "))
                    converted_temp: float = temp_converter(temperature)
                    print(f"a temperatura será de {converted_temp}°")
                    break
                except:
                    print("número inválido!")

        elif option == 3:
            while True:
                try:
                    num: int = int(input("digite o número para realizar o fatorial: "))
                    factorial: int = fact(num)
                    print(f"{num}! = {factorial}")
                    break
                except:
                    print("número inválido!")

        elif option == 4:
            while True:
                text: str = input("digite o texto: ")
                if palindrome(text):
                    print("é um palíndromo")
                else:
                    print("não é um palíndromo")
                break


        elif option == 5: 
            while True:
                try:
                    sequence_limit: int = int(input("digite o limite da sua sequência fibonnaci (ela irá parar quando o próximo valor for maior que ele): "))
                    fibo_sequence: list[int] = fibo(sequence_limit)
                    print(f"Sua sequência é {fibo_sequence}")
                    break
                except:
                    print("número inválido!")
                    
        elif option == 6:
            while True:
                try:
                    break
                except:
                    pass
            continue

        elif option == 7:
            while True:
                try:
                    break
                except:
                    pass
            continue

        elif option == 8:
            while True:
                try:
                    break
                except:
                    pass
            continue

        elif option == 9:
            while True:
                try:
                    break
                except:
                    pass
            continue

        elif option == 10:
            while True:
                try:
                    break
                except:
                    pass
            continue

        elif option == 0:
            print("adeus!")
            break
        
        else:
            print("opção inválida!")
        
    except:
        print("opção inválida!")

"""
while True:
    try:
        break
    except:
        pass
continue
"""