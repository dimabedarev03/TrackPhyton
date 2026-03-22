if __name__ == "__main__":
 class Birds:

 """Базовый класс Птицы."""

        def __init__(self, wingspan: float, food: str):
            """
 Создание и подготовка к работе класса "Птицы"
 :param wingspan: Размах крыльев птицы.
 :param food: Наименование пищи, чем питается птица.
            """
            self.wingspan = wingspan
            self.food = food

        def flight_speed(self, wingspan: float) -> int:
            """
 Функция, оценивающая скорость полета птицы в зависимости от размаха крыльев.
 Возвращает значение от 0 до 10, где 0 - скорость полета новорожденной, нелетающей птицы.
 :param wingspan: Размах крыльев.
            """
            ...

        def speed_limit(self, weight: int, age: int) -> int:
            """
            Функция, показывающая максимальную скорость птицы
            :param weight: Вес птицы.
            :param age: Возраст птицы.
            """
            ...

        def __str__(self):
            return f"Размах крыльев птицы {self.wingspan}, пища, которую ест птица {self.food}"

        def __repr__(self):
            return f"{self.__class__.__name__}(wingspan = {self.wingspan}, food = {self.food}"

    class Woodpecker(Birds):

        "Дочерний класс Дятел"

        def __init__(self, wingspan: float, food: str, flight_altitude: float):
            """
            Расширяет конструктор базового класса: добавляет высоту полета
            :param wingspan: Размах крыльев дятла.
            :param food: Пища, которой питается дятел.
            :param flight_altitude: Высота полета.
            """
            super().__init__(wingspan, food)
            self.flight_altitude = flight_altitude

        def __str__(self):
            """Расширяет строковое предствление, добавляя информацию о высоте полета дятла"""
            return f"Размах крыльев дятла {self.wingspan}, пища, которой питается дятел {self.food}, высота полета {self.flight_altitude}"

        def __repr__(self):
            """Расширяет официальное преставление с учетом новых атрибутов"""
            return f"{self.__class__.__name__}(wingspan = {self.wingspan}, food = {self.food}, flight_altitude = {self.flight_altitude}"
    pass
    