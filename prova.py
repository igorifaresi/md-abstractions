import numpy

import gera
import testa

def exibir_erro(dominio, valor, teste):
    tmp = dominio.__name__
    artigo = "dos"
    if tmp[len(tmp) - 1] == 'e' or tmp[len(tmp) - 1] == 'a':
        artigo = "das"
    print("No domínio "+artigo+" "+dominio.__name__+"s, para o valor "+str(valor)+", a proposição \""+teste.__name__+"\" é falsa")
 
def para_todo_natural(dominio, teste, testes):
    for i in range(-testes, testes):
        if teste(dominio(i)) == False:
            exibir_erro(dominio, dominio(i), teste)
            return False
    return True

def para_todo_natural_positivo(dominio, teste, inicio, testes):
    for i in range(inicio, testes):
        if teste(dominio(i)) == False:
            exibir_erro(dominio, dominio(i), teste)
            return False
    return True

def para_todo_real(dominio, teste, passo, testes):
    for i in numpy.arange(-testes, testes, passo):
        if teste(dominio(i)) == False:
            exibir_erro(dominio, dominio(i), teste)
            return False
    return True

def para_todo_real_positivo(dominio, teste, passo, inicio, testes):
    for i in numpy.arange(inicio, testes, passo):
        if teste(dominio(i)) == False:
            exibir_erro(dominio, dominio(i), teste)
            return False
    return True

# alguns testes
# para_todo_natural_positivo(gera.quadrado, testa.par, 0, 10000)
# para_todo_real_positivo(gera.identidade, testa.par, 0.1, 0, 100)
