from matrix import *

A = Matrix.from_csv("data/matriz_incidencia.csv")
    
S = A * t(A) # gera a matriz de similaridade
diag(S, 0) # zera a diagonal principal
S.to_csv("similaridade") # grava em um arquivo .csv

C = t(A) * A # gera a matriz de coocorrencia
diag(C,0) # zera a diagonal principal
C.to_csv("coocorrencia") # grava em um arquivo .csv

