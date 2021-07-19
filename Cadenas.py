#Aca estan las funciones que formatean los characteres y confirman que son validos
def confirmer(value, start = 0, end = 0):
  #Confirma el valor es un digito y en rango 
  #Esto se utiliza para regresar cuando presionas 0
  return value.isdigit() and start <= int(value) <= end

#Selecion repite el loop hasta que
#el usuario da un valor valido
def select(menu, start, end): 
  menu = ('\n').join(menu.split(', '))
  while True:
    print(menu)
    inp = input('Selecione opcion: '.upper()).strip(' ')
    #uso de confirmer para conseguir valor valido
    if confirmer(inp, start, end):
      return int(inp)
    else:
      print('OPCION INCORRECTA. INTENTE DE NUEVO.')

#Imprime el tablero del jugadeor
def board_print(player):
  #Aca se crea una lista usando comprehnsion
  disp = [str(x[0]) + ' ' + str(x[1]) + ' ' + (' '*(20 - len(x[0]) - len(x[1]) - 1)) for x in player[2]]
  #Usando join, se puede imprimr una lista sin usar for loops
  print(f"|  {'|  '.join(disp[0:3])}|")
  print(f"|  {'|  '.join(disp[3:6])}|")
  print(f"{(20*3)//2 * ' '}|{' '.join(player[1])}|")