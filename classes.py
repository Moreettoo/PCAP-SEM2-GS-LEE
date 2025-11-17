import json

class Competencia:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Perfil:
    def __init__(self, nome, competencias):
        self.nome = nome
        self.competencias = competencias

class Carreira:
    def __init__(self, nome, competencias_necessarias):
        self.nome = nome
        self.competencias_necessarias = competencias_necessarias 