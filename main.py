'''
Desenvolva uma função que (mostre na tela o resultado chamando a função e receba o retorno caso haja):

receba 5 números por parâmetro e retorne uma lista com estes números em ordem crescente.

receba um float e retorne o seu dobro


receba dois floats. O primeiro parâmetro deve ser chamado de valorEmReal e o segundo parâmetro deve ser chamado juros.
Retornar o valorEmReal acrescido da taxa de juros.

'''


def crescente(a, b, c, d, e):

    vet = [a, b, c, d, e]
    vet.sort()
    return vet



def dobro(a:float):
    return float(a*2)


def juros(valorEmReal, juros):
    valorEmReal = float(valorEmReal)
    juros = float(juros/100) + 1

    return round(valorEmReal * juros, 2)

