import mysql.connector
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from database.database_connection import sql_connection


class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self._password = password
        self._user_table_name = "users"
        self._db = sql_connection()
    
    def create_uid(self,uid):
        """
        Converts a numeric uid into a string id with prefix 'u' and leading zeros.
        Example: 7 -> 'u0007', 12345 -> 'u12345'
        """
        if(isinstance(uid,str)):
            raise ValueError
        id_len = 4
        if(len(str(uid)) <= 4):
            prefix_len = id_len - len(str(uid))
            return "u"+"0"*prefix_len+str(uid)
        else:
            return "u"+str(uid)

    def generate_id(self):
        sql_query = f"SELECT COUNT(*) FROM {self._user_table_name}"
        try:
            self._db.cursor.execute(sql_query)
            row_count = self._db.cursor.fetchone()[0]  # fetchone returns a tuple
            return self.create_uid(row_count+1)
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
    
    def encrypt_password(self):
        """
            Encrypts the password by inserting it into the local part of the email and transforming 
            each character using the formula: x^2 + 5x + 10, where x is the ASCII value of the character.
            
            Returns:
                str: The encrypted password as a concatenated string of transformed character codes.
            
            Raises:
                ValueError: If the email format is invalid (doesn't contain '@').
            """
        try:
            local, domain = self.email.split("@")
            del domain
        except ValueError:
            raise ValueError("Invalid email format")

        half_local_len = max(len(local) // 2 - 1, 0)
        new_password = local[:half_local_len] + self._password + local[half_local_len:]
        encrypted_chars = [str((ord(c) ** 2) + (ord(c) * 5) + 10) for c in new_password]
        encrypted_password = ''.join(encrypted_chars)
        return encrypted_password

    def save_user_data(self):
        """
            Saves the user data into the database table specified by self._user_table_name.
            User ID is generated dynamically, and password is encrypted before storage.

            Returns:
                bool: True if the user data was saved successfully, False otherwise.
        """
        sql_query = f"""
            insert into {self._user_table_name}
            (user_id,username,email,password)
            values
            (%s,%s,%s,%s)
        """
        sql_data = (
            self.generate_id(),
            self.name,
            self.email,
            self.encrypt_password(),
        )
        try:
           self._db.cursor.execute(sql_query,sql_data)
           self._db.connection.commit()
           return True
        except Exception as e:
            print(f"Error executing query: {e}") 
            if self._db.connection.is_connected():
                self._db.connection.rollback()
            return False

    def verify_user(self):
        """
            Verifies if a user exists with the given email and matching encrypted password.

            Returns:
                bool: True if user exists and password matches, False otherwise.
        """
        sql_query = f"""
            SELECT * FROM {self._user_table_name}
            WHERE email = %s
        """
        sql_data = (self.email,)

        try:
            self._db.cursor.execute(sql_query, sql_data)
            user_record = self._db.cursor.fetchone()

            if user_record is None:
                return False

            stored_encrypted_password = user_record[3]
            return self.encrypt_password() == stored_encrypted_password
        except Exception as e:
            print(f"Error executing query: {e}")
            return False


