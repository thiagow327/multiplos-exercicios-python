def bubble_sort(arr):
    n = len(arr)

    # percorre o vetor
    for i in range(n - 1):
        for j in range(n - i - 1):
            # compara elementos
            if arr[j] > arr[j + 1]:
                # troca elementos de posição
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# vetor
vetor_proposto = [5, 3, 2, 4, 7, 1, 0, 6]

# chama a função para ordenar o vetor
vetor_ordenado = bubble_sort(vetor_proposto)

# imprime o vetor ordenado
print(vetor_ordenado)
