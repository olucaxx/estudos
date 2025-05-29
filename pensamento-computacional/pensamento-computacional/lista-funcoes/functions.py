def sum_two_nums(a: float, b: float) -> float:
    return float(a + b)

def temp_converter(original_temp: float) -> float:
    print("você deseja converter de:")
    print("1. fahrenheit para celsius")
    print("2. celsius para fahrenheit")
    while True:
        try:
            option: int = int(input("digite o número da opção desejada: ")) 
            # odiei colocar um input dentro de uma função assim, mas se eu fizesse diferente achei que tu poderia descontar nota

            if option == 1:
                return round((original_temp - 32) / 1.8, 2)

            if option == 2:
                return round(original_temp * 1.8 + 32, 2)
            
            print("opção inválida!")
        except:
            print("opção inválida!")


def fact(n: int) -> int:
    # se fosse com recursion ficaria assim:

    #    if n <= 1:
    #        return n
    #    return n * fact(n-1) 
        
    if n <= 1:
        return n

    x: int = 1
    while n > 1:
        x *= n
        n -= 1
    return x

def palindrome(text: str) -> bool:
    # poderiamos usar indexação, ficaria apenas uma linha
    # return text == text[::-1] 

    text = text.strip().replace(" ", "").lower()
    splitted_text: list[str] = [] # poderiamos simplesmente colocar splitted_text = list(text) que funcionária tbm
    reversed_text: list[str] = []
    
    for char in text:
        splitted_text.append(char)
        reversed_text.insert(0, char) # vai sempre inserir na primeira posição, o que "empurra" as outras letras e reverte tudo

    is_palidrome: bool = True

    for i in range(len(splitted_text)):
        if splitted_text[i] != reversed_text[i]:
            is_palidrome = False
            break

    return is_palidrome

def fibo(limit: int) -> list[int]:
    last: int = 1
    current: int = 0
    sequence: list[int] = []

    while current <= limit:
        temp = last
        last = current
        current = temp + last
        sequence.append(last)

    return sequence

def get_prime_numbers(start: int, stop: int) -> list[int]:
    prime_numbers: list[int] = []
    if start <= 1:
        start = 2
        
    if stop == 2:
        return [2]
    
    for i in range(start, stop):
        is_prime: bool = True
        for j in range(2, i-1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(i)
    return prime_numbers

def longest_prefix(words: list[str]) -> str:
    prefix: str = ''
    is_common: bool = True
    
    for i in range(len(words[0])):
        for j in range(len(words)-1): # não vai passar pela última palavra
            if words[-1][i] != words[j][i]: # compara a letra atual da última palavra cm a palavra atual
                is_common = False
                
        if is_common:
            prefix += words[-1][i]
        else:
            break
        
    return prefix
                
def validate_cpf(cpf: str) -> bool:
    is_valid = True
    cpf = cpf.replace(".", "").replace("-", "")
    
    if len(cpf) != 11:
        return False
    
    for i in range(1, 3):
        current_verifier_digit = 8 + i
        sequence = 9 + i
        sum = 0
        
        for j in range(sequence - 1):
            sum += int(cpf[j]) * sequence
            sequence -= 1

        verifier_digit = 11 - (sum % 11)
        
        if verifier_digit >= 10:
            verifier_digit = 0
            
        if verifier_digit != int(cpf[current_verifier_digit]):
            is_valid = False
            break
        
    return is_valid

def translate_bells(sequence: list[str]) -> list[str]:
    translation: list[str] = []     
    
    for bell in sequence:
        if bell.upper() == "DING":
            translation.append("Ensolarado")
        elif bell.upper() == "DONG":
            translation.append("Nublado")
        elif bell.upper() == "DANG":
            translation.append("Chuva")
        else:
            translation.append("DESCONHECIDO")
            
    return translation

def analyze_training(letters: str): # não deu pra usar o typing aqui sem importar o módulo, pois eu não vou retornar uma tuple e teria que usar o Union, acho que ia ficar paia
    # usando um HashMap aqui seria muito fácil, mas como você não ensinou dict fica essa monstrusidade
    
    def add_training(element: str, elements: list[str], amount_of_training: list[int]) -> None:
        if element in elements:
            for i in range(len(elements)):
                if elements[i] == element:
                    amount_of_training[i] += 1
                    return
        elements.append(element)
        amount_of_training.append(1)
        
    def get_most_trained_element(elements: list[str], amount_of_training: list[int]) -> str:
        biggest_num: int = amount_of_training[0]
        element: str = elements[0]
        
        for i in range(1, len(amount_of_training)):
            if amount_of_training[i] > biggest_num:
                biggest_num = amount_of_training[i]
                element = elements[i]
                
            elif amount_of_training[i] == biggest_num:
                element = "Empate!"
                break
            
        return element
    
    elements: list[str] = []
    amount_of_training: list[int] = []
    
    for letter in letters:
        if letter.upper() == "F":
           add_training("Fogo", elements, amount_of_training)
        elif letter.upper() == "W":
            add_training("Água", elements, amount_of_training)
        elif letter.upper() == "E":
            add_training("Terra", elements, amount_of_training)
        elif letter.upper() == "A":
            add_training("Ar", elements, amount_of_training)
        elif letter.upper() == "L":
            add_training("Relâmpago", elements, amount_of_training)
        else:
            add_training("Desconhecido", elements, amount_of_training)
            
    return [elements, amount_of_training, get_most_trained_element(elements, amount_of_training)]
