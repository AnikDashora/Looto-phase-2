import mysql.connector
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)


class sql_connection:
    def __init__(self):
        # Read environment variables
        self._host = "localhost"
        self._user = "root"
        self._password = "root"
        self._database = "looto"

        if not all([self._host, self._user, self._password, self._database]):
            raise ValueError("Database configuration is missing in the .env file.")

        # Establish connection
        self.connection = mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=self._database
        )
        self.cursor = self.connection.cursor()

    # Optionally, you can add methods for closing the connection
    def close(self):
        self.cursor.close()
        self.connection.close()