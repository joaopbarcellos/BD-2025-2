from service.connection import Conexao
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
                ConnectionFactory.__connection = Conexao(conn)
            except Exception as e:
                print(f"Erro ao conectar ao banco de dados: {e}")
                raise e
        return ConnectionFactory.__connection
    

connectionService: Conexao = ConnectionFactory().get_service()