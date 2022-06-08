def vocales():
    continuar = True
    while continuar:
        vocal= input('Escriba una letra: ')
        if vocal.lower() in 'aeiou':
            print('VOCAL')
        elif vocal ==' ':
            continuar = False
        else:
            print('No vocal')

print(vocales())