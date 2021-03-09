import psycopg2 as db

class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "postgres",
                "password": "123456789",
                "host": "localhost",
                "port": "5432",
                "database": "academia"
            }
        }

class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Erro na conexão", e)
            exit(1)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val1, exc_tb):
        self.commit()
        self.connection.close()
    
    @property
    def connection(self):
        return self.conn
    
    @property
    def cursor(self):
        return self.cur
    
    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()
    
    def execute(self, sql, params=None):
        if params == None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, params)

    def query(self, sql, params=None):
        if params == None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, params)
        return self.fetchall()

