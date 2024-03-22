while True:
    numero = int(input("INFORME UM NUMERO:" ))

    if numero == 10:
        break

    print(numero)


    for numero2 in range(100):

        if numero == 12:
            continue

        print(numero2 , end=" " )