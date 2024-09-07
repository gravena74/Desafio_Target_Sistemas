def fibonacci(n1, n2):
    return n1 + n2


def control(number, n1, n2):   
    while(True):
        if (number == n1 or number == n2):
            return 'O numero existe'
        elif (n1 > number or n2 > number):
            return 'O numero não existe'
        else:
            # print(n1)
            n1 = fibonacci(n1, n2)
            # print(n2)
            n2 = n1 + n2


if __name__ == '__main__':
    number = int(input("Digite um numero para fazer a verificação de fibonacci: "))
    n1 = 0
    n2 = 1
    print(control(number, n1, n2))