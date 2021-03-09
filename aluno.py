from datetime import date
from modelAdmin import ModelAdmin
from modelProfessor import ModelProfessor
from modelAluno import ModelAluno
from modelMatricula import ModelMatricula



class Aluno():
    def __init__(self):
        self.admin = ModelAdmin()
        self.professor = ModelProfessor()
        self.aluno = ModelAluno()
        self.matricula = ModelMatricula()
    
    def cadastrar(self, data):

        for key in data["inputs"]:
            if(data["inputs"][key] == ""):
                return 'Digite todo os campos!'
        
        if(self.admin.search(data["inputs"]["email"], type_s="email") != None or self.professor.search(data["inputs"]["email"], type_s="email") != None or self.aluno.search(data["inputs"]["email"], type_s="email") != None):
            return "E-mail já cadastrado!"

        try:
            aluno_id = self.aluno.insert(
                                data["inputs"]["nome"],
                                data["inputs"]["email"],
                                data["inputs"]["nascimento"], 
                                float(data["inputs"]["altura"]),
                                float(data["inputs"]["peso"]),
                        )
        except:
            return 'Digite um numero nos campos "peso" e "altura"'

        
        for esporte in data["matriculas"]:
            if(data["matriculas"][esporte] == 1):    
                try: 
                    self.matricula.insert(esporte, data["idsProfessores"][data["professores"][esporte]], aluno_id[0])
                except:
                    self.matricula.insert(esporte, None, aluno_id[0])


        return "Aluno cadastrado com sucesso"
    
    def editar(self, id, data):
        for key in data["inputs"]:
            if(data["inputs"][key] == ""):
                return 'Digite todo os campos!'
            
        
        aluno = self.aluno.search(id, type_s="id")
        
        if data["inputs"]["email"] != aluno[0][2]:     
            if(self.admin.search(data["inputs"]["email"], type_s="email") != None or self.professor.search(data["inputs"]["email"], type_s="email") != None or self.aluno.search(data["inputs"]["email"], type_s="email") != None):
                return "E-mail já cadastrado!"



        matriculas = self.matricula.search(id, type_s="aluno_id")

        if matriculas != None:
            for matricula in matriculas:
                if data["matriculas"][matricula[1]] == 0:
                    self.matricula.delete(matricula[0])
                else:
                    data["matriculas"][matricula[1]] = 0
                    try:
                        self.matricula.update(matricula[0], data["idsProfessores"][data["professores"][matricula[1]]])
                    except:
                        self.matricula.update(matricula[0], None)


        for esporte in data["matriculas"]:
            if(data["matriculas"][esporte] == 1):    
                try: 
                    self.matricula.insert(esporte, data["idsProfessores"][data["professores"][esporte]], id)
                except:
                    self.matricula.insert(esporte, None, id)

        try:
            self.aluno.update(
                id,
                data["inputs"]["nome"],
                data["inputs"]["email"],
                data["inputs"]["nascimento"], 
                float(data["inputs"]["altura"]),
                float(data["inputs"]["peso"])
            )
        except:
            return 'Digite um numero nos campos "peso" e "altura"'



        return "Aluno editado com sucesso!"

    def listaAlunos(self):
        results = self.aluno.selectAll()
        alunos = []



        for result in results:
            today = date.today()

            birthDate = result[3].split("/")

            age = int(today.strftime("%Y")) - int(birthDate[2])
            
            month = int(today.strftime("%m")) - int(birthDate[1])

            if (month < 0) or ((month == 0) and (int(today.strftime("%d")) < int(birthDate[0]))): 
                age-= 1

            alunos.append({
                "id":result[0],
                "nome":result[1],
                "email":result[2],
                "altura":result[4],
                "peso":result[5],
                "idade": age
            })
        
        return alunos

    def alunoId(self, id):

        result = self.aluno.search(id, type_s="id")

        matriculas = self.matricula.search(id, type_s="aluno_id")

        esportes = {
            "Natação": 0,
            "Dança": 0,
            "Yoga": 0,
            "Musculação": 0,
            "Crossfit": 0,
            "Muay Thai": 0,
            "Jiu Jitsu": 0,
            "Boxe": 0
        }

        professores = {
            "Natação": "",
            "Dança": "",
            "Yoga": "",
            "Musculação": "",
            "Crossfit": "",
            "Muay Thai": "",
            "Jiu Jitsu": "",
            "Boxe": ""
        }

        if matriculas != None:
            for matricula in matriculas:
                esportes[matricula[1]] = 1
                professor = self.professor.search(matricula[2], type_s="id")
                if professor != None:
                    professores[matricula[1]] = professor[0][1]
            

        nascimento = result[0][3].split("/")

        aluno = {
            "id": result[0][0],
            "nome": result[0][1],
            "email": result[0][2],
            "altura": result[0][4],
            "peso": result[0][5],
            "nascimento":{
                "dia": int(nascimento[0]),
                "mes": int(nascimento[1]),
                "ano": int(nascimento[2])
            },
            "matriculas": esportes,
            "professores": professores
        }
        return aluno
    
    def deletar(self, id):
        matriculas = self.matricula.search(id, type_s="aluno_id")

        if matriculas != None:
            for matricula in matriculas:
                self.matricula.delete(matricula[0])


        self.aluno.delete(id)

    def filtrar(self, filtro):
        results = self.aluno.filter(filtro)
        alunos = []
        if results != None:
            for result in results:
                today = date.today()

                birthDate = result[3].split("/")

                age = int(today.strftime("%Y")) - int(birthDate[2])
                
                month = int(today.strftime("%m")) - int(birthDate[1])

                if (month < 0) or ((month == 0) and (int(today.strftime("%d")) < int(birthDate[0]))): 
                    age-= 1
                alunos.append({
                    "id":result[0],
                    "nome":result[1],
                    "email":result[2],
                    "altura":result[4],
                    "peso": result[5],
                    "idade": age
                })
        
        return alunos

    def professoresAtuacoes(self):
        atuacoes = {
            "Natação":[],
            "Dança":[],
            "Yoga":[], 
            "Musculação":[], 
            "Crossfit": [], 
            "Muay Thai": [],
            "Jiu Jitsu": [],
            "Boxe": [],
            "ids": {}
            }

        professores = self.professor.selectAll()

        for atuacao in atuacoes:
            for professor in professores:
                if atuacao in professor[6]:
                    atuacoes[atuacao].append(professor[1])
        
        for professor in professores:
            atuacoes["ids"][professor[1]] = professor[0]
                    



        return atuacoes

