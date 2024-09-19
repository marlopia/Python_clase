# Importamos módulos
import random, time

# Creamos el deck de cartas
deck = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Definimos función de robar carta
def draw():
    return random.choice(list(deck.keys())) # Convertimos en una lista las claves del diccionario para usar random.choice()

# Definimos la cantidad de jugadores suprimiendo el error de que el usuario meta texto
while True:
    try:
        player_count = int(input("Indica número de jugadores del 1 al 3:"))
        if player_count in [1, 2, 3]:
            break
    except ValueError: # Ignoramos el error de comparar str con int porque es un caso falso
        pass

# Creamos arrays en base a la cantidad de jugadores y añadimos al dealer
all_players = {'Dealer':0}
name = "foo"
for i in range(player_count):
    name = input(f"Introduce el nombre del jugador {i+1}: ")
    all_players[name] = 0

# Función de sumatorio del valor de una mano
def add(hand):
    total = 0
    aces = 0
    for card in hand:
        if card == 'A':
                aces += 1
        total += deck[card]
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Comienzo del juego para jugadores
for player in all_players:
    if player == 'Dealer':
        score = 0
        hand = []
        hand.append(draw())
        while score < 21:
            hand.append(draw())
            score = add(hand)
        all_players['Dealer'] = score
    else:
        print(f"Turno de {player}")
        time.sleep(1) # Añade 1s de pausa
        score = 0
        out = False
        hand = []
        choice = "foo"
        hand.append(draw())
        score = add(hand)
        print(f"{player}, tu mano es {hand}")
        while score < 21 and out != True:
            print(f"{player}, tienes {score} puntos en tu mano")
            answer = input(f"{player}, quieres robar otra carta?(s/n): ")
            if answer == "s":
                time.sleep(1) # Añadimos pausa 1s
                hand.append(draw())
                score = add(hand)
                print(f"{player}, tu mano es {hand}")
            elif answer == "n": 
                out = True
                all_players[player] = score # Graba los puntos en el listado
            else:
                print("Por favor escribe (s/n)")
        score = add(hand)
        all_players[player] = score
        if score > 21:
            print("Te has pasado de 21")
            time.sleep(2) # Añade 2s de pausa
            all_players[player] = score # Graba los puntos en el listado
        if score == 21:
            print("BLACKJACK!!!!!")
            time.sleep(2) # Añade 2s de pausa
            all_players[player] = score # Graba los puntos en el listado

# Tras que juegen todos los jugadores sacamos al ganador

# Filtramos a los que se han pasado de 21
winners = {}
for player,score in all_players.items():
    if score <= 21:
        winners[player] = score

# Saca la clave con el valor más alto, en caso de empate es por posicion de diccionario
max = max(winners, key=winners.get)
print(f"El resultado final es de {all_players}")
print(f"El ganador es {max}")

