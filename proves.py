import math

def es_primer(num):
    if num < 2:
        return False
    for i in range (2*0.5+ 1):
        if num % i == 0:
            return False 
print(es_primer(7))   # Ha de mostrar True
print(es_primer(10))  # Ha de mostrar False
            
