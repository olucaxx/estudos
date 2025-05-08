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
                return (original_temp - 32) / 1.8

            if option == 2:
                return original_temp * 1.8 + 32
            
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
    # poderiamos usar indexação, mas como não lembro de ti ter ensinado isso, vou fazer a mão
    # return text == text[::-1] 

    text = text.strip().replace(" ", "").lower()
    splitted_text: list[str] = [] # poderia ser simplesmente um splitted_text = list(text) que funcionária tbm
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
    if start == 1:
        start = 2
    for i in range(start, stop):
        is_prime: bool = True
        for j in range(2, i-1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(i)
    return prime_numbers

print(get_prime_numbers(1, 100))