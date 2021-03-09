from db import Connection

class ModelMatricula(Connection):
    def __init__(self):
        Connection.__init__(self)
    
    def insert(self, *args):
        try:
            sql = "INSERT INTO matricula (esporte, professor_id, aluno_id) VALUES (%s,%s,%s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao inserir", e)

    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM matricula WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado"
            sql_d = f"DELETE FROM matricula WHERE ID = {id}"
            self.execute(sql_d)
            self.commit()
        except Exception as e:
            print("Erro ao deletar", e)

    def update(self, id, *args):
        try:
            sql = f"UPDATE matricula SET professor_id = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao atualizar", e)

    def search(self, *args, type_s="usuario"):
        try:
            sql = f"SELECT * FROM matricula WHERE {type_s} = %s"
            if type_s == "id":
                sql = "SELECT * FROM matricula WHERE id = %s"
            data = self.query(sql, args)
            if data:
                return data
            return None

        except Exception as e:
            print("Erro ao procurar", e)

    def selectAll(self):
        try:
            sql = f"SELECT * FROM matricula"

            return self.query(sql)
        except Exception as e:
            print("Erro ao procurar", e)

