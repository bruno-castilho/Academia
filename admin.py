from modelAdmin import ModelAdmin
from modelProfessor import ModelProfessor
from modelAluno import ModelAluno

class Admin():
    def __init__(self):
        self.admin = ModelAdmin()
        self.professor = ModelProfessor()
        self.aluno = ModelAluno()
    
    def cadastrar(self, data):
        for key in data:
            if(data[key] == ""):
                return f'Digite todo os campos!'

        if(data["senha"] != data["repetirsenha"]):
            return "A senhas não conferem!"
    
        if(self.admin.search(data["usuario"]) != None or self.professor.search(data["usuario"]) != None):
            return "Usuário já existe!"


        if(self.admin.search(data["email"], type_s="email") != None or self.professor.search(data["email"], type_s="email") != None):
            return "E-mail já cadastrado!"
        
        
        self.admin.insert(
                    data["nome"],
                    data["email"],
                    data["usuario"], 
                    data["senha"],
                    )

        return "Admin cadastrado com sucesso!"
    
    def editar(self, id, data):
        for key in data:
            if(data[key] == ""):
                return f'Digite todo os campos!'

        if(data["senha"] != data["repetirsenha"]):
            return "A senhas não conferem!"


        usuario = self.admin.search(id, type_s="id")
        if data["usuario"] != usuario[0][3]:
            if(self.admin.search(data["usuario"]) != None or self.professor.search(data["usuario"]) != None):
                return "Usuário já existe!"

        if data["email"] != usuario[0][2]:
            if(self.admin.search(data["email"], type_s="email") != None or self.professor.search(data["email"], type_s="email") != None):
                return "E-mail já cadastrado!"
        

        self.admin.update(
            id,
            data["nome"],
            data["email"],
            data["usuario"],
            data["senha"]
        )

        return "Admin editado com sucesso!"

    def listaAdmins(self):
        results = self.admin.selectAll()
        admins = []

        for result in results:
            admins.append({
                "id":result[0],
                "nome":result[1],
                "email":result[2],
                "usuario":result[3]
            })
        
        return admins

    def adminId(self, id):

        result = self.admin.search(id, type_s="id")
        admin = {
            "id": result[0][0],
            "nome": result[0][1],
            "email": result[0][2],
            "usuario": result[0][3],
            "senha": result[0][4],
        }
        return admin
    
    def deletar(self, id):
        self.admin.delete(id)

    def filtrar(self, filtro):
        results = self.admin.filter(filtro)
        admins = []
        if results != None:
            for result in results:
                admins.append({
                    "id":result[0],
                    "nome":result[1],
                    "email":result[2],
                    "usuario":result[3]
                })
        
        return admins
