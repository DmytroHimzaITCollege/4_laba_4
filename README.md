# Звіт до роботи №4
## Тема: _Тестування_
### Мета роботи: _Тестування_
---
### Виконання роботи

- Результати виконання завдання *N1*;
Запустив даний код:
   ```python
   number = -1
   assert number > 0, "число має бути більшим за нуль!"
   ```
Результат коду в терміналі:
   ```
   ---------------------------------------------------------------------------
   AssertionError                            Traceback (most recent call last)
   Cell In [1], line 2
         1 number = -1
   ----> 2 assert number > 0, "число має бути більшим за нуль!"

   AssertionError: число має бути більшим за нуль!
   ```
   Запустив даний код:
   ```python
   a = input("Введіть число: ")
   assert a.isdigit(), "Потрібно ввести число!"
   print(f"введене число: {a}")
   ```
Результат коду в терміналі:
   ```
   введене число: 1
   ```
      Запустив даний код:
   ```python
   class Figure:
   def __init__(self, type, length) -> None:
   assert length > 0, "Довжина має бути більшою за 0!"
   assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
   self.type = type
   self.length = length

   a = Figure("трапеція", 12)
   b = Figure("квадрат", 0)
   c = Figure("квадрат", 1)
   ```
Результат коду в терміналі:
   ```
   AssertionError                            Traceback (most recent call last)
Cell In [15], line 8
      5         self.type = type
      6         self.length = length
----> 8 a = Figure("трапеція", 12)
      9 b = Figure("квадрат", 0)
     10 c = Figure("квадрат", 1)

Cell In [15], line 4, in Figure.__init__(self, type, length)
      2 def __init__(self, type, length) -> None:
      3     assert length > 0, "Довжина має бути більшою за 0!"
----> 4     assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
      5     self.type = type
      6     self.length = length

AssertionError: Дозволені фігури: квадрат, прямокутник, трикутник
   ```
    Запустив даний код:
   ```python
   class Name:
   def __init__(self, name) -> None:
   if name not in ["Дмитро", "Анонім"]:
   raise ValueError("Дозволені імена: Дмитро, Анонім")
   self.name = name

   class Hobby:
   def __init__(self, hobby) -> None:
   if hobby not in ["IT", "Програмування"]:
   raise ValueError("Дозволені хоббі: IT, Програмування)
   self.hobby = hobby
   ```
Результат коду в терміналі:
   ```
   Cell In [17], line 10
    raise ValueError("Дозволені хоббі: IT, Програмування)
                     ^
   SyntaxError: unterminated string literal (detected at line 10)
   ```
   - Результати виконання завдання *N2*;
Запустив даний код:
   ```python
   class Figure:
      FIGURES = ["квадрат", "прямокутник", "трикутник"]
      def __init__(self, type, length) -> None:
         assert length > 0, "Довжина має бути більшою за 0!"
         assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
         self.type = type
         self.length = length

      @property
      def get_figure_type(self):
         return self.type

      @property
      def get_figure_length(self):
         return self.type # робимо помилку
   ```
Результат коду в терміналі:
   ```

   ```
   Запустив даний код:
   ```python
   import unittest
   from random import choice, randint

   from app import Figure # назва файлу з нашим класом повинна бути app.py

   class TestFigure(unittest.TestCase):
      @classmethod
      def setUpClass(cls):
         """Виконається лише раз на початку тестів
         """
         pass
      
      def setUp(self) -> None:
         """Виконується кожного разу коли запускається тест
         """
         self.figure = choice(Figure.FIGURES)
         self.length = randint(1, 10)
         self.obj = Figure(self.figure, self.length)
         return super().setUp()

      def tearDown(self) -> None:
         del self.obj
         return super().tearDown()

      def test_figure_type(self):
         print(f"Тестуємо вивід, має бути: {self.figure} == {self.obj.get_figure_type}")
         self.assertEqual(self.figure, self.obj.get_figure_type, "Властивість get_figure_type повертає непривильну фігуру!")

      def test_figure_lengh(self):
         self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає непривильну довжину!")
      
      def test_obj(self):
         with self.assertRaises(AssertionError):
               Figure("коло", 1) # Спробуємо створити обєкт з недозволеними параметрими, в нас має бути помилка AssertionError


   if __name__ == '__main__':
      unittest.main() # unittest.main(verbosity=2) щоб був більш детальний вивід
   ```
Результат коду в терміналі:
   ```
      ---------------------------------------------------------------------------
   ModuleNotFoundError                       Traceback (most recent call last)
   Cell In [21], line 4
         1 import unittest
         2 from random import choice, randint
   ----> 4 from app import Figure # назва файлу з нашим класом повинна бути app.py
         6 class TestFigure(unittest.TestCase):
         7     @classmethod
         8     def setUpClass(cls):

   ModuleNotFoundError: No module named 'app'
   ```
    - Результати виконання завдання *N3*;
- ![5laba1](https://github.com/DmytroHimzaITCollege/4_laba_4/blob/main/%D0%AE%D0%BD%D1%96%D1%82%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%20%D0%B7%20%D0%B2%D0%B8%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%B0%D0%BD%D0%BD%D1%8F%20%D0%B1%D1%96%D0%B1%D0%BB%D1%96%D0%BE%D1%82%D0%B5%D0%BA%D0%B8%20PyTest%201.png?raw=true)
- ![5laba1](https://github.com/DmytroHimzaITCollege/4_laba_4/blob/main/%D0%AE%D0%BD%D1%96%D1%82%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%20%D0%B7%20%D0%B2%D0%B8%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%B0%D0%BD%D0%BD%D1%8F%20%D0%B1%D1%96%D0%B1%D0%BB%D1%96%D0%BE%D1%82%D0%B5%D0%BA%D0%B8%20PyTest%202.png?raw=true)

+ Виконав індивідуальні завдання для кождного пункту.
### Висновок: 
> у висновку потрібно відповісти на запитання:
- :question: Що зроблено в роботі - Проведенно тестування;
- :question: Чи досягнуто мети роботи - Частково;
- :question: Які нові знання отримано - знання тестування коду;
- :question: Чи вдалось відповісти на всі питання задані в ході роботи - Ні.;
- :question: Чи вдалося виконати всі завдання - Ні.;
- :question: Чи виникли складності у виконанні завдання - Так.;
- :question: Чи подобається такий формат здачі роботи (Feedback)- Так.;
- :question: Побажання для покращення (Suggestions) - Немає побажань;
---# -
