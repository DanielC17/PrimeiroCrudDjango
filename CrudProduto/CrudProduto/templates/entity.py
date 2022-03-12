
class produto:
    def __init__(self, id, nome_produto, descriacao, valor, quantidade):
        set.id = id 
        set.nome_produto = nome_produto
        set.descriacao = descriacao
        set.valor = valor 
        set.quantidade = quantidade

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_nome_produto(self, nome_produto):
        self.nome_produto = nome_produto

    def get_nome_produto(self):
        return self.nome_produto

    def set_descricao(self, descriacao):
        self.descriacao = descriacao

    def get_descricao(self):
        return self.descriacao

    def set_valor(self, valor):
        self.valor = valor 

    def get_valor(self):
        return self.valor

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade

    def get_quantidade(self):
        return self.quantidade

    