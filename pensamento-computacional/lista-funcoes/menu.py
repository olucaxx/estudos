from functions import *

# Lucas Santos Pereira
# RA 2052735
# obs. fiz todos tentando usar o que eu lembro de você ter passado em sala, evitei tuples, dicts, built-in functions e tudo mais

while True:
    try:
        print()
        print("1.  soma de dois números")
        print("2.  conversor de temperatura")
        print("3.  fatorial de um número")
        print("4.  verificar palindromo")
        print("5.  sequência de fibonnaci")
        print("6.  números primos em intervalo")
        print("7.  prefixo comum mais longo")
        print("8.  validador de cpf")
        print("9.  código dos sinos")
        print("10. scrolls dos cinco elementos")
        print("0.  sair")
        
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
                    print(f"sua sequência é {fibo_sequence}")
                    break
                except:
                    print("número inválido!")
                    
        elif option == 6:
            while True:
                try:
                    start: int = int(input("digite onde sua sequência vai começar: "))
                    stop: int = int(input("digite onde sua sequência vai terminar: "))
                    prime_numbers: list[int] = get_prime_numbers(start, stop)
                    print(f"os números primos entre {start} e {stop} são : {prime_numbers}")
                    break
                except:
                    print("número inválido!")

        elif option == 7:
            while True:
                words: list[str] = []
                while True:
                    new_word: str = input("digite uma palavra para adicionar a lista (ou 'sair' para sair): ")
                    if new_word == "sair":
                        break
                    words.append(new_word)
                commom_prefix: str = longest_prefix(words)
                print(f"o maior prefixo em comum entre as palavras {words} é '{commom_prefix}'")
                break

        elif option == 8:
            while True:
                cpf_string: str = input("digite o cpf para validar: ")
                is_valid: bool = validate_cpf(cpf_string)
                if is_valid:
                    print("esse cpf é válido!")
                else:
                    print("esse cpf é inválido!")
                break

        elif option == 9:
            while True:
                bell_sequence: list[str] = []
                for i in range(1, 6):
                    bell_sequence.append(input(f"digite o som do {i}º sino: "))
                translation: list[str] = translate_bells(bell_sequence)
                print(f"o zelador prevê que o clima será {translation}")
                break

        elif option == 10:
            while True:
                scroll_letters: str = input("digite a sequência de letras que aparece em seu pergaminho: ")
                report = analyze_training(scroll_letters)
                print("você deverá treinar: ")
                for i in range(len(report[0])):
                    print(f"{report[0][i]} {report[1][i]} vezes")
                    
                print(f"o elemento dominante é: {report[2]}")
                break

        elif option == 0:
            print("adeus!")
            break
        
        else:
            print("opção inválida!")
        
    except:
        print("opção inválida!")
