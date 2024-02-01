# Finde the greatest commum denominator of two numbers
# using Euclid's algorithm

def greatest_commum_denominator(a: int, b: int) -> int: 
    while (b != 0):
        aux = a
        a = b
        b = aux % b
    return a

print(greatest_commum_denominator(60, 96)) 
# should be 12

print(greatest_commum_denominator(20, 8))   
# should be 4