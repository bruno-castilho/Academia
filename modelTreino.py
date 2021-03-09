from db import Connection

class ModelTreino(Connection):
    def __init__(self):
        Connection.__init__(self)
    
    def insert(self, *args):
        try:
            sql = "INSERT INTO treino (aluno_id, professor_id, descricao) VALUES (%s,%s,%s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao inserir", e)

    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM treino WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado"
            sql_d = f"DELETE FROM treino WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
        except Exception as e:
            print("Erro ao deletar", e)

    def update(self, id, *args):
        try:
            sql = f"UPDATE treino SET descricao = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao atualizar", e)

    def search(self, *args):
        try:
            sql = "SELECT * FROM treino WHERE  aluno_id = %s and professor_id = %s"
            data = self.query(sql, args)
            if data:
                return data
            return None

        except Exception as e:
            print("Erro ao procurar", e)



