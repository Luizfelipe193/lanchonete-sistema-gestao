import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Corrige o caminho para importar o pacote lanchonete_sistema_gestao
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lanchonete_sistema_gestao import estoque


class TestEstoque(unittest.TestCase):

    @patch("lanchonete_sistema_gestao.estoque.conectar")
    def test_atualizar_estoque_entrada(self, mock_conectar):
        mock_conexao = MagicMock()
        mock_cursor = MagicMock()
        mock_conexao.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conexao

        # Supondo que a função atualiza_estoque existe
        estoque.atualizar_estoque(1, 10, operacao="entrada")

        mock_cursor.execute.assert_called()
        mock_conexao.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conexao.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
