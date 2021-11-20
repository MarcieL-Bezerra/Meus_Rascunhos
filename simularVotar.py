from datetime import date
data_atual = date.today()
ano = data_atual.year
continuar = 's'
resultado = []
maior = 0
candidados = ['Lucas', 'Matheus','Marcos','Nulos','Brancos']

def votaCao():
	votar = int(input('\n Seja bem vindo! Aqui voce exerce seu direito a cidadania!\n Para Votar em Lucas digite (1)\n Para Votar em Matheus digite (2)\n Para Votar em Marcos digite (3)\n Para votar Nulo digite (4)\n Para votar Branco digite(5)'))
	resultado.append(votar)

def calculaida(anoNas):
	idade = ano - anoNas
	if idade >= 64:
		print("Seu voto é opcional: ")
		votaCao()
	elif idade<16:
		print("Você não pode votar")
		pass
	else:
		votaCao()

while continuar == 's':
	continuar = str(input('Ainda temos pessoas para votar?\nUse (s) para (Sim) ou (n) para (Não): '))
	if continuar == 's':
		anoNas = int(input('\n\nEm que ano você nasceu?: '))
		calculaida(anoNas)
for x in resultado:
	votosComputados = resultado.count(x)
	if votosComputados > maior:
		maior = votosComputados
		campeao = candidados[x-1]

print("\n ******* O CAMPEÃO com: " + str(maior) + " votos foi: " + campeao.upper() + " *******\n")