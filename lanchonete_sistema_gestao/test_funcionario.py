import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Corrigir caminho para acessar arquivos do diretório principal
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lanchonete_sistema_gestao import funcionario


class TestFuncionario(unittest.TestCase):

    @patch("funcionario.conectar")
    @patch("builtins.input", side_effect=["João", "12345678900", "garcom", "joaouser", "senha123"])
    def test_cadastrar_funcionario(self, mock_input, mock_conectar):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conn

        funcionario.cadastrar_funcionario()

        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO funcionarios (nome, cpf, cargo, usuario, senha) VALUES (%s, %s, %s, %s, %s)",
            ("João", "12345678900", "garcom", "joaouser", "senha123")
        )
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("funcionario.conectar")
    def test_listar_funcionarios(self, mock_conectar):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, "Maria", "11111111111", "gerente", "mariauser")
        ]
        mock_conn.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conn

        funcionario.listar_funcionarios()

        mock_cursor.execute.assert_called_once_with("SELECT * FROM funcionarios")
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("funcionario.conectar")
    @patch("builtins.input", side_effect=["1", "Carlos", "22222222222", "cozinheiro", "carlosuser", "novaSenha"])
    def test_editar_funcionario(self, mock_input, mock_conectar):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conn

        funcionario.editar_funcionario()

        mock_cursor.execute.assert_called_once_with(
            "UPDATE funcionarios SET nome=%s, cpf=%s, cargo=%s, usuario=%s, senha=%s WHERE id=%s",
            ("Carlos", "22222222222", "cozinheiro", "carlosuser", "novaSenha", "1")
        )
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("funcionario.conectar")
    @patch("builtins.input", return_value="2")
    def test_excluir_funcionario(self, mock_input, mock_conectar):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conn

        funcionario.excluir_funcionario()

        mock_cursor.execute.assert_called_once_with(
            "DELETE FROM funcionarios WHERE id=%s", ("2",)
        )
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
