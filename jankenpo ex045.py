import random
import sys
from time import sleep

#Fazer o usuário escolher um número entre 1 à 3:
numero = int(input('''Vamos jogar Jankenpô?
                   Escolha um número entre 1 à 3 onde :
                   1 é Pedra
                   2 é Papel
                   3 é Tesoura
                   
                   Insira o Número:     '''))

if numero > 3:
    print('Por favor, escolha um número entre 1 à 3')
    sys.exit()

#Sorteio da máquina
sorteio = random.randint(1, 3)

#Condição de vitória ou derrota:
cond = numero - sorteio

#Nomeando jogador:
if numero == 1: 
    numero = str('Pedra')
if numero == 2:
    numero = str('Papel')
if numero == 3:
    numero = str('Tesoura')

#Nomeando máquina:
if sorteio == 1: 
    sorteio = str('Pedra')
if sorteio == 2:
    sorteio = str('Papel')
if sorteio == 3:
    sorteio = str('Tesoura')

print('=' * 20)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('=' * 20)
sleep(1)

print(f'Você escolheu {numero}')
print(f'Eu escolhi {sorteio}')

print('=' * 20)

#Determinando a vitória ou derrota:
if cond == 0:
    print("Empate!")
elif cond == 1:
    print("Você ganhou!")
elif cond == 2:
    print("Eu ganhei!")

elif cond == -1:
    print("Eu ganhei!")
elif cond == -2:
    print("Você ganhou!")
