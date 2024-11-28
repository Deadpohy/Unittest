import unittest
def area(a, h):
    """Возвращает площадь треугольника"""
    # Параметры:
    #   a (int): основание треугольника
    #   h (int): высота треугольника
    # Возвращаемое значение:
    #   a * h / 2: искомая площадь треугольника
    if type(a) is not int or type(h) is not int:
        raise TypeError("Основание и высота должны быть int")
    if a <= 0 or h <= 0:
        raise ValueError("Основание и высота должны быть больше нуля")
    return a * h / 2

def perimeter(a, b, c):
    """Возвращает периметр треугольника"""
    # Параметры:
    #   a (int): одна сторона треугольника
    #   b (int): вторая сторона треугольника
    #   c (int): третья сторона треугольника
    # Возвращаемое значение:
    #   a + b + c: искомый периметр треугольника
    if type(a) is not int or type(b) is not int or type(c) is not int:
        raise TypeError("Все стороны должны быть int")
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Все стороны должны быть больше нуля")
    return a + b + c
class TriangleAreaTestCases(unittest.TestCase):
    def test_triangle_int_first(self):
        self.assertEqual(area(5, 8), 5 * 8 / 2)

    def test_triangle_int_second(self):
        self.assertEqual(area(5725, 3872), 5725 * 3872 / 2)

    def test_triangle_string_first(self):
        with self.assertRaises(TypeError):
            area("19", 91)

    def test_triangle_string_second(self):
        with self.assertRaises(TypeError):
            area("arbuz", "lala")

    def test_triangle_bool_first(self):
        with self.assertRaises(TypeError):
            area(True, False)

    def test_triangle_bool_second(self):
        with self.assertRaises(TypeError):
            area(False)

    def test_triangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            area(-15, 19)

    def test_triangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            area(-5983, -1)

    def test_triangle_zero_int(self):
        with self.assertRaises(ValueError):
            area(0, 0)
class TrianglePerimeterTestCases(unittest.TestCase):
    def test_triangle_int_first(self):
        self.assertEqual(perimeter(9, 8, 1), 9 + 8 + 1)

    def test_triangle_int_second(self):
        self.assertEqual(perimeter(394732, 1985321, 3852999), 394732 + 3852999 + 1985321)

    def test_triangle_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("19", "23", "15")

    def test_triangle_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("IM", "FROM", "M3118")

    def test_triangle_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True)

    def test_triangle_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False)

    def test_triangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 158, 29)

    def test_triangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-59853, -15, -25)

    def test_triangle_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0, 19, 16)

