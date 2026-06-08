atual = 1
anterior = 0
prox = 0

while (atual < 2000):
    print(atual)
    prox = atual + anterior
    anterior = atual
    atual = prox
