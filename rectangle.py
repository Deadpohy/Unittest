import unittest
def area(a, b):
    """Возвращает площадь прямоугольника"""
    # Параметры:
    #   a (int): длина прямоугольника
    #   b (int): ширина прямоугольника
    # Возвращаемое значение:
    #   a * b: искомая площадь прямоугольника
    if type(a) is not int or type(b) is not int:
        raise TypeError("Длина и ширина должны быть int")
    if a <= 0 or b <= 0:
        raise ValueError("Длина и ширина должны быть больше нуля")
    return a * b

def perimeter(a, b):
    """Возвращает периметр прямоугольника"""
    # Параметры:
    #   a (int): длина прямоугольника
    #   b (int): ширина прямоугольника
    # Возвращаемое значение:
    #   2 * (a + b): искомый периметр прямоугольника
    if type(a) is not int or type(b) is not int:
        raise TypeError("Длина и ширина должны быть int")
    if a <= 0 or b <= 0:
        raise ValueError("Длина и ширина должны быть больше нуля")
    return 2 * (a + b)
class RectangleAreaTestCases(unittest.TestCase):
    def test_rectangle_int_first(self):
        self.assertEqual(area(5, 19), 5 * 19)

    def test_rectangle_int_second(self):
        self.assertEqual(area(57285, 187533), 57285 * 187533)

    def test_rectangle_string_first(self):
        with self.assertRaises(TypeError):
            area("13", "23")

    def test_rectangle_string_second(self):
        with self.assertRaises(TypeError):
            area("14", 19)

    def test_rectangle_bool_first(self):
        with self.assertRaises(TypeError):
            area(True, True)

    def test_rectangle_bool_second(self):
        with self.assertRaises(TypeError):
            area(False, False)

    def test_rectangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            area(-15, 18)

    def test_rectangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            area(-5983, -1)

    def test_rectangle_zero_int_first(self):
        with self.assertRaises(ValueError):
            area(0, 8)

    def test_rectangle_zero_int_second(self):
        with self.assertRaises(ValueError):
            area(0, 0)
class RectanglePerimeterTestCases(unittest.TestCase):
    def test_rectangle_int_first(self):
        self.assertEqual(perimeter(5, 9), 2 * (5 + 9))

    def test_rectangle_int_second(self):
        self.assertEqual(perimeter(57285, 394732), 2 * (57285 + 394732))

    def test_rectangle_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("13", "23")
    def test_rectangle_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("14", 19)
    def test_rectangle_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True, True)
    def test_rectangle_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False, False)
    def test_rectangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-15, 18)
    def test_rectangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-5983, -1)
    def test_rectangle_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0, 8)

    def test_rectangle_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0, 0)
