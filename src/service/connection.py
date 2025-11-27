import psycopg2
from customTypes import ConexaoInterface

class Conexao(ConexaoInterface):
    conn: psycopg2.extensions.connection = None

    def __init__(self, connection: psycopg2.extensions.connection = None):
        if not self.conn and connection:
            self.conn = connection
    
    def get_connection(self) -> psycopg2.extensions.connection:
        return self.conn
    
    def close_connection(self) -> None:
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute_query(self, query: str, params: tuple = ()) -> list:
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
            self.conn.commit()
            return []
