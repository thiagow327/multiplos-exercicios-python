def fatorial(n):
    
    # regra proposta
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


numero = int(input("Digite um numero: "))

if numero < 0:
    print("Não é possível prosseguir com números negativos!")
else:
    resultado = fatorial(numero)
    print(resultado)
