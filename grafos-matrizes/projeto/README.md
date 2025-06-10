# Como usar

A forma mais interessante que eu achei é abrindo o terminal interativo do python, pra isso você pode digitar apenas `py`, `python` ou `python3` dependendo do que estiver instalado no seu computador.
Dentro desse terminal você digita `from matrix import *` para conseguir utilizar todas as features. Se estiver fazendo isso em um arquivo mesmo, você importa da mesma forma.

No momento, implementei as operações seguintes operações: adição, subtração, multiplicação por constante, multiplicação entre matrizes e determinante. 

Além de coisas como: operação para deixar a matriz transposta e também modificar/acessar os valores da diagonal principal.

# Segue uma demonstração utilizando o terminal interativo que mencionei antes

```
lucas@desktop:~/Documents/estudos/grafos-matrizes/$ python3
Python 3.12.3 (main, Feb  4 2025, 14:48:35) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from matrix import *
>>> A = Matrix(ncol=3, nrow=3, data=[1,2,3,4,5,6,7,8,9], byrow=True)
>>> print(A)
       [,0]   [,1]   [,2]
[0,]      1      2      3
[1,]      4      5      6
[2,]      7      8      9

>>> print(A * 2) 
       [,0]   [,1]   [,2]
[0,]      2      4      6
[1,]      8     10     12
[2,]     14     16     18

>>> print(A * t(A))
       [,0]   [,1]   [,2]
[0,]     14     32     50
[1,]     32     77    122
[2,]     50    122    194

>>> diag(A, 0) 
<matrix.Matrix object at 0x78e8f84f6180>
>>> print(A)
       [,0]   [,1]   [,2]
[0,]      0      2      3
[1,]      4      0      6
[2,]      7      8      0

>>> exit()
```

### criando e exportanto matrizes
Para criar uma matriz você chama a classe `Matrix`, os argumentos são os seguintes (* indica ser obrigatório):
- ncol* = número de colunas
- nrow* = número de linhas
- byrow = booleano, se você vai preencher pelas linhas ou colunas
- data = uma lista com os dados para preencher a matriz
- dimnames = uma lista com duas listas dentro, a primeira para os rótulos das linhas e a segunda para os rótuls das colunas
### Exemplo completo:
```
>>> A = Matrix(ncol=3, nrow=3, data=[1,2,3,4,5,6,7,8,9], dimnames=[['l um', 'l dois', 'l tres'],['c um', 'c dois', 'c tres']], byrow=True)
>>> print(A)
         c um c dois c tres
l um        1      2      3
l dois      4      5      6
l tres      7      8      9
```
Podemos também criar uma matriz através de um arquivo csv, mas ele obrigatóriamente precisa ter os nomes das colunas e os nomes das linhas definidos. Para isso você precisa chamar o método estático `from_csv()` da classe `Matrix`, passando o caminho/nome do arquivo como argumento, dessa forma: `A = Matrix.from_csv("valores.csv")`

Depois de criar sua matriz, você pode também exportar ela para csv, mas dessa vez você vai chamar o método `to_csv() `na instância da sua matriz, passando o caminho/nome desejado como argumento, dessa forma: `A.to_csv("novos_valores.csv")`

### soma, adição e multiplicação
As operações básicas você chama os operadores padrão do Python para realizar, `A + B` para soma e `A - B` para subtração. Agora para multiplciação com constante, você coloca `A * <valor>` e entre matrizes é `A * B`

### transposta
Para deixar a matriz transposta, você chama o método `t()` e passa como argumento a matriz, ele não vai alterar o valor dela direto, apenas retorna uma nova matriz, se você quiser modificar a atual tem que fazer algo como `A = t(A)`.

### determinante
Para pegar a determinante dela, você chama o método `det()` e passa como argumento a matriz também, eu utilizei o algorítmo de Laplace, então o tempo de execução pode demorar um pouco para matrizes com dimensões maiores. Essa função vai retornar o valor do determinante.

### diagonal principal
Agora para a diagonal principal, chamammos o método `diag()` e passamos como primeiro argumento a matriz, assim ele retorna o valor da diag principal. Caso você informe um segundo valor, ele substitui os valores atuais pelo que for passado, dessa forma: `diag(A, 0)` assim você zerou a diag principal.