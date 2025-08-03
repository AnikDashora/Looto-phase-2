import pymysql

class SqlConnection:

    def __init__(self,charset='utf8mb4'):
        self.host = "localhost"
        self.user = "root"
        self.password = "root"
        self.database = "looto"
        self.charset = charset
        self.connection = None
    
    