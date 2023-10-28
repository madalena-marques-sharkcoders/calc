from math import sqrt

while True:
    print("1 - Soma;")
    print("2 - Subtração;")
    print("3 - Multiplicação;")
    print("4 - Divisão;")
    print("5 - Potênciação;")
    print("6 - Resto;")
    print("7 - Raiz;")
    print("8 - Sair.")

    op = int(input("Qual é o modo que você deseja?: "))

    if op == 1:
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        soma = n1 + n2
        print("Resultado: " + str(soma))

    elif op == 2:
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        Subtr = n1 - n2
        print("Resultado: " + str(Subtr))

    elif op == 3:
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        Mult = n1 * n2
        print("Resultado: " + str(Mult))

    elif op == 4:
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        Div = n1 / n2
        print("Resultado: " + str(Div))

    elif op == 5:
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        Pot = n1 ** n2
        print("Resultado: " + str(Pot))

    elif op == 6:
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        Res = n1 % n2
        print("Resultado: " + str(Res))

    elif op == 7:
        n1 = float(input("Insira o número que deseja: "))
        Raiz = sqrt(n1)
        print("Resultado: " + str(Raiz))

    elif op == 8:
        exit()


    else:
        print("Operação Inválida. Tente outro número!")