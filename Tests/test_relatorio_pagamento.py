import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import contextlib

from lanchonete_sistema_gestao import relatorio_pagamento


class TestRelatorioPagamento(unittest.TestCase):

    @patch('lanchonete_sistema_gestao.relatorio_pagamento.conectar')
    def test_relatorio_por_forma_pagamento(self, mock_conectar):
        # Mocka os dados retornados do banco
        dados_mock = [('Cartão', 150.00), ('Pix', 300.75)]

        # Mocka cursor e conexão
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = dados_mock
        mock_conexao = MagicMock()
        mock_conexao.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conexao

        # Captura a saída de forma compatível
        output = StringIO()
        with contextlib.redirect_stdout(output):
            relatorio_pagamento.relatorio_por_forma_pagamento()

        # Verifica se o conteúdo esperado está presente
        saida = output.getvalue()
        self.assertIn("Forma de Pagamento: Cartão | Faturamento Total: R$150.00", saida)
        self.assertIn("Forma de Pagamento: Pix | Faturamento Total: R$300.75", saida)

        # Verifica se o cursor e conexão foram fechados
        mock_cursor.close.assert_called_once()
        mock_conexao.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()

