#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def somaDoQuadrado(teto):
    soma = 0
    for x in range(1, teto + 1):
        soma += x * x
    return soma

def quadradoDaSoma(teto):
    soma = 0
    for x in range(1, teto + 1):
        soma += x
    return soma * soma
    
def diferenca(x):
    return quadradoDaSoma(x) - somaDoQuadrado(x)
    
print(diferenca(100))
