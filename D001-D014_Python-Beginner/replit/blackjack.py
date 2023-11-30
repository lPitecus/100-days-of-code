import random

def pegar_carta():
  '''Pega uma carta aleatória do baralho'''
  
  cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return cartas[random.randint(0,12)]

def primeiro_round():
  '''Define as duas primeiras cartas do jogador'''
  
  primeiras_cartas = []
  for i in range(2):
      primeiras_cartas.append(pegar_carta())
  return primeiras_cartas

def adicionar_cartas(lista_de_cartas):
  '''Recebe uma lista com as cartas do jogador e retorna essa lista com uma carta aleatória adicionada'''
  lista_de_cartas.append(pegar_carta())
  return lista_de_cartas

def iniciar_jogo():
  '''Começa o jogo de Blackjack'''
  #flag que diz se o jogo deve continuar ou não
  nao_parou = True
  #distribui as primeiras duas cartas do jogador
  cartas_jogador = primeiro_round()
  #definindo a primeira carta do computador
  cartas_computador= []
  cartas_computador.append(pegar_carta())
  print(f"Essas são suas cartas: {cartas_jogador}, e a soma delas é", sum(cartas_jogador))
  print(f"Essa é a primeira carta do computador: {cartas_computador}")
  #loop que continua até o jogador não querer mais uma nova carta
  while nao_parou:
    choice = input("\nQuer adicionar uma carta nova? 'y' ou 'n': ").lower()
    #caso o jogador queira mais uma carta
    if choice == 'y':
      #chama a função que adiciona mais uma carta na lista do jogador e atualiza essa lista
      cartas_jogador = adicionar_cartas(cartas_jogador)
      #caso a soma da lista do jogador passe de 21, ele perde automaticamente e o jogo acaba.
      if sum(cartas_jogador) > 21:
        print("você passou de 21 obtendo:", sum(cartas_jogador),"\nVocê perdeu.")
        nao_parou = False
      #caso a soma da lista do jogador for igual 21, ainda há possibilidade de empate.  
      elif sum(cartas_jogador) == 21:
        #loop que adiciona cartas na lista do computador enquanto a soma dela for menor que 21.
        while sum(cartas_computador) < 21:
          cartas_computador = adicionar_cartas(cartas_computador)
        #checa se as somas das duas listas são 21, retorna uma mensagem de empate e o jogo acaba.
        if sum(cartas_computador) == sum(cartas_jogador):
          print("Empate!")
          nao_parou = False
      #caso a soma da lista do jogador ainda não chegue em 21, pode-se pedir uma nova carta.
      else:
        print(f"essas são suas cartas {cartas_jogador}")
        print("a soma delas é", sum(cartas_jogador))
        
    elif choice == 'n':
      print(f"Suas cartas são {cartas_jogador}, e a soma delas é", sum(cartas_jogador))
      #da as cartas para o computador enquanto a soma delas for menor do que a soma das cartas do jogador pra ver se ele chega mais perto de 21 (computador ganha)ou passa de 21 (jogador ganha)
      while sum(cartas_computador) < sum(cartas_jogador):
        cartas_computador = adicionar_cartas(cartas_computador)
      print(f"As cartas do computador são {cartas_computador}, e a soma delas é", sum(cartas_computador))
      if sum(cartas_computador) > 21:
        print("Você ganhou!")
      elif sum(cartas_computador) < 21:
        print("Você perdeu!")
      elif sum(cartas_computador) == 21:
        print("Emapte")
      nao_parou = False

iniciar_jogo()