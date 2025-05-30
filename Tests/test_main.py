import unittest
from unittest.mock import patch, MagicMock
from lanchonete_sistema_gestao import main


class TestMainSystem(unittest.TestCase):

    @patch('lanchonete_sistema_gestao.main.conectar')
    def test_conexao_banco(self, mock_conectar):
        # Simula conexão com o banco
        mock_conexao = MagicMock()
        mock_conexao.is_connected.return_value = True
        mock_conectar.return_value = mock_conexao

        try:
            main.main()  # Apenas checa se executa sem erro com mock
        except Exception as e:
            self.fail(f"main.main() lançou uma exceção inesperada: {e}")

    @patch('builtins.input', side_effect=["1", "admin1234", "1234"])
    @patch('lanchonete_sistema_gestao.login.login', return_value="administrador")
    def test_menu_inicial_retorna_cargo(self, mock_login, mock_input):
        cargo = main.menu_inicial()
        self.assertEqual(cargo, "administrador")

    def test_funcoes_importadas_existem(self):
        self.assertTrue(callable(main.menu_administrador))
        self.assertTrue(callable(main.menu_gerente))
        self.assertTrue(callable(main.menu_atendente))
        self.assertTrue(callable(main.menu_cozinheiro))
        self.assertTrue(callable(main.menu_garcom))
        self.assertTrue(callable(main.menu_inicial))


if __name__ == '__main__':
    unittest.main()


