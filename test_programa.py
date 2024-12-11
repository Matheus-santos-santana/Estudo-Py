import unittest
from funcoes import validar_idade, validar_sexo, validar_decisao, contar_pessoas

class TestPrograma(unittest.TestCase):

    def test_validar_idade(self):
        self.assertTrue(validar_idade('18'))  # Idade válida
        self.assertTrue(validar_idade('0'))  # Idade válida (zero)
        self.assertFalse(validar_idade('-1'))  # Idade negativa não válida
        self.assertFalse(validar_idade('abc'))  # Texto não numérico não válido
        self.assertFalse(validar_idade(' 18'))  # Idade com espaço extra
        self.assertFalse(validar_idade('18 anos'))  # Texto extra não válido
        self.assertFalse(validar_idade(''))  # Entrada vazia não válida

    def test_validar_sexo(self):
        self.assertTrue(validar_sexo('M'))  # Sexo masculino válido
        self.assertTrue(validar_sexo('F'))  # Sexo feminino válido
        self.assertFalse(validar_sexo('X'))  # Sexo inválido
        self.assertFalse(validar_sexo(''))  # Entrada vazia não válida

    def test_validar_decisao(self):
        self.assertTrue(validar_decisao('S'))  # Resposta 'Sim' válida
        self.assertTrue(validar_decisao('N'))  # Resposta 'Não' válida
        self.assertFalse(validar_decisao('A'))  # Resposta inválida
        self.assertFalse(validar_decisao(''))  # Entrada vazia não válida

    def test_contar_pessoas(self):
        # Contar uma pessoa do sexo masculino
        count, countM, countF = contar_pessoas(18, 'M', 0, 0, 0)
        self.assertEqual(count, 1)  # Uma pessoa foi contada
        self.assertEqual(countM, 1)  # Uma pessoa do sexo masculino
        self.assertEqual(countF, 0)  # Nenhuma pessoa do sexo feminino

        # Contar uma pessoa do sexo feminino
        count, countM, countF = contar_pessoas(19, 'F', 0, 0, 0)
        self.assertEqual(count, 1)  # Uma pessoa foi contada
        self.assertEqual(countM, 0)  # Nenhuma pessoa do sexo masculino
        self.assertEqual(countF, 1)  # Uma pessoa do sexo feminino

    def test_validar_idade_adicional(self):
        # Testar com espaço extra antes do número
        self.assertFalse(validar_idade(' 18'))  # Entrada com espaço

        # Testar com texto extra (não numérico)
        self.assertFalse(validar_idade('18 anos'))  # Entrada com texto

        # Testar com uma string vazia
        self.assertFalse(validar_idade(''))  # Entrada vazia

if __name__ == '__main__':
    unittest.main()
r