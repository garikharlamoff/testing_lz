import unittest
import formula

class TestFormula(unittest.TestCase):
    def test_normal_work(self):
        self.assertEqual(formula.err(52,42,69,67,169),60.0)

    def test_zero_err(self):
        result = formula.err(52,42,69,69,169)
        self.assertEqual(result,"Деление на ноль запрещено (c не равно d)")

    def test_minus_err(self):
        result = formula.err(52,42,69,67,-169)
        self.assertEqual(result,"Вычисление корня из отрицательного числа запрещено (f >= 0)")

    def test_type_err(self):
        result = formula.err(52,42,69,"sixseven",169)
        self.assertEqual(result,"Неверный тип данных")

if __name__ == "__main__":
    unittest.main()