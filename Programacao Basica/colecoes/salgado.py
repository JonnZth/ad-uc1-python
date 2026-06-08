salgados = ['Coxinha', 'Kibe', 'Risole', 'Pastel', 'Pão de Queijo', 'Joelho', 'Esfirra']

print(salgados)

print("\nLista de Salgados:")
for item in salgados:
    print('-',item)

print("\n",salgados[3]) # Pastel

print("\n",salgados[3-5]) # Pão de Queijo.   Posição -2: O penultimo. -1 é o final da lista

print("\n",salgados[3:5]) # Pastel até, não incluindo, Joelho

print("\nLista de Salgados, filtrado:")
for item in salgados[3:5]:
    print('-',item)

print("\n",salgados[0:6:2]) # Coxinha até, não incluindo, Esfirra. Pulando de 2 em 2 itens

if 'Pastel' in salgados:
    print(salgados.index('Pastel')) # Mostra o numero do Index da posição onde Pastel está

if 'Doritos' not in salgados:
    print("Essa salgado não está disponível.")

