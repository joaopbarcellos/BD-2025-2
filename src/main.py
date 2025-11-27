import customtkinter as ctk
from tkinter import ttk 
from customTypes import ConexaoInterface
from connectionFactory import connectionService

# Configuração inicial da aparência
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    connection: ConexaoInterface = None

    def __init__(self):
        super().__init__()
        self.connection = connectionService
        self.title("Sistema de Academia")
        self.geometry("1000x700")

        # Container principal onde as telas serão trocadas
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        # Inicia mostrando o Menu Principal
        self.show_menu()

    def get_connection(self) -> ConexaoInterface:
        return self.connection

    def clear_frame(self):
        """Remove todos os widgets do container atual"""
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_menu(self):
        self.clear_frame()
        MenuFrame(self.container, self)

    def show_create(self):
        self.clear_frame()
        CreateFrame(self.container, self)

    def show_read(self):
        self.clear_frame()
        ReadFrame(self.container, self)

    def show_intermediate(self):
        self.clear_frame()
        IntermediateFrame(self.container, self)

    def show_update(self, selected_item):
        self.clear_frame()
        UpdateFrame(self.container, self, selected_item)

    def show_delete(self):
        self.clear_frame()
        DeleteFrame(self.container, self)


class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=20, pady=20)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Menu Principal", font=("Arial", 24, "bold"))
        label.pack(pady=30)

        # Botões do Menu
        btn_create = ctk.CTkButton(self, text="Cadastrar professor", command=controller.show_create)
        btn_create.pack(pady=10, fill="x", padx=100)

        btn_read = ctk.CTkButton(self, text="Visualizar professores", command=controller.show_read)
        btn_read.pack(pady=10, fill="x", padx=100)

        btn_update = ctk.CTkButton(self, text="Atualizar professor", command=controller.show_intermediate)
        btn_update.pack(pady=10, fill="x", padx=100)

        btn_delete = ctk.CTkButton(self, text="Deletar professor", command=controller.show_delete, fg_color="red", hover_color="#8B0000")
        btn_delete.pack(pady=10, fill="x", padx=100)


class CreateFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(self, text="Cadastrar Novo Professor", font=("Arial", 20)).pack(pady=20)

        # Campos
        self.entry_name = ctk.CTkEntry(self, placeholder_text="Digite o Nome")
        self.entry_name.pack(pady=10, fill="x", padx=50)

        self.entry_login = ctk.CTkEntry(self, placeholder_text="Digite o Login")
        self.entry_login.pack(pady=10, fill="x", padx=50)

        self.entry_password = ctk.CTkEntry(self, placeholder_text="Digite a Senha", show="*")
        self.entry_password.pack(pady=10, fill="x", padx=50)

        ctk.CTkLabel(self, text="Selecione uma academia", font=("Arial", 14)).pack(pady=20)

        academias = self.read_academias()
        self.academias_dict = {nome: id_academia for id_academia, nome in academias}
        
        # Lista dos textos que serão exibidos no dropdown
        options = list(self.academias_dict.keys())
        
        # 1. Variável de Controle: Armazena o TEXTO exibido
        self.selected_option_text = ctk.StringVar(value=options[0])

        self.acad_dropdown = ctk.CTkOptionMenu(
            self,
            values=options,
            variable=self.selected_option_text  # Define a variável que será atualizada
        )
        self.acad_dropdown.pack(pady=10)
        
        ctk.CTkButton(self, text="Salvar", command=lambda: self.save_data(controller)).pack(pady=20)
        # Botão Voltar
        ctk.CTkButton(self, text="Voltar", fg_color="transparent", border_width=1, command=controller.show_menu).pack(side="bottom", pady=10)


    def read_academias(self):
        query = "SELECT id_academia, nome FROM academia"
        academias = app.get_connection().execute_query(query)
        return academias


    def save_data(self, controller):
        string_sql = f"""INSERT INTO professor (nome, login, senha, fk_academia_id_academia) 
        VALUES (
        '{self.entry_name.get()}', 
        '{self.entry_login.get()}', 
        '{self.entry_password.get()}', 
        {self.academias_dict.get(self.selected_option_text.get())})"""
        app.get_connection().execute_query(string_sql)
        controller.show_menu()


    # def option_changed(self, choice):
    #     real_value = self.academias_dict.get(choice)
        
    #     if real_value:
    #         self.value_label.configure(text=f"Academia escolhida: {choice}, {real_value}")
    #     else:
    #         self.value_label.configure(text="Erro de Mapeamento")


class IntermediateFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(self, text="Atualizar Professor", font=("Arial", 20)).pack(pady=10)
        ctk.CTkLabel(self, text="Selecione um item para atualizar", font=("Arial", 12)).pack()

        # Tabela Selecionável
        columns = ("id_professor", "nome", "login", "senha", "fk_academia_id_academia")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        
        # Cabeçalhos
        self.tree.heading("id_professor", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("login", text="Login")
        self.tree.heading("senha", text="Senha")
        self.tree.heading("fk_academia_id_academia", text="Academia ID")
        
        # Largura das colunas
        self.tree.column("id_professor", width=50)
        self.tree.column("nome", width=200)
        self.tree.column("login", width=150)
        self.tree.column("senha", width=150)
        self.tree.column("fk_academia_id_academia", width=100)
        
        self.tree.pack(fill="both", expand=True, pady=10)

        self.populate_table()

        ctk.CTkButton(self, text="Atualizar Selecionado", command=lambda: self.go_to_update(controller)).pack(pady=10)

        # Botão Voltar
        ctk.CTkButton(self, text="Voltar", fg_color="transparent", border_width=1, command=controller.show_menu).pack(side="bottom", pady=10)

    def populate_table(self):
        data = app.get_connection().execute_query("SELECT * FROM professor")
        for row in data:
            self.tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))


    def go_to_update(self, controller):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item)['values']
            controller.show_update(item_values)
        else:
            print("Nenhum item selecionado")

class UpdateFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, selected_item):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=20, pady=20)

        self.data = self.read_data(selected_item[0])

        ctk.CTkLabel(self, text="Atualizar Registro", font=("Arial", 20)).pack(pady=20)

        self.entry_name = ctk.CTkEntry(self, placeholder_text="Digite o Nome")
        self.entry_name.pack(pady=10, fill="x", padx=50)
        self.entry_name.insert(0, self.data[1]) 

        self.entry_login = ctk.CTkEntry(self, placeholder_text="Digite o Login")
        self.entry_login.pack(pady=10, fill="x", padx=50)
        self.entry_login.insert(0, self.data[2]) 

        self.entry_password = ctk.CTkEntry(self, placeholder_text="Digite a Senha", show="*")
        self.entry_password.pack(pady=10, fill="x", padx=50)
        self.entry_password.insert(0, self.data[3])  

        ctk.CTkLabel(self, text="Selecione uma academia", font=("Arial", 14)).pack(pady=20)

        academias = self.read_academias()
        self.academias_dict = {nome: id_academia for id_academia, nome in academias}
        
        options = list(self.academias_dict.keys())
        selected_academia_name = next((nome for nome, id_academia in self.academias_dict.items() if id_academia == self.data[4]), options[0])
        self.selected_option_text = ctk.StringVar(value=selected_academia_name)

        self.acad_dropdown = ctk.CTkOptionMenu(
            self,
            values=options,
            variable=self.selected_option_text  # Define a variável que será atualizada
        )

        self.acad_dropdown.pack(pady=10)
        ctk.CTkButton(self, text="Atualizar", command=lambda: self.update_data(controller)).pack(pady=20)
        ctk.CTkButton(self, text="Voltar", fg_color="transparent", border_width=1, command=controller.show_menu).pack(side="bottom", pady=10)

    def read_academias(self):
        query = "SELECT id_academia, nome FROM academia"
        academias = app.get_connection().execute_query(query)
        return academias

    def read_data(self, id_professor):
        query = f"SELECT * FROM professor WHERE id_professor = {id_professor}"
        data = app.get_connection().execute_query(query)
        if data:
            return data[0]
        return None


    def update_data(self, controller):
        if not self.data:
            print("Nenhum dado encontrado para atualizar.")
            return

        if not self.entry_name.get() or not self.entry_login.get() or not self.entry_password.get():
            print("Todos os campos devem ser preenchidos.")
            return
        
        string_sql = f"""UPDATE professor SET 
        nome = '{self.entry_name.get()}', 
        login = '{self.entry_login.get()}', 
        senha = '{self.entry_password.get()}', 
        fk_academia_id_academia = {self.academias_dict.get(self.selected_option_text.get())}
        WHERE id_professor = {self.data[0]}"""
        app.get_connection().execute_query(string_sql)
        controller.show_menu()


class ReadFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(self, text="Visualizar professores", font=("Arial", 20)).pack(pady=10)

        columns = ("id_professor", "nome", "login", "senha", "fk_academia_id_academia")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        
        # Cabeçalhos
        self.tree.heading("id_professor", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("login", text="Login")
        self.tree.heading("senha", text="Senha")
        self.tree.heading("fk_academia_id_academia", text="Academia ID")
        
        # Largura das colunas
        self.tree.column("id_professor", width=50)
        self.tree.column("nome", width=200)
        self.tree.column("login", width=150)
        self.tree.column("senha", width=150)
        self.tree.column("fk_academia_id_academia", width=100)

        self.tree.pack(fill="both", expand=True, pady=20)

        self.populate_table()

        # Botão Voltar
        ctk.CTkButton(self, text="Voltar", fg_color="transparent", border_width=1, command=controller.show_menu).pack(side="bottom", pady=10)
    
    def populate_table(self):
        data = app.get_connection().execute_query("SELECT * FROM professor")
        for row in data:
            self.tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))

class DeleteFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(self, text="Deletar Professor", font=("Arial", 20)).pack(pady=10)
        ctk.CTkLabel(self, text="Selecione um item para deletar", font=("Arial", 12)).pack()

        # Tabela Selecionável
        columns = ("id_professor", "nome", "login", "senha", "fk_academia_id_academia")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        
        # Cabeçalhos
        self.tree.heading("id_professor", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("login", text="Login")
        self.tree.heading("senha", text="Senha")
        self.tree.heading("fk_academia_id_academia", text="Academia ID")
        
        # Largura das colunas
        self.tree.column("id_professor", width=50)
        self.tree.column("nome", width=200)
        self.tree.column("login", width=150)
        self.tree.column("senha", width=150)
        self.tree.column("fk_academia_id_academia", width=100)
        
        self.tree.pack(fill="both", expand=True, pady=10)

        self.populate_table()

        # Botão Deletar
        ctk.CTkButton(self, text="Deletar Selecionado", fg_color="red", hover_color="#8B0000", command=lambda: self.delete_selected(controller)).pack(pady=10)

        # Botão Voltar
        ctk.CTkButton(self, text="Voltar", fg_color="transparent", border_width=1, command=controller.show_menu).pack(side="bottom", pady=10)

    def populate_table(self):
        data = app.get_connection().execute_query("SELECT * FROM professor")
        for row in data:
            self.tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))


    def delete_selected(self, controller):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item)['values']
            delete_query = f"DELETE FROM professor WHERE id_professor = {item_values[0]}"
            app.get_connection().execute_query(delete_query)
            self.tree.delete(selected_item)
            controller.show_menu()
        else:
            print("Nenhum item selecionado")


if __name__ == "__main__":
    app = App()
    app.mainloop()