import unittest
from unittest.mock import patch, MagicMock
from lanchonete_sistema_gestao.mesa import visualizar_mesas, atualizar_status_mesa


class TestMesa(unittest.TestCase):

    @patch('lanchonete_sistema_gestao.mesa.conectar')
    @patch('builtins.print')
    def test_visualizar_mesas(self, mock_print, mock_conectar):
        # Mock da conexão e cursor
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, '10', 'livre'),
            (2, '11', 'ocupada')
        ]
        mock_conexao = MagicMock()
        mock_conexao.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conexao

        visualizar_mesas()

        # Verifica se o SELECT foi chamado
        mock_cursor.execute.assert_called_once_with("SELECT id, numero, status FROM mesas")
        # Verifica se os dados foram buscados
        mock_cursor.fetchall.assert_called_once()
        # Verifica se o print foi chamado com as mesas esperadas
        mock_print.assert_any_call("\n=== MESAS DISPONÍVEIS ===")
        mock_print.assert_any_call("ID: 1 | Número: 10 | Status: livre")
        mock_print.assert_any_call("ID: 2 | Número: 11 | Status: ocupada")
        # Verifica se cursor e conexão foram fechados
        mock_cursor.close.assert_called_once()
        mock_conexao.close.assert_called_once()

    @patch('lanchonete_sistema_gestao.mesa.conectar')
    @patch('builtins.input', side_effect=['10', 'ativa'])
    @patch('builtins.print')
    def test_atualizar_status_mesa_sucesso(self, mock_print, mock_input, mock_conectar):
        # Mock conexão e cursor
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 1  # indica que atualização afetou 1 linha
        mock_conexao = MagicMock()
        mock_conexao.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conexao

        atualizar_status_mesa()

        # Verifica se o UPDATE foi executado com os parâmetros corretos
        mock_cursor.execute.assert_called_once_with(
            "UPDATE mesas SET status = %s WHERE numero = %s",
            ('ativa', '10')
        )
        # Verifica se o commit foi chamado
        mock_conexao.commit.assert_called_once()
        # Verifica se a mensagem de sucesso foi impressa
        mock_print.assert_any_call("✅ Status da mesa atualizado com sucesso!")
        # Verifica se cursor e conexão foram fechados
        mock_cursor.close.assert_called_once()
        mock_conexao.close.assert_called_once()

    @patch('lanchonete_sistema_gestao.mesa.conectar')
    @patch('builtins.input', side_effect=['99', 'livre'])
    @patch('builtins.print')
    def test_atualizar_status_mesa_mesa_nao_encontrada(self, mock_print, mock_input, mock_conectar):
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 0  # nenhuma linha afetada
        mock_conexao = MagicMock()
        mock_conexao.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conexao

        atualizar_status_mesa()

        mock_print.assert_any_call("❌ Mesa não encontrada.")
        mock_cursor.close.assert_called_once()
        mock_conexao.close.assert_called_once()

    @patch('builtins.input', side_effect=['10', 'inválido'])
    @patch('builtins.print')
    def test_atualizar_status_mesa_status_invalido(self, mock_print, mock_input):
        # Não mocka conexão porque nem deve chegar a conectar se o status for inválido
        atualizar_status_mesa()
        mock_print.assert_any_call("❌ Status inválido.")


if __name__ == '__main__':
    unittest.main()
