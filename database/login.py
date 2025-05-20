import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="bardopastel2020",
        database="lanchonete_db"
    )

def login():
    usuario = input("Login: ")
    senha = input("Senha: ")

    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM funcionarios WHERE login = %s AND senha = %s"
    cursor.execute(query, (usuario, senha))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if resultado:
        print(f"\n✅ Bem-vindo(a), {resultado['nome']}!")
        return resultado['cargo']
    else:
        print("\n❌ Login ou senha incorretos.")
        return None

# Apenas para testes individuais
if __name__ == "__main__":
    cargo = login()
    if cargo:
        print(f"Cargo identificado: {cargo}")

