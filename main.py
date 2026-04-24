class Produto:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class SistemaLogistica:
    def __init__(self):
        self.estoque = []      # Lista para busca binária
        self.pedidos = []      # Fila (FIFO)
        self.devoluções = []   # Pilha (LIFO)

    def adicionar_produto(self, produto):
        self.estoque.append(produto)
        n = len(self.estoque)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.estoque[j].id > self.estoque[j+1].id:
                    self.estoque[j], self.estoque[j+1] = self.estoque[j+1], self.estoque[j]
        print(f"Produto {produto.nome} adicionado e estoque organizado!")

    def buscar_produto(self, id_alvo):
        # TODO: Implemente a Busca Binária aqui para encontrar o nome do produto pelo ID
        inicio = 0
        fim = len(self.estoque) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if self.estoque[meio].id == id_alvo:
                return self.estoque[meio].nome
            elif self.estoque[meio].id < id_alvo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return "Não encontrado"

    def novo_pedido(self, cliente):
        # TODO: Adicione o cliente na FILA de pedidos
        self.pedidos.append(cliente)

    def processar_proximo_pedido(self):
        if self.pedidos:
            # TODO: Remova o PRIMEIRO cliente da fila (O "arreda-arreda" lento, mas funcional)
            cliente = self.pedidos.pop(0)
            print(f"Processando pedido de: {cliente}")
        else:
            print("Nenhum pedido na fila.")

# --- TESTANDO O SISTEMA ---
logistica = SistemaLogistica()
logistica.adicionar_produto(Produto(302, "Celular"))
logistica.adicionar_produto(Produto(101, "Fone de Ouvido"))
logistica.adicionar_produto(Produto(205, "Carregador"))

print(f"Produto 101: {logistica.buscar_produto(101)}")
logistica.novo_pedido("Ivano")
logistica.novo_pedido("Maria")
logistica.processar_proximo_pedido() 