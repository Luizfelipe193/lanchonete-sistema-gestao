from database.db_config import conectar

def cadastrar_funcionario():
    nome = input("Nome do funcionário: ")
    cargo = input("Cargo: ")
    login = input("Login: ")
    senha = input("Senha: ")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO funcionarios (nome, cargo, login, senha) VALUES (%s, %s, %s, %s)"
    valores = (nome, cargo, login, senha)
    cursor.execute(sql, valores)

    conexao.commit()
    print("Funcionário cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def listar_funcionarios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()

    print("\n=== LISTA DE FUNCIONÁRIOS ===")
    for funcionario in funcionarios:
        print(f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Cargo: {funcionario[2]}, Login: {funcionario[3]}")

    cursor.close()
    conexao.close()

def editar_funcionario():
    id_funcionario = input("ID do funcionário a editar: ")
    nome = input("Novo nome: ")
    cargo = input("Novo cargo: ")
    login = input("Novo login: ")
    senha = input("Nova senha: ")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "UPDATE funcionarios SET nome=%s, cargo=%s, login=%s, senha=%s WHERE id=%s"
    valores = (nome, cargo, login, senha, id_funcionario)
    cursor.execute(sql, valores)

    conexao.commit()
    print("Funcionário atualizado com sucesso!")

    cursor.close()
    conexao.close()

def excluir_funcionario():
    id_funcionario = input("ID do funcionário a excluir: ")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM funcionarios WHERE id=%s"
    cursor.execute(sql, (id_funcionario,))

    conexao.commit()
    print("Funcionário excluído com sucesso!")

    cursor.close()
    conexao.close()
