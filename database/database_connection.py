import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into environment

class sql_connection:
    def __init__(self):
        # Read environment variables
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_NAME')

        if not all([self.host, self.user, self.password, self.database]):
            raise ValueError("Database configuration is missing in the .env file.")

        # Establish connection
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    # Optionally, you can add methods for closing the connection
    def close(self):
        self.cursor.close()
        self.connection.close()