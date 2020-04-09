# Abstrações computacionais para MD
# Igor Fagundes [ifaresi]

def _arranjo_permitindo_repeticao(lista, n, nivel):
    if nivel < n:
        arr = []
        for letra in lista:
            sub_arranjo = _arranjo_permitindo_repeticao(lista, n, nivel + 1)
            if len(sub_arranjo) > 0:
                for i in sub_arranjo:
                    arr.append(letra + i)
            else:
                arr.append('' + letra)
        return arr
    else:
        return []


def arranjo_permitindo_repeticao(lista, n):
    return _arranjo_permitindo_repeticao(lista, n, 0)


def _combinacao_permitindo_repeticao(arr):
    achou_igual = False

    for palavra in arr:
        for i in range(len(arr)):
            if set(list(palavra)) == set(list(arr[i])) and palavra != arr[i]:
                del arr[i]
                achou_igual = True
                break
        if achou_igual == True:
            break

    if achou_igual == True:
        return _combinacao(arr)
    else:
        return arr


def combinacao_permitindo_repeticao(lista, n):
    return _combinacao_permitindo_repeticao(arranjo_permitindo_repeticao(lista, n))


def permutacao_permitindo_repeticao(lista):
    return arranjo_permitindo_repeticao(lista, len(lista))

def _remover_duplicados(lista):
    achou_igual = False
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] == lista[j] and i != j:
                del lista[j]
                achou_igual = True
                break
        if achou_igual == True:
            break

    if achou_igual == True:
        return _remover_duplicados(lista)
    else:
        return lista

def remover_duplicados(lista):
    return _remover_duplicados(lista.copy())

# alguns testes
# print(permutacao_permitindo_repeticao('1234'))
# print(arranjo_permitindo_repeticao('0123456789', 2))
# print(combinacao_permitindo_repeticao('12345', 2))
# print(remover_duplicados(permutacao_permitindo_repeticao('abbc')))
# print(permutacao_permitindo_repeticao('abbc'))
