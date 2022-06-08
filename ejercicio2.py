"""
Hacer un programa que pide caracteres al usuario y los vaya guardando,de formas que al finalizar muestre una lista con todas las vocales y otra con todas las consonantes.
Tambien debe contar cuantas hay de cada una de ellas.
"""

def pedir_caracteres():
    vocales = []
    consonantes = []
    continuar = True
    while continuar:

        pedir= input('Introduzca un caracter: ')
        if pedir in 'aeiuoAEIUO':
            vocales.append(pedir)
        elif pedir in 'BCDFGHJKLMÑPQRSTVWXYZbcdfghjklmñpqrstvwxyz':
            consonantes.append(pedir)
        else:
            continuar = False
    print(vocales)
    print(consonantes)

pedir_caracteres()