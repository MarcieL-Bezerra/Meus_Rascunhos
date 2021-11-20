import random
q_partidas = int(input("Quantas partidas deseja jogar?:  "))
venceu = 0
perdeu = 0
empate = 0
joken_po = ['Pedra!', 'Papel!', 'Tesoura!']

for i in range(q_partidas):
    sorteio = random.randint(0,2)
    escolha = int(input('Escolha sua jogada ( 0 = Pedra, 1 = papel ou 2 = tesoura) : '))
    #sorteado = joken_po[sorteio]
    if escolha >= 3 or sorteio >= 3:
        print("\nValor invalido! Tente novamente.")
    elif escolha == 0 and sorteio == 2:
        venceu = venceu + 1
        maquina = joken_po[sorteio]
        print("Máquina jogou: " + maquina)
        print("\nVocê Venceu: " + joken_po[escolha] + " Vence: " + joken_po[sorteio])
        
    elif escolha == 2 and sorteio == 1:
        venceu = venceu + 1
        maquina = joken_po[sorteio]
        print("Máquina jogou: " + maquina)
        print("\nVocê Venceu: " + joken_po[escolha] + " Vence: " + joken_po[sorteio])
    elif escolha == 1 and sorteio == 2:
        venceu = venceu + 1
        maquina = joken_po[sorteio]
        print("Máquina jogou: " + maquina)
        print("\nVocê Venceu: " + joken_po[escolha] + " Vence: " + joken_po[sorteio])
    elif escolha == 1 and sorteio == 0:
        venceu = venceu + 1
        maquina = joken_po[sorteio]
        print("Máquina jogou: " + maquina)
        print("\nVocê Venceu: " + joken_po[escolha] + " Vence: " + joken_po[sorteio])
        
    elif escolha ==  sorteio:
        empate = empate + 1
        maquina = joken_po[sorteio]
        print("Máquina jogou: " + maquina)
        print("\nEmpate: " + joken_po[escolha] + " empata: " + joken_po[sorteio])    
    else:
        pedeu = perdeu + 1
        maquina = joken_po[sorteio]
        print("Máquina jogou: " + maquina)
        print("\nVocê Perdeu: " + joken_po[escolha] + " perde para: " + joken_po[sorteio])

print("No total de: {q_partidas} Voce venceu: {venceu}")