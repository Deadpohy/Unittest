# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a * h) / 2
## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c
# Functions
## Circle
### Area
```python
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
```
### Perimeter
```python
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
```
## Rectangle
### Area
```python
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
```
### Perimeter
```python
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
```
## square
### Area
```python
def area(a):
    """Возвращает площадь квадрата"""
    # Параметры:
    #   a (int): длина квадрата
    #   b (int): ширина квадрата  
    # Возвращаемое значение:
    #   a * a: искомая площадь квадрата
    if type(a) is not int:
        raise TypeError("Сторона должен быть int")
    if a <= 0:
        raise ValueError("Сторона должен быть больше нуля")
    return a * a
```
### Perimeter
```python
def perimeter(a):
    """Возвращает периметр квадрата"""
    # Параметры:
    #   a (int): длина квадрата
    #   b (int): ширина квадрата
    # Возвращаемое значение:
    #   4 * a: искомый периметр квадрата
    if type(a) is not int:
        raise TypeError("Сторона должен быть int")
    if a <= 0:
        raise ValueError("Сторона должна быть больше нуля")
    return 4 * a
```