from modelAdmin import ModelAdmin
from modelProfessor import ModelProfessor



class Login():
    def __init__(self):
        self.admin = ModelAdmin()
        self.professor = ModelProfessor()

    def login(self, data):
        usuario = self.admin.search(data["usuario"])
        if usuario != None:
            if usuario[0][4] == data["senha"]:
                return ["Deu Boa!", {"id": usuario[0][0], "usuario": usuario[0][3], "admin": True }]
            else:
                return ["Senha incorreta!", None]
            
        else:    
            usuario = self.professor.search(data["usuario"])
            if usuario != None:
                if usuario[0][4] == data["senha"]:
                    return ["Deu Boa!", {"id": usuario[0][0], "usuario": usuario[0][3], "admin": False }]
                else:
                    return ["Senha incorreta!", None]

        return ["Usuario não existe!", None]




        


    