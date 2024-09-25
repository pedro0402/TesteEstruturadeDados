class PilhaPy:
    def __init__(self):
        self.vetor = []

    def empilhar_e_inverter(self, valor):
        if isinstance(valor, str):
            valor = valor[::-1]
        self.vetor.append(valor)
        return valor

if __name__ == "__main__":
    pilha = PilhaPy()
  
    print(pilha.empilhar_e_inverter("Hello"))

    