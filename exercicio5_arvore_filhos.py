def encontrar_filhos(raiz, valor):
    if (nó := _encontrar_filhos(raiz, valor)):
        saida = []
        pre_ordem(nó, saida)
        return saida[1:]  


def _encontrar_filhos(nó, valor):
    if not nó:
        return None

    if nó.valor == valor:
        return nó

    return _encontrar_filhos(nó.esquerda, valor) or _encontrar_filhos(nó.direita, valor)


def pre_ordem(nó, saida):
    if not nó:
        return

    saida.append(nó.valor)
    pre_ordem(nó.esquerda, saida)
    pre_ordem(nó.direita, saida)

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def adicionar(self, valor):
        self.raiz = self._adicionar(valor, self.raiz)

    def _adicionar(self, valor, nó):
        if nó is None:
            return No(valor)

        if valor <= nó.valor:
            nó.esquerda = self._adicionar(valor, nó.esquerda)
        else:
            nó.direita = self._adicionar(valor, nó.direita)
        return nó

# Testando a função
arvore = ArvoreBinaria()
arvore.adicionar(50)
arvore.adicionar(70)
arvore.adicionar(35)
arvore.adicionar(22)
arvore.adicionar(21)
arvore.adicionar(23)
arvore.adicionar(36)
arvore.adicionar(37)

filhos = encontrar_filhos(arvore.raiz, 50)
print("Filhos de 50:", filhos)  
