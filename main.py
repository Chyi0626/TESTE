import random

bot = random.randint(1, 5)
vc = str(input("escolhe um número:"))

if vc == bot:
    print("vc acertou o número do BOT!")
else:
    print(f"BURRO! o BOT escolheu o número {bot}!")





itens = ('pedra', 'tesoura', 'papel')
l = random.randint(0, 2)
print('''Qual você escolhe?
[0] pedra
[1] tesoura
[2] papel ''')
você = int(input("Qual é a sua jogada?"))
if l == 0:
    if você == 0:
        print("empate")
    if você == 1:
        print("você perdeu")
    if você == 2:
        print("você ganhou")
if l == 1:
    if você == 0:
        print("você ganhou")
    if você == 1:
        print("empate")
    if você == 2:
        print("você perdeu")
if l == 2:
    if você == 0:
        print("você perdeu")
    if você == 1:
        print("você ganhou")
    if você == 2:
        print("empate")

print(f"Pois o BOT lançou {itens[l]} e você {itens[você]}")
