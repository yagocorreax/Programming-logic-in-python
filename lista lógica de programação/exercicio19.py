nome = input("Digite o seu nome:")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
media = (nota1 + nota2) / 2
if media > 7:
    print("Você está acima da média, parabéns!")
elif media < 7:
    print("você está abaixo da média, estude mais!")
else:
    print("você está na média, fique de olho!")