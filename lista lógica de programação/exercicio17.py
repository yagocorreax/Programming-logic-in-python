velocidade = float(input("Digite a velocidade do automóvel:"))
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 5
    print("Você foi multado!")
    print(f"você ultrapassou o limite de velocidade em {excesso}")
    print(f"o valor da multa a ser pago é de {multa}")
else:
    print("Tudo certo! você está dentro do limite de velocidade.")


