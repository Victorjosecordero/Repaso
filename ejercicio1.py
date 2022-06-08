def vocales():
    continuar = True
    while continuar:
        vocal= input('Escriba una letra: ')
        if vocal.lower() in 'aeiou':
            return 'VOCAL'
        elif vocal ==' ':
            continuar == False
        else:
            return 'No vocal'

print(vocales())