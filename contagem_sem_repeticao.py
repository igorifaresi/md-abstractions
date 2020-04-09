# Abstrações computacionais para MD
# Igor Fagundes [ifaresi]

def _arranjo(lista, n, ja_escolhidos):
    if len(ja_escolhidos) < n:
        arr = []
        for letra in lista:

            letra_ja_escolhida = False
            for tmp in ja_escolhidos:
                if letra == tmp:
                    letra_ja_escolhida = True
                    break

            if letra_ja_escolhida == False:
                sub_arranjo = _arranjo(lista, n, ja_escolhidos + letra)
                if len(sub_arranjo) > 0:
                    for i in sub_arranjo:
                        arr.append(letra + i)
                else:
                    arr.append('' + letra)
        return arr
    else:
        return []


def arranjo(lista, n):
    return _arranjo(lista, n, '')


def _combinacao(arr):
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


def combinacao(lista, n):
    return _combinacao(arranjo(lista, n))


def permutacao(lista):
    return _arranjo(lista, len(lista), '')


# alguns testes
# print(permutacao('GATO'))
# print(arranjo('123456', 2))
# print(combinacao('12345', 2))
