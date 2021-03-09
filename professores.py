from modelProfessor import ModelProfessor
from datetime import date
from modelAdmin import ModelAdmin
from modelAluno import ModelAluno
from modelMatricula import ModelMatricula



class Professores():
    def __init__(self):
        self.admin = ModelAdmin()
        self.professor = ModelProfessor()
        self.aluno = ModelAluno()
        self.matricula = ModelMatricula()
    
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

        atuacoes = []
        for atuacao in data["atuacoes"]:
            if data["atuacoes"][atuacao] == 1:
                atuacoes.append(atuacao)


        self.professor.insert(
                    data["nome"],
                    data["email"],
                    data["usuario"], 
                    data["senha"],
                    data["nascimento"],
                    atuacoes
                    )

        return "Professor cadastrado com sucesso!"
    
    def editar(self, id, data):
        for key in data:
            if(data[key] == ""):
                return f'Digite todo os campos!'

        if(data["senha"] != data["repetirsenha"]):
            return "A senhas não conferem!"


        usuario = self.professor.search(id, type_s="id")

        if data["usuario"] != usuario[0][3]:
            if(self.admin.search(data["usuario"]) != None or self.professor.search(data["usuario"]) != None):
                return "Usuário já existe!"

        if data["email"] != usuario[0][2]:
            if(self.admin.search(data["email"], type_s="email") != None or self.professor.search(data["email"], type_s="email") != None):
                return "E-mail já cadastrado!"

        atuacoes = []

        for atuacao in data["atuacoes"]:
            if data["atuacoes"][atuacao] == 1:
                atuacoes.append(atuacao)
        

        self.professor.update(
            id,
            data["nome"],
            data["email"],
            data["usuario"], 
            data["senha"],
            data["nascimento"],
            atuacoes
        )

        return "Professor editado com sucesso!"

    def listaProfessores(self):
        results = self.professor.selectAll()
        professores = []

        for result in results:
            today = date.today()

            birthDate = result[5].split("/")

            age = int(today.strftime("%Y")) - int(birthDate[2])
            
            month = int(today.strftime("%m")) - int(birthDate[1])

            if (month < 0) or ((month == 0) and (int(today.strftime("%d")) < int(birthDate[0]))): 
                age-= 1
            professores.append({
                "id":result[0],
                "nome":result[1],
                "email":result[2],
                "usuario":result[3],
                "idade": age,
                "atuacao": result[6]
            })
        
        return professores

    def professorId(self, id):
        result = self.professor.search(id, type_s="id")

        
        atuacoes = {
            "Natação": 0,
            "Dança": 0,
            "Yoga": 0,
            "Musculação": 0,
            "Crossfit": 0,
            "Muay Thai": 0,
            "Jiu Jitsu": 0,
            "Boxe": 0
        }

        for atuacao in result[0][6]:
            atuacoes[atuacao] = 1

        today = date.today()

        nascimento = result[0][5].split("/")

        age = int(today.strftime("%Y")) - int(nascimento[2])
            
        month = int(today.strftime("%m")) - int(nascimento[1])

        if (month < 0) or ((month == 0) and (int(today.strftime("%d")) < int(nascimento[0]))): 
            age-= 1
        
        professor = {
            "id": result[0][0],
            "nome": result[0][1],
            "email": result[0][2],
            "usuario": result[0][3],
            "senha": result[0][4],
            "nascimento":{
                "dia": int(nascimento[0]),
                "mes": int(nascimento[1]),
                "ano": int(nascimento[2])
            },
            "idade": age,
            "atuacoes": atuacoes
        }
        return professor
    
    def deletar(self, id):
        self.professor.delete(id)

    def filtrar(self, filtro):
        results = self.professor.filter(filtro)
        professores = []
        if results != None:
            for result in results:
                professores.append({
                    "id":result[0],
                    "nome":result[1],
                    "email":result[2],
                    "usuario":result[3],
                    "idade": 24,
                    "atuacao": result[6]
                })
        
        return professores

    def alunos(self, id):
        matriculas = self.matricula.search(id, type_s="professor_id")

        alunos = []
        if matriculas != None:
            for matricula in matriculas:
                if not matricula[3] in alunos:
                    aluno = self.aluno.search(matricula[3], type_s="id")


                    today = date.today()

                    nascimento = aluno[0][3].split("/")

                    age = int(today.strftime("%Y")) - int(nascimento[2])
                        
                    month = int(today.strftime("%m")) - int(nascimento[1])

                    if (month < 0) or ((month == 0) and (int(today.strftime("%d")) < int(nascimento[0]))): 
                        age-= 1

                    alunos.append({
                        "id": aluno[0][0],
                        "nome": aluno[0][1],
                        "email": aluno[0][2],
                        "idade": age,
                        "altura": aluno[0][4],
                        "peso": aluno[0][5],

                    })
        
        return alunos
                    


        

