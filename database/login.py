import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="bardopastel2020",
        database="lanchonete_db"
    )

def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM funcionarios WHERE usuario = %s AND senha = %s"
    cursor.execute(query, (usuario, senha))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if resultado:
        print(f"\n✅ Bem-vindo(a), {resultado['nome']}!")
        return resultado['cargo']
    else:
        print("\n❌ Usuário ou senha incorretos.")
        return None


def cadastrar_usuario():
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    cargo = input("Cargo (gerente / atendente / cozinheiro): ")
    usuario = input("Usuário desejado: ")
    senha = input("Senha: ")

    conn = conectar_bd()
    cursor = conn.cursor()

    query = "INSERT INTO funcionarios (nome, cpf, cargo, usuario, senha) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, cpf, cargo, usuario, senha)
    cursor.execute(query, valores)

    conn.commit()
    print("\n✅ Usuário cadastrado com sucesso!")

    cursor.close()
    conn.close()


def recuperar_senha():
    usuario = input("Digite seu nome de usuário: ")
    cpf = input("Digite seu CPF cadastrado: ")

    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT senha FROM funcionarios WHERE usuario = %s AND cpf = %s"
    cursor.execute(query, (usuario, cpf))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if resultado:
        print(f"\n🔐 Sua senha é: {resultado['senha']}")
    else:
        print("\n❌ Usuário ou CPF não encontrados.")


# Apenas para testes individuais
if __name__ == "__main__":
    print("1 - Login")
    print("2 - Cadastrar novo usuário")
    print("3 - Esqueci minha senha")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        login()
    elif escolha == "2":
        cadastrar_usuario()
    elif escolha == "3":
        recuperar_senha()
    else:
        print("Opção inválida.")


