from db import Connection

class ModelAluno(Connection):
    def __init__(self):
        Connection.__init__(self)
    
    def insert(self, *args):
        try:
            sql = "INSERT INTO aluno (nome, email, nascimento, altura, peso) VALUES (%s,%s,%s,%s,%s) RETURNING id"
            id = self.query(sql, args)
            self.commit()
            return id       
        except Exception as e:
            print("Erro ao inserir", e)

    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM aluno WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado"
            sql_d = f"DELETE FROM aluno WHERE ID = {id}"
            self.execute(sql_d)
            self.commit()
        except Exception as e:
            print("Erro ao deletar", e)

    def update(self, id, *args):
        try:
            sql = f"UPDATE aluno SET nome = %s, email = %s, nascimento = %s, altura = %s, peso = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao atualizar", e)

    def search(self, *args, type_s="usuario"):
        try:
            sql = f"SELECT * FROM aluno WHERE {type_s} LIKE %s"
            if type_s == "id":
                sql = "SELECT * FROM aluno WHERE id = %s"
            data = self.query(sql, args)
            if data:
                return data
            return None

        except Exception as e:
            print("Erro ao procurar", e)

    def selectAll(self):
        try:
            sql = f"SELECT * FROM aluno"

            return self.query(sql)
        except Exception as e:
            print("Erro ao procurar", e)

    def filter(self, fil):
        try:
            sql = f"SELECT * FROM aluno WHERE nome LIKE '%{fil}%' or email LIKE '%{fil}%'"
            data = self.query(sql)
            if data:
                return data
            return None

        except Exception as e:
            print("Erro ao procurar", e)
