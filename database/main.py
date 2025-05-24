import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db_config import conectar
from database.produto import cadastrar_produto, listar_produtos, editar_produto, excluir_produto
from database.cliente import cadastrar_cliente, listar_clientes, editar_cliente, excluir_cliente
from database.funcionario import cadastrar_funcionario, listar_funcionarios, editar_funcionario, excluir_funcionario
from database.pedido import (
    registrar_pedido, listar_pedidos, editar_pedido, excluir_pedido,
    relatorio_faturamento_por_pagamento, gerenciar_pedidos_cozinha
)
from database.estoque import visualizar_estoque

from login import login, cadastrar_usuario, recuperar_senha


def menu_produto():
    while True:
        print("\n=== MENU DE PRODUTOS ===")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Editar Produto")
        print("4. Excluir Produto")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            editar_produto()
        elif opcao == '4':
            excluir_produto()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


def menu_cliente():
    while True:
        print("\n=== MENU DE CLIENTES ===")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Editar Cliente")
        print("4. Excluir Cliente")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            editar_cliente()
        elif opcao == '4':
            excluir_cliente()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


def menu_funcionario():
    while True:
        print("\n=== MENU DE FUNCIONÁRIOS ===")
        print("1. Cadastrar Funcionário")
        print("2. Listar Funcionários")
        print("3. Editar Funcionário")
        print("4. Excluir Funcionário")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            listar_funcionarios()
        elif opcao == '3':
            editar_funcionario()
        elif opcao == '4':
            excluir_funcionario()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


def menu_pedido():
    while True:
        print("\n=== MENU DE PEDIDOS ===")
        print("1. Registrar Pedido")
        print("2. Listar Pedidos")
        print("3. Editar Pedido")
        print("4. Excluir Pedido")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_pedido()
        elif opcao == '2':
            listar_pedidos()
        elif opcao == '3':
            editar_pedido()
        elif opcao == '4':
            excluir_pedido()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


def menu_estoque():
    while True:
        print("\n=== MENU DE ESTOQUE ===")
        print("1. Visualizar Movimentação de Estoque")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            visualizar_estoque()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


def menu_relatorios():
    while True:
        print("\n=== MENU DE RELATÓRIOS ===")
        print("1. Faturamento por Forma de Pagamento")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            relatorio_faturamento_por_pagamento()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


def menu_gerente():
    while True:
        print("\n=== MENU GERENTE ===")
        print("1. Produtos")
        print("2. Clientes")
        print("3. Funcionários")
        print("4. Pedidos")
        print("5. Estoque")
        print("6. Relatórios")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_produto()
        elif opcao == '2':
            menu_cliente()
        elif opcao == '3':
            menu_funcionario()
        elif opcao == '4':
            menu_pedido()
        elif opcao == '5':
            menu_estoque()
        elif opcao == '6':
            menu_relatorios()
        elif opcao == '0':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")


def menu_atendente():
    while True:
        print("\n=== MENU ATENDENTE ===")
        print("1. Pedidos")
        print("2. Clientes")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_pedido()
        elif opcao == '2':
            menu_cliente()
        elif opcao == '0':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")


def menu_cozinheiro():
    while True:
        print("\n=== MENU COZINHEIRO ===")
        print("1. Visualizar Pedidos / Alterar Status")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            gerenciar_pedidos_cozinha()
        elif opcao == '0':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")


def menu_inicial():
    while True:
        print("\n=== SISTEMA DE GESTÃO DE LANCHONETE ===")
        print("1. Login")
        print("2. Cadastrar Novo Usuário")
        print("3. Esqueci minha Senha")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cargo = login()
            if cargo:
                return cargo
        elif escolha == "2":
            cadastrar_usuario()
        elif escolha == "3":
            recuperar_senha()
        elif escolha == "0":
            print("Encerrando o sistema.")
            exit()
        else:
            print("Opção inválida.")


def main():
    try:
        conexao = conectar()
        if conexao.is_connected():
            conexao.close()

            cargo = menu_inicial()

            # Redireciona para o menu conforme o cargo
            if cargo == "gerente":
                menu_gerente()
            elif cargo == "atendente":
                menu_atendente()
            elif cargo == "cozinheiro":
                menu_cozinheiro()
            else:
                print("Cargo não reconhecido ou sem permissões.")
    except Exception as e:
        print(f"Erro ao conectar com o banco: {e}")


if __name__ == "__main__":
    main()





















