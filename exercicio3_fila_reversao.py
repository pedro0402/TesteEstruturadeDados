def inverter_fila(fila):
  fila_invertida = []
  while fila:
    fila_invertida.append(fila.pop())
  return fila_invertida


print(inverter_fila([1,2,3,4]))