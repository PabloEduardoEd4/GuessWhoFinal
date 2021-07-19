# Importacion de modulos propios
from Cadenas import select, confirmer
#intetos que estan configurados: Defualt 3
global intentos
intentos = 3
#Flag para ver si salimos o no del programa

# El main del modulo, aca es donde comienza todo
def main():
  while True:
    # Guarda el valor de select
    menu_principal =  select("1. JUGAR, 2. CONFIGURACION, 3. HIGHSCORES, 4. SALIR", 1, 4)
    if menu_principal == 1:
      if personajes():
        return True
    if menu_principal == 2:
      config()
    if menu_principal == 3:
      highscore()
    if menu_principal == 4:
      quit()
  return False

# Configuracion
def config():
    menu = '1. CONFIGURAR INTENTOS, 2. REGRESAR, 3. SALIR'
    # al colocar \n es para que que la lista salga en vertical no en una sola línea 
    opcion = select(menu, 1, 3)
    if opcion == 1:
      config_intentos()
    if opcion == 2:
      return False
    if opcion == 3:
      quit()

# Configuracion, intentos
def config_intentos():
  global intentos
  while True:
    print('Elige 1, 3 o 5')
    intento = input()
    # Uso de confirmer para verificar valides especifica
    if confirmer(intento,1,1) or confirmer(intento,3,3) or confirmer(intento,5,5):
      intentos = int(intento)
      return False
    else:
      print('OPCION INCORRECTA. INTENTE DE NUEVO.')

# Dando nombres a los jugadores
def personajes():
    # globales p1 y p2 para usar en main.py
    global p1
    global p2
    p1 = input('INGRESE EL NOMBRE DEL JUGADOR 1 (INGRESE 0 PARA VOLVER ATRAS):\n')
    # si es zero, sale
    if confirmer(p1):
      return False
    p2 = input('INGRESE EL NOMBRE DEL JUGADOR 2 (INGRESE 0 PARA VOLVER ATRAS):\n')
    # si es zero, sale
    if confirmer(p2):
      return False
    return True

# No tiene contenido
def highscore():
  print('EN CONSTRUCCION')
  menu = '1. REGRESAR'
  if select(menu, 1, 1) == 1:
      return True
