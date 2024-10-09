def verifica_parentesis(frase):
    abierto = 0
    cerrado = 0

    for caracter in frase:
        if caracter == '(':
            abierto += 1
        elif caracter == ')':
            cerrado += 1

    if abierto != cerrado:
        print("La cantidad de paréntesis es diferente")
        return False
    else:
        return True

resultado = verifica_parentesis("((ejemplo) de (frase (con) paréntesis) balanceados)")
print(resultado)