class Transacao:
    def __init__(self, descricao, valor, tipo, categoria):
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo
        self.categoria = categoria

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        if not isinstance(novo_valor, (int, float)):
            raise TypeError("o valor precisa ser maior que zero (int ou float)")
        if novo_valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")
        self._valor = float(novo_valor)
