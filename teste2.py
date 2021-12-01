"""
No começo me deparei com problema, onde descobro pouco depois que, 
era para selecionar o interpretador. Os passos para isso são:

1) Ctrl+Shift+P
2) digite -> "python: selecionar interpretador"
3) Clique no interpretador recomendado, no caso é o conda.

"""

from numpy import cos

x = float(input("Insira aqui o valor numérico: "))
print("O cosseno de {} é {}".format(x, cos(x)))
