import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from classificador import (  # noqa: E402
    classificar_nivel,
    classificar_nivel_por_laco,
    formatar_mensagem,
)

CASOS = [
    (0, "Ferro"), (999, "Ferro"), (1000, "Ferro"),
    (1001, "Bronze"), (2000, "Bronze"),
    (2001, "Prata"), (5000, "Prata"),
    (5001, "Ouro"), (7000, "Ouro"),
    (7001, "Platina"), (8000, "Platina"),
    (8001, "Ascendente"), (9000, "Ascendente"),
    (9001, "Imortal"), (10000, "Imortal"),
    (10001, "Radiante"), (99999, "Radiante"),
]


class TestClassificador(unittest.TestCase):
    def test_if_elif(self):
        for xp, esperado in CASOS:
            with self.subTest(xp=xp):
                self.assertEqual(classificar_nivel(xp), esperado)

    def test_versao_com_laco(self):
        for xp, esperado in CASOS:
            with self.subTest(xp=xp):
                self.assertEqual(classificar_nivel_por_laco(xp), esperado)

    def test_xp_negativo(self):
        with self.assertRaises(ValueError):
            classificar_nivel(-1)

    def test_mensagem(self):
        self.assertEqual(
            formatar_mensagem("Aragorn", "Ouro"),
            "O Herói de nome **Aragorn** está no nível de **Ouro**",
        )


if __name__ == "__main__":
    unittest.main()
