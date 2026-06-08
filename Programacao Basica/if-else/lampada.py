import math
# from sklearn.preprocessing import StandardScaler

pot = int(input("Digite a potência em watts das lampadas utilizadas: "))
larg = float(input("Digite a largura do cômodo em metros: "))
comp = float(input("Digite o comprimento do cômodo em metros: "))
area = larg * comp

potNec = area * 3 # potencia necessaria pra iluminar a area do comodo
print(f"A potência necessária para iluminar o cômodo é de {potNec} watts.")

quantBocais = math.ceil(area / 3) # quantidade de bocais no cômodo

quantLamp = math.ceil(potNec/pot)

if quantLamp > quantBocais:
    print(f"São necessárias lampadas com potência maior para iluminar o cômodo com a quantidade atual de bocais")
if quantLamp == quantBocais:
    print(f"São necessárias exatas {quantBocais} lampadas, utilizando todos os bocais do cômodo")
if quantLamp < quantBocais:
    print(f"São necessárias apenas {quantLamp} para iluminar o cômodo.")

