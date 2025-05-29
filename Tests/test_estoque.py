import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock, ANY
from database.estoque import atualizar_estoque, visualizar_estoque



class TestEstoque(unittest.TestCase):

    @patch('database.estoque.conectar')
    def test_atualizar_estoque_entrada(self, mock_conectar):
        mock_conexao = MagicMock()
        mock_cursor = MagicMock()
        mock_conexao.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conexao

        atualizar_estoque(id_produto=2, quantidade=5, operacao='entrada')

        # Verificações aqui

        mock_cursor.execute.assert_any_call(
            "UPDATE produtos SET estoque = estoque + %s WHERE id = %s", (5, 2)
        )
        mock_cursor.execute.assert_any_call(ANY, (2, 5, 0))  # entrada: 5, saída: 0
        mock_conexao.commit.assert_called()

    @patch('database.estoque.conectar')
    def test_atualizar_estoque_saida(self, mock_conectar):
        mock_conexao = MagicMock()
        mock_cursor = MagicMock()
        mock_conexao.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conexao

        atualizar_estoque(id_produto=1, quantidade=10, operacao='saida')

        mock_cursor.execute.assert_any_call(
            "UPDATE produtos SET estoque = estoque - %s WHERE id = %s", (10, 1)
        )
        mock_cursor.execute.assert_any_call(ANY, (1, 0, 10))  # entrada: 0, saída: 10
        mock_conexao.commit.assert_called()

    @patch('database.estoque.conectar')
    def test_visualizar_estoque(self, mock_conectar):
        mock_conexao = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, "Hambúrguer", 10, 0, "2025-05-28 10:00:00"),
            (2, "Refrigerante", 0, 5, "2025-05-28 11:00:00")
        ]
        mock_conexao.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conexao

        visualizar_estoque()

        mock_cursor.execute.assert_called_once()
        mock_cursor.fetchall.assert_called_once()


if __name__ == '__main__':
    unittest.main()
