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

for item in salgados_com_nota:
    print(f"- {item[0]}: Nota {item[1]}")

salgados_com_nota.append('Pizza', 10)