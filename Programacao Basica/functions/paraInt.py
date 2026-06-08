def toInt():
    try:
        valor = input("Digite um número para ser convertido: ")
        valor = int(valor)
    except ValueError:
        print("----------------------------------------------------")
        print("Erro: O valor informado não é um número inteiro.")
    else:
        print("----------------------------------------------------")
        print(f"O input {valor} foi convertido corretamente.")
    finally:
        print("====================================================")
        print("Fim da operação")
        print("====================================================\n")

print("====================================================")
print("Conversão para Int")
print("====================================================")
toInt()
