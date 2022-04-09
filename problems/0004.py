""" A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers. """

def isPalindrome(a):
    numeroTemp = a;
    reverso = 0;
    
    while (numeroTemp > 0):
        resto = numeroTemp % 10
        reverso = (reverso * 10) + resto
        numeroTemp = numeroTemp // 10

    if (a == reverso):
        return True
    else:
        return False

maior = 0
a = 0
b = 0

for x in range(1, 1000):
    for y in range(1, 1000):
        if (isPalindrome(x*y) and x*y > maior):
            maior = x*y
            a = x
            b = y
            
print("Maior palindromo de 3 números é {} = {} x {}".format(maior, a, b))
