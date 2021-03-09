from modelTreino import ModelTreino

class Treino():
    def __init__(self):
        self.treino = ModelTreino()
    
    def cadastrar(self, data):

        self.treino.insert(data["alunoId"], data["professorId"], data["texto"])
    
    def procurar(self, data):
        result = self.treino.search(data["alunoId"], data["professorId"])
        
        if result != None:
            data = {"id": result[0][0], "texto": result[0][3]}

            return data
        
        return None

    def atualizar(self, data):
        self.treino.update(data["treinoId"], data["texto"])