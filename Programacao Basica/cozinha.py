import math

azulejo_tam = 1.5
comprimento = float(input("Digite o comprimento da cozinha em metros: "))
largura = float(input("Digite o largura da cozinha em metros: "))
altura = float(input("Digite o altura da cozinha em metros: "))

area1 = comprimento * altura
area2 = largura * altura

print(f"\nArea de uma parede ao comprido: {area1} m².")
print(f"Area de uma parede ao longo: {area2} m².\n")

qtdAzulejo1 = (area1 / azulejo_tam) * 2 # duas paredes ao comprido
qtdAzulejo2 = (area2 / azulejo_tam) * 2 # duas paredes ao longo

print(f"Serão necessarios {math.ceil(qtdAzulejo1 + qtdAzulejo2)} caixas de azulejos para cobrir as quatro paredes.")