from src.service.connection import Conexao
import psycopg2

class ConnectionFactory:
    __connection: Conexao = None

    def get_service(self) -> Conexao:
        if ConnectionFactory.__connection is None:
            try: 
                conn = psycopg2.connect(
                    dbname="academia",
                    user="sa",
                    password="123321q",
                    host="localhost",
                    port="5432"
                )
            except Exception as e:
                print(f"Erro ao conectar ao banco de dados: {e}")
                raise e
            ConnectionFactory.__connection = Conexao(conn)
        return ConnectionFactory.__connection