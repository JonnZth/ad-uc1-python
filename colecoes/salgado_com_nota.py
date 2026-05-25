salgados_com_nota = \
    [['Coxinha', 8.75],
     ['Kibe', 4.5],
     ['Risole', 6.5],
     ['Pastel', 10],
     ['Pão de Queijo', 10],
     ['Joelho', 10],
     ['Esfirra', 6]]

# Coluna 1 -> Salgado
# Coluna 2 -> Nota

for salgado in salgados_com_nota:
    print(f"- {salgado[0]}: Nota {salgado[1]}")

salgados_com_nota.append('Pizza')


# Compreensão de listas
# Vem da linguagem funcional haskell
salgados_nao_tao_bons = []
for salgado in salgados_com_nota:
    if float(salgado[1]) <= 6:
        print(salgado)
        salgados_nao_tao_bons.append(salgado)

salgados_ruins = [
    salgado for salgado in salgados_com_nota
    if salgado[1] <= 6
                  ]