palavra_secreta = "Flamengo"
palpite = ""
contador_palpites = 0
limite_palpites = 3
sem_palpites = False

while palpite != palavra_secreta and not(sem_palpites):
    if contador_palpites < limite_palpites:
        palpite = input("Digite a palavra secreta:")
        contador_palpites += 1
else:
    sem_palpites = True

if sem_palpites:
    print('Você ficou sem palpites, VOCÊ PERDEU!!!')
else:
    print("Meus parábens, você acertou!!!!")


