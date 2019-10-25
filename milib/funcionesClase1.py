def divcien(divididoEntre):
    try:
        return 100/divididoEntre
    except ZeroDivisionError:
        print('Error: No se puede dividir entre 0')
def sumatorio(a, b, f):
    s = 0
    for i in range(a, b+1): s+= f(i)
    return s
def cuadrado(x):
    return x*x
def cubo(x):
    return x*x*x
def multiplo(value, factor=2):
    return value * factor
def minymax(lista):
    return min(lista), max(lista)
def suma(a, b):
    return a+b