class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self) -> None:
        self.raiz = None

    def adicionar(self, valor):
        novo_no = self._adicionar(valor, self.raiz)
        if not self.raiz:
            self.raiz = novo_no

    def _adicionar(self, valor, no):
        if no is None:
            return No(valor)

        if valor <= no.valor:
            no.esquerda = self._adicionar(valor, no.esquerda)
        else:
            no.direita = self._adicionar(valor, no.direita)
        return no

    def em_ordem(self):
        print("Em ordem:", end=" ")
        self._em_ordem(self.raiz)
        print()

    def _em_ordem(self, no):
        if no is None:
            return

        self._em_ordem(no.esquerda)
        print(no.valor, end=" ")
        self._em_ordem(no.direita)

    def pre_ordem(self):
        print("Pré ordem:", end=" ")
        self._pre_ordem(self.raiz)
        print()

    def _pre_ordem(self, no):
        if no is None:
            return

        print(no.valor, end=" ")
        self._pre_ordem(no.esquerda)
        self._pre_ordem(no.direita)

arvore = ArvoreBinaria()
arvore.adicionar(50)
arvore.adicionar(70)
arvore.adicionar(35)
arvore.adicionar(22)
arvore.adicionar(21)
arvore.adicionar(23)
arvore.adicionar(36)
arvore.adicionar(37)

arvore.pre_ordem()
arvore.em_ordem()
