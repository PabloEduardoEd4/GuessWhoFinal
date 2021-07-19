# 5
# Lady Ann Pachas Tito, 202110749
# Rosa Maria Polti Deustua, 202110629
# Ivanna Tovar Moreno, 202110669
# Joaquin Mendoza Bouroncle, 202110603
# Pablo Eduardo Ghezzi Barton 202110568

# Importacion de librerias nativas
from random import randint

# Importacion de modulos propios
from Cadenas import confirmer, select, board_print
  
# ACA usando import creo el juego.
import Menus

# Gamewinner guarda el nombre del jugador que gana
global gamewinner
gamewinner = ''

# Consigue personajes y descriptores usando 
# los archivos nombres.txt y descriptores.txt
# y los retorna
def generador():
  with open('nombres.txt', 'r') as file:
    nombres = [x for linea in file for x in linea.split(',')]
    file = open('descriptores.txt', 'r')
    descriptores = [x for linea in file for x in linea.split(',')]
  return nombres, descriptores

# Usa dos listas (nombres, descriptores) para generar
# Personajes random que no son repetidos
def random_generador(nombres, descriptores, size = 1):
  out = []
  counter = 0
  while counter != size:
    if (temp := [nombres[randint(0,len(nombres)-1)], descriptores[randint(0,len(descriptores)-1)]]) not in out:
      out.append(temp)
      counter += 1
    else:
      pass
  return out

# Comienzo del juego
# Inicia todos variables y va a la selecion de personajes
def juego_start(p1_nombre, p2_nombre, intentos):
  global gamewinner
  # Consigue nombres, descriptores de generador
  nombres, descriptores = generador()
  all_chr = random_generador(nombres, descriptores, 6)
  # Determinan los intentos de cada Jugador
  p1_intentos = intentos 
  p2_intentos = intentos
  # Crea una nueva lista no ref al original
  p1_chrs = all_chr[:]
  p2_chrs = all_chr[:]
  p1_sel = name_selector(all_chr, p1_nombre) # Va a name selector para selcionar el nombre
  p2_sel = name_selector(all_chr, p2_nombre)
  # Los pone en un array de orden 
  # nombre, selecionado, personajes, intentos
  p1 = [p1_nombre, p1_sel, p1_chrs, p1_intentos]
  p2 = [p2_nombre, p2_sel, p2_chrs, p2_intentos]
  # Comienza el juego
  game(p1, p2)
  return gamewinner

# Seleciona el nombre
def name_selector(all_chr, name):
  while True:
    # Usando join, se puede imprimr una lista sin usar for loops
    print(f"{' '.join([str(x) for x in all_chr[0:3]])}")
    print(f"{' '.join([str(x) for x in all_chr[3:6]])}")
    # Imprime el tablero de 0 a 3 y de 3 a 6
    inp = input(f'Elige tu personaje misterio, {name}: ')
    if inp in (temp := [x[0] for x in all_chr]):
      return all_chr[temp.index(inp)]
    print('OPCION INCORRECTA. INTENTE DE NUEVO.')

# Aca occure el juego usando un gameloop
def game(p1, p2):
  # Este while true no deja que pare el programa
  # Hasta que termine el codigo
  while True:
    res = gameloop(p1, p2)
    if gamewinner != '':
        return True
    res = gameloop(p2, p1)
    if gamewinner != '':
        return True

# El gameloop de turnos
def gameloop(player, notPlayer):
    global gamewinner
    print(f'Es tu turno de {player[0]}')
    # Imprime el board del player
    board_print(player)
    # menu es usado para usar el select, una funcion que lo format
    # Esta en cadenas
    menu = '1. ADIVINAR PERSONAJE, 2. HACER PREGUNTA'
    # selecion
    sel = select(menu, start = 1, end = 2)
    # IFS para selecion de opcion
    if sel == 1:
        inp = input('QUIEN:')
        anws = adiv(player, notPlayer, inp)
        if anws == True:
            gamewinner = player[0]
            return True
        player[3] = player[3] - 1
        print(f"Tiene {player[3]} intentos")
        if player[3] == 0:
            print(f"Lo siento {player[0]}, se quedo sin intentos")
            gamewinner = notPlayer[0]
            return True
    if sel == 2:
        inp = input('PREGUNTA: ')
        anws = preg(player, notPlayer, inp)
    board_print(player)
    # Usando una lista y el anws, evito usar if
    print(f"Jugador ha respodido: {['no', 'si'][anws]}")
    # Imprime intentos
    print(f"Tiene {player[3]} intentos")
    # Saca los personajes puestos por el jugador
    list_rem(player,  [x.strip() for x in input("Ingrese una lista de personajes a remover tablero: ").split(',')])
    # Imprime el board
    board_print(player)
    # Input para pausa
    input()

# opcion de adivinar
def adiv(player, notPlayer, Persona):
    # Input para pausa
    input()
    global gamewinner
    print('Su contricante esta tratando de adivinar su personaje')
    print(f"Su personaje actual: es {notPlayer[1]} . El personaje adivinado era {Persona}")
    menu = '1. ES CORRECTO, 2. ES INCORRECTO'
    if select(menu, start = 1, end = 2) == 1:
        gamewinner = f'{player[0]}'
        return True
    else:
        return False

# opcion de preguntar
def preg(player, notPlayer, pregunta):
    # Input para pausa
    input()
    board_print(notPlayer)
    print('Su contricante le ha hecho la siguiente pregunta:')
    print(pregunta)
    menu = '1. SI, 2. NO'
    return select(menu, start = 1, end = 2) == 1

# sacar de lista
def list_rem(player, remove):
    # Saca los personajes puestos por el jugador
    nombre = [x[0] for x in player[2]]
    for x in remove:
      if x in nombre:
        player[2][nombre.index(x)] = ['X', '']

#Corre el main solo si se ejecuta directamente
if __name__ == "__main__":
  print("Hola, ¡Bienvenido a Adivina Quien!")
  Menus.main()
  print(f'{juego_start(Menus.p1, Menus.p2, Menus.intentos)} ES EL GANADOR!!!')