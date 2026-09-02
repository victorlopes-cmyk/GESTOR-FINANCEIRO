import json
from transacao import Transacao

class GerenciadorTransacoes:
    def __init__(self):
        self.transacoes = []
        self.carregar_dados()

    def salvar_dados(self):
        lista_dados = []
        for t in self.transacoes:
            dicionario = {
                "descricao": t.descricao,
                "valor": t.valor,
                "tipo": t.tipo,
                "categoria": t.categoria
            }
            lista_dados.append(dicionario)
        with open("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista_dados, arquivo, indent=4, ensure_ascii=False)

    def carregar_dados(self):
        try:
            with open("dados.json", "r", encoding="utf-8") as arquivo:
                lista_dados = json.load(arquivo)
                for item in lista_dados:
                    nova_t = Transacao(item["descricao"], item["valor"], item["tipo"], item["categoria"])
                    self.transacoes.append(nova_t)
        except FileNotFoundError:
            pass

    def adicionar_transacao(self, nova_transacao):
        self.transacoes.append(nova_transacao)

    def calcular_saldo(self):
        saldo = 0
        for transacao in self.transacoes:
            if transacao.tipo == "receita":
                saldo += transacao.valor
            elif transacao.tipo == "despesa":
                saldo -= transacao.valor
        return saldo
    def listar_transacoes(self):
        # Primeiro, verificamos se a lista está vazia
        if len(self.transacoes) == 0:
            print("\nNenhuma transação cadastrada ainda.")
            return # O 'return' vazio faz o método parar por aqui

        print("\n=== EXTRATO DE TRANSAÇÕES ===")
        
        # Fazemos um loop para imprimir cada transação formatada
        for t in self.transacoes:
            # O .upper() deixa o texto em MAIÚSCULO (ex: RECEITA ou DESPESA)
            # O :.2f garante que o valor fique com duas casas (ex: 150.00)
            print(f"[{t.tipo.upper()}] {t.descricao} | {t.categoria} | R$ {t.valor:.2f}")
            
        print("=============================")
