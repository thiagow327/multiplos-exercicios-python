def soma_multiplos(n):
    soma = 0

    for num in range(n):  # range gera uma sequência de numeros de 0 a n - 1
        if num % 3 == 0 or num % 5 == 0:
            soma += num
    return soma


numero = int(input("Digite um numero: "))
resultado = soma_multiplos(numero)
print(f"A soma dos multiplos de 3 ou 5 a baixo de {numero} é: {resultado}")
