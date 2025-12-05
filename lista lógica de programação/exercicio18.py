ano = int(input("Digite o ano em que você nasceu:"))
ano_atual = 2025
idade= ano_atual - ano
print(f"Sua idade é {idade}") 
if idade >= 18:
    print("Meus parabéns, você pode registrar seu voto eleitoral!")
elif idade< 18:
    print("Infelizmente você ainda não pode votar, volte daqui alguns anos!")

    

