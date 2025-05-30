import unittest
from unittest.mock import patch, mock_open, MagicMock
from lanchonete_sistema_gestao import login


class TestLogin(unittest.TestCase):

    @patch("builtins.input", side_effect=["admin1234", "1234"])
    @patch("builtins.open", new_callable=mock_open, read_data="1234")
    @patch("os.path.exists", return_value=True)
    def test_login_administrador_sucesso(self, mock_exists, mock_open_file, mock_input):
        cargo = login.login()
        self.assertEqual(cargo, "administrador")

    @patch("builtins.open", new_callable=mock_open)
    def test_salvar_senha_admin(self, mock_file):
        nova_senha = "nova123"
        login.salvar_senha_admin(nova_senha)
        mock_file().write.assert_called_once_with(nova_senha)

    @patch("builtins.open", new_callable=mock_open, read_data="senha321")
    @patch("os.path.exists", return_value=True)
    def test_obter_senha_admin_existente(self, mock_exists, mock_file):
        senha = login.obter_senha_admin()
        self.assertEqual(senha, "senha321")

    @patch("os.path.exists", return_value=False)
    def test_obter_senha_admin_arquivo_nao_existe(self, mock_exists):
        m = mock_open()
        # Simular comportamento de escrita e depois leitura
        m().read.return_value = "1234"
        with patch("builtins.open", m):
            senha = login.obter_senha_admin()
            m().write.assert_called_once_with("1234")
            self.assertEqual(senha, "1234")

    @patch("builtins.input", side_effect=["joao123", "senha123"])
    @patch("lanchonete_sistema_gestao.login.conectar_bd")
    def test_login_funcionario_sucesso(self, mock_conectar, mock_input):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {
            "nome": "João", "cargo": "garcom"
        }
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conn

        cargo = login.login()
        self.assertEqual(cargo, "garcom")

    @patch("builtins.input", side_effect=["joao123", "senhaerrada"])
    @patch("lanchonete_sistema_gestao.login.conectar_bd")
    def test_login_funcionario_falha(self, mock_conectar, mock_input):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conn

        cargo = login.login()
        self.assertIsNone(cargo)


if __name__ == '__main__':
    unittest.main()
