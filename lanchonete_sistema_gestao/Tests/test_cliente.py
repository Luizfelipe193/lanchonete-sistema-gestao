import unittest
from unittest.mock import patch, MagicMock
from lanchonete_sistema_gestao import cliente


class TestCliente(unittest.TestCase):

    @patch('lanchonete_sistema_gestao.cliente.conectar')
    @patch('builtins.input', side_effect=["João", "123.456.789-00", "11999999999", "Rua A"])
    def test_cadastrar_cliente(self, mock_input, mock_conectar):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conectar.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        cliente.cadastrar_cliente()

        mock_cursor.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('lanchonete_sistema_gestao.cliente.conectar')
    def test_listar_clientes(self, mock_conectar):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, "João", "123.456.789-00", "11999999999", "Rua A")
        ]
        mock_conectar.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        cliente.listar_clientes()

        mock_cursor.execute.assert_called_once_with("SELECT * FROM clientes")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('lanchonete_sistema_gestao.cliente.conectar')
    @patch('builtins.input', side_effect=["1", "Maria", "987.654.321-00", "11888888888", "Rua B"])
    def test_editar_cliente(self, mock_input, mock_conectar):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conectar.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        cliente.editar_cliente()

        mock_cursor.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('lanchonete_sistema_gestao.cliente.conectar')
    @patch('builtins.input', return_value="1")
    def test_excluir_cliente(self, mock_input, mock_conectar):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conectar.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        cliente.excluir_cliente()

        mock_cursor.execute.assert_called_once_with("DELETE FROM clientes WHERE id=%s", ("1",))
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()

