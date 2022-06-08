def vocales():
    continuar = True
    while True:
        vocal= input('Escriba una letra: ')
        if vocal.lower() == 'a' or vocal.lower() == 'e' or vocal.lower() == 'i' or vocal.lower() == 'o' or vocal.lower() == 'u':
            return 'VOCAL'
        elif vocal ==' ':
            return False
        else:
            return 'No vocal'

print(vocales())