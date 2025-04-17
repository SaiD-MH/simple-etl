import mysql.connector

class DatabaseConnection:
    def create_connection(self):  # Added self
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysqlabg",
            database="simple_etl"
        )

    def write_dictList_to_database(self, dictList):
        """
        Take list of dicts and write to MySQL database
        """
        try:
            mydb = self.create_connection()
            mycursor = mydb.cursor()

            for record in dictList:
                sql_statement = '''
                    INSERT INTO rating_details 
                    (username, user_age, user_country, movie_title, movie_genre, rating) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                '''
                values = (
                    record['username'],
                    record['user_age'],
                    record['user_country'],
                    record['movie_title'],
                    record['movie_genre'],
                    record['rating']
                )
                mycursor.execute(sql_statement, values)

            mydb.commit()
        except Exception as e:
            print("Error writing to the database:", e)
        finally:
            if mycursor:
                mycursor.close()
            if mydb:
                mydb.close()
