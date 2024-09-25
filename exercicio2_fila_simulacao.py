class Fila:
    def __init__(self) -> None:
        self.itens = []  
        
    def adicionar(self, valor):
        self.itens.append(valor) 

    def remover(self):
        if self.itens:  
            primeiro_item = self.itens[0]  
            del self.itens[0]  
            return primeiro_item  

    def esta_vazia(self):
        return len(self.itens) == 0  

fila = Fila()
fila.adicionar(1)
fila.adicionar(2)
fila.adicionar(3)

print(fila.remover())  
print(fila.remover())  
print(fila.remover())  
print(fila.remover())  