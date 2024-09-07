def verificaString(a, contador):
    for i in a:
        if i == 'a' or i == 'A':
            contador += 1
    return f'Na palavra existe {contador} letras A ou a.'



if __name__ == "__main__":
    contador = 0
    a = str(input('Digite uma palavra para a verificação: '))
    print(verificaString(a, contador))
