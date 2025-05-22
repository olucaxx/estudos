import os
from os.path import exists
from os import makedirs

def show_menu(matriz: list) -> None:
    for i, item in enumerate(matriz): 
        print(f"{i+1} -> {item[0]} | R$ {item[1]}")

def save_order(cart: list, products: list) -> None:
    if not exists('files'):
        makedirs('files')
    with open('files/orders.txt', 'a+', encoding="utf-8") as text_file:
        cart_total = 0
        for i, item in enumerate(cart, 1):
            item_total = products[item[0]-1][1] * item[1]
            cart_total += item_total
            text_file.write(f"{products[item[0]-1][0]};{products[item[0]-1][1]};{item[1]};{item_total}\n")
        text_file.write(str(cart_total) + "\n")

products: list[str,int] = [
    ["Pneu", 500], 
    ["Troca de Óleo",400], 
    ["Alinhamento", 300]
    ]

cart = [] 
print("Bem-vindo, nossos produtos são:")
while True: 
    show_menu(products)
    option = int(input("Digite o código desejado: "))

    if option == 0:
        print("Saindo da seleção de produtos")
        break

    print(f"Digite a quantidade desejada do produto {products[option-1][0]}")
    amount = int(input())

    cart.append([option, amount]) 

os.system('cls')
save_order(cart, products)