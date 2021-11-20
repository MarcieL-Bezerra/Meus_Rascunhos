import os
os.system("cls")
import random
from random import choice
import numpy as np
from time import sleep


class Snake(object):
	"""docstring for Snake"""
	def __init__(self, matriz_size, body_size=2):
		
		self.fruit_position = (int(matriz_size[0]/2),int(matriz_size[1]/2))

		if body_size < 2: 
			body_size = 2

		self.body_size = body_size
		self.body = []

		for c in range(body_size):
			self.body.append((0,c))

		self.head_position = self.body[-1]


	def move(self, action):
		
		"""
		0 : esquerda
		1 : direita
		2 : cima
		3 : baixo
		"""

		d = action

		x = y = 0

		if d == 0:
			y = -1
		elif d == 1:
			y = 1
		elif d == 2:
			x = -1
		else:
			x = 1

		if (self.head_position[0]+x,self.head_position[1]+y) != self.fruit_position: 
			self.body.pop(0)
		self.body.append((self.head_position[0]+x,self.head_position[1]+y))
		self.head_position = self.body[-1]


	def GetState(self):
		return str(self.body+[self.fruit_position])


	def Render(self):

		os.system("cls")
		m = CreateMatriz(matriz_size)

		for x, y in self.body:
			m[x][y] = 1

		m[self.fruit_position[0]][self.fruit_position[1]] = 2
		m[self.body[-1][0]][self.body[-1][1]] = 3

		print("-"*(matriz_size[1]+2))	
		for row in m:
			print("|", end="")
			for col in row:
				if col == 2:
					print("+", end="")
				elif col == 1: 
					print("#", end="")
				elif col == 3: 
					print("@", end="")
				else:
					print(end=" ")
			print("|")
		print("-"*(matriz_size[1]+2))	


def CreateMatriz(matriz_size):
	m = []
	for i in range(matriz_size[0]):
		row = []
		for j in range(matriz_size[1]):
			row.append(0)
		m.append(row)
	return m		


def Step(action):

	done = False
	snake.move(action)
	reward = -0.005
	win = ""
	
	d = action

	x = y = 0

	if d == 0:
		y = -1
	elif d == 1:
		y = 1
	elif d == 2:
		x = -1
	else:
		x = 1

	if snake.head_position in snake.body[:-1]:
		done = True
		win = 0
		reward = -1
	elif len(snake.body) == np.prod(matriz_size):
		done = True
		reward = 1
		win = 1
	elif snake.head_position == snake.fruit_position:
		reward = 0.05
		aux = []
		for i in range(matriz_size[0]):
			for j in range(matriz_size[1]):
				aux.append((i,j))
		while True:
			if(len(aux) > 0):
				new_pos = choice(aux)
			else:
				new_pos = (0,0)
				break
			if(new_pos not in snake.body+[(snake.head_position[0]+x,snake.head_position[1]+y)]):
				break
			aux.remove(new_pos)
		snake.fruit_position = new_pos

	return reward, snake.GetState(), done, win


def CheckMove(action):

		x = y = 0

		if action == 0:
			y = -1
		elif action == 1:
			y = 1
		elif action == 2:
			x = -1
		elif action == 3:
			x = 1

		tmp_head = (snake.head_position[0]+x,snake.head_position[1]+y)

		if tmp_head != snake.body[-1] and tmp_head[0] < matriz_size[0] and tmp_head[1] < matriz_size[1] and \
			tmp_head[0] >= 0 and tmp_head[1] >= 0 and tmp_head != snake.body[-2]:
			return True

		return False


def OnlyCanMove(snake):
	playable_moves = []

	# for move in range(4):
	for i, c in enumerate(Q[snake.GetState()]):
		
		if CheckMove(i):
			playable_moves.append(c)
		else:
			playable_moves.append(-1)


	return playable_moves


def RandomAction(snake):
		moves = [0,1,2,3]

		for _ in range(4):
			move = choice(moves)
			moves.remove(move)

			x = y = 0

			if move == 0:
				y = -1
			elif move == 1:
				y = 1
			elif move == 2:
				x = -1
			else:
				x = 1
			tmp_head = (snake.head_position[0]+x,snake.head_position[1]+y)
			if tmp_head != snake.body[-1] and tmp_head[0] < matriz_size[0] and tmp_head[1] < matriz_size[1] and \
			tmp_head[0] >= 0 and tmp_head[1] >= 0 and tmp_head != snake.body[-2]:
				return move



# Train -------------------------------------------------------------------------------------------
 


matriz_size = [3,3]    
eps = 10000            # Número de epsodios
epsilon = 0.1          # Chance de movimento aleatório (Exploration)
gamma = 0.9
alpha = 0.1
Q = {}				   # Q-Table 


# Train started 
print("> Training...")
for _ in range(eps):
	
	done = False
	snake = Snake(matriz_size)
	# snake.Render()

	while not done:

		state = snake.GetState()
			
		if state not in Q:
			Q[state] = [0,0,0,0]

		if random.uniform(0,1) < epsilon:
			action = RandomAction(snake)            # Exploration

		else:
			action = np.argmax(OnlyCanMove(snake))  # Exploitation

		reward, next_state, done, win = Step(action)

		# snake.Render()

		if next_state not in Q:
			Q[next_state] = [0,0,0,0]
		
		s, a, ns = state, action, next_state
		
		old_value = Q[s][a]
		next_max = np.max(Q[ns])
		new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
		Q[s][a] = new_value



# Test ---------------------------------------------------------------------------------------------

eps = 100
error = 0

os.system("cls")
print("> Training finished!")
input("> Press enter to test ")

for c in range(eps):
	
	done = False
	snake = Snake(matriz_size)
	# snake.Render()

	while not done:

		state = snake.GetState()

		if state not in Q:
			Q[state] = [0,0,0,0]

		action = np.argmax(OnlyCanMove(snake))

		reward, next_state, done, win = Step(action)

		# snake.Render()

		if next_state not in Q:
			Q[next_state] = [0,0,0,0]

	if not win:
		error += 1


print(f"\nErro após {eps} testes: {error} -> {error*eps/100}%")

