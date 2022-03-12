
class class_produto:
    def __init__(self, id=int, nome_produto=str, descricao=str, valor=float, quantidade=int):
        self.id = id
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.valor = valor 
        self.quantidade = quantidade

    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

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

     