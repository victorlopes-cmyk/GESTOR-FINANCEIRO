from transacao import Transacao
from gerenciador import GerenciadorTransacoes

def iniciar_sistema():
    caixa = GerenciadorTransacoes()
    while True:
        print("\n=== GESTOR FINANCEIRO ===")
        print("1. Adicionar nova transação")
        print("2. Ver Saldo Atual")
        print("3. Ver Extrato de Transações")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("\n-- Nova Transação --")
            descricao = input("Descrição (ex: Aluguel, Salário): ")
            while True:
                try:
                    valor_texto = input("Digite o valor( ex: 1500.00): ")
                    valor = float(valor_texto)
                    break
                except ValueError:
                    print("Valor inválido. Tente novamente.")

            tipo = input("Digite o tipo (receita ou despesa): ").lower()
            categoria = input(" Categoria( ex: alimentação, transporte, lazer): ")
            nova_t = Transacao(descricao, valor, tipo, categoria)
            caixa.adicionar_transacao(nova_t)
            caixa.salvar_dados()
            print("Transação adicionada e salva com sucesso!")

        elif opcao == "2":
            saldo_atual = caixa.calcular_saldo()
            print(f"Saldo atual: R$ {saldo_atual:.2f}")

        elif opcao == "3":
            caixa.listar_transacoes()

        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()