import psycopg2
class ConexaoInterface:

    def get_connection(self) -> psycopg2.extensions.connection:
        pass

    def close_connection(self) -> None:
        pass

    def execute_query(self, query: str, params: tuple = ()) -> list:
        pass