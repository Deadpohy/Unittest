import math
import unittest
def area(r):
    """Возвращает площадь круга"""
    # Параметры:
    #   r (int): радиус круга
    # Возвращаемое значение:
    #   math.pi * r * r: искомая площадь круга
    if type(r) is not int:
        raise TypeError("Радиyc должен быть int")
    if r <= 0:
        raise ValueError("Paдиyc должен быть больше нуля")
    return math.pi * r * r

def perimeter(r):
    """Возвращает периметр круга"""
    # Параметры:
    #   r (int): радиус круга
    # Возвращаемое значение:
    #   2 * math.pi * r: искомый периметр круга
    if type(r) is not int:
        raise TypeError("Радиyс должен быть int")
    if r <= 0:
        raise ValueError("Радиyс должен быть больше нуля")
    return 2 * math.pi * r
class CircleAreaTestCases(unittest.TestCase):
  def test_circle_int_first(self):
    self.assertEqual(area(1235), math.pi * 1235 * 1235)
  def test_circle_int_second(self):
    self.assertEqual(area(575), math.pi * 575 * 575)
  def test_circle_string_first(self):
    with self.assertRaises(TypeError):
      area("32")
  def test_circle_string_second(self):
    with self.assertRaises(TypeError):
      area("itmo")
  def test_circle_bool_first(self):
    with self.assertRaises(TypeError):
      area(True)
  def test_circle_bool_second(self):
    with self.assertRaises(TypeError):
      area(False)
  def test_circle_negative_int_first(self):
    with self.assertRaises(ValueError):
      area(-412)
  def test_circle_negative_int_second(self):
    with self.assertRaises(ValueError):
      area(-9853)
  def test_circle_zero_int(self):
    with self.assertRaises(ValueError):
      area(0)
class CirclePerimeterTestCases(unittest.TestCase):
  def test_circle_int_first(self):
    self.assertEqual(perimeter(7), 2 * math.pi * 7)
  def test_circle_int_second(self):
    self.assertEqual(perimeter(57285), 2 * math.pi * 57285)
  def test_circle_string_first(self):
    with self.assertRaises(TypeError):
      perimeter("85")
  def test_circle_string_second(self):
    with self.assertRaises(TypeError):
      perimeter("ITMO")
  def test_circle_bool_first(self):
    with self.assertRaises(TypeError):
      perimeter(True)
  def test_circle_bool_second(self):
    with self.assertRaises(TypeError):
      perimeter(False)
  def test_circle_negative_int_first(self):
    with self.assertRaises(ValueError):
      perimeter(-5)
  def test_circle_negative_int_second(self):
    with self.assertRaises(ValueError):
      perimeter(-59853)
  def test_circle_zero_int(self):
    with self.assertRaises(ValueError):
      perimeter(0)

if __name__ == "__main__":
  unittest.main()

