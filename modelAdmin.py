from db import Connection

class ModelAdmin(Connection):
    def __init__(self):
        Connection.__init__(self)
    
    def insert(self, *args):
        try:
            sql = "INSERT INTO admin (nome, email, usuario, senha) VALUES (%s,%s,%s,%s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao inserir", e)

    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM admin WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado"
            sql_d = f"DELETE FROM admin WHERE ID = {id}"
            self.execute(sql_d)
            self.commit()
        except Exception as e:
            print("Erro ao deletar", e)

    def update(self, id, *args):
        try:
            sql = f"UPDATE admin SET nome = %s, email = %s, usuario = %s, senha = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao atualizar", e)

    def search(self, *args, type_s="usuario"):
        try:
            sql = f"SELECT * FROM admin WHERE {type_s} LIKE %s"
            if type_s == "id":
                sql = "SELECT * FROM admin WHERE id = %s"
            data = self.query(sql, args)
            if data:
                return data
            return None

        except Exception as e:
            print("Erro ao procurar", e)

    def selectAll(self):
        try:
            sql = f"SELECT * FROM admin"

            return self.query(sql)
        except Exception as e:
            print("Erro ao procurar", e)

    def filter(self, fil):
        try:
            sql = f"SELECT * FROM admin WHERE usuario LIKE '%{fil}%' or nome LIKE '%{fil}%' or email LIKE '%{fil}%'"
            data = self.query(sql)
            if data:
                return data
            return None

        except Exception as e:
            print("Erro ao procurar", e)

