class Produto:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class SistemaLogistica:
    def __init__(self):
        self.estoque = []      # Lista para busca binária
        self.pedidos = []      # Fila (FIFO)
        self.devolucoes = []   # Pilha (LIFO)

    def adicionar_produto(self, produto):
        self.estoque.append(produto)
        n = len(self.estoque)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.estoque[j].id > self.estoque[j+1].id:
                    self.estoque[j], self.estoque[j+1] = self.estoque[j+1], self.estoque[j]
        print(f"Produto {produto.nome} adicionado e estoque organizado!")

    def buscar_produto(self, id_alvo):
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
        self.pedidos.append(cliente)

    def processar_proximo_pedido(self):
        if self.pedidos:
            cliente = self.pedidos.pop(0)
            print(f"Processando pedido de: {cliente}")
        else:
            print("Nenhum pedido na fila.")

    def registrar_devolucao(self, item):
        self.devolucoes.append(item)

    def conferir_devolucao(self):
        if self.devolucoes:
            item = self.devolucoes.pop()
            print(f"Conferindo {item} para retorno ao estoque.")
        else:
            print(f"Nenhuama devolução na pilha.")

# --- TESTANDO O SISTEMA ---
logistica = SistemaLogistica()
logistica.adicionar_produto(Produto(302, "Celular"))
logistica.adicionar_produto(Produto(101, "Fone de Ouvido"))
logistica.adicionar_produto(Produto(205, "Carregador"))

print(f"Produto 101: {logistica.buscar_produto(101)}")
logistica.novo_pedido("Ivano")
logistica.novo_pedido("Maria")
logistica.processar_proximo_pedido() 

logistica.registrar_devolucao("Teclado Quebrado")
logistica.registrar_devolucao("Cabo com Mau Contato")
logistica.conferir_devolucao()