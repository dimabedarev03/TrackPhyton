import doctest
from typing import Union


class GasCan:
    def __init__(self, type_of_gascan: str, capacity_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Канистра для бензина"

        :param type_of_gascan: Тип канистры
        :param capacity_volume: Объем канистры, л

        Пример:
        >>> gascan = GasCan("Металлическая", 20) # инициализация экземпляра класса
        """
        if not isinstance(type_of_gascan, str):
            raise TypeError("Тип канистры должен быть типа str")
        self.type_of_gascan = type_of_gascan

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем канистры должен быть типа int или float")
        if capacity_volume < 0:
            raise ValueError("Объем канистры не может быть отрицательным числом")
        self.capacity_volume = capacity_volume

    def add_gas_to_gascan(self, gas: float) -> None:
        """
        Добавление бензина в канистру
        :param gas: Объем добавляемого бензина

        :raise ValueError: Если количество добавляемого бензина превышает свободное место в канистре, то вызываем ошибку

        Пример:
        >>> gascan = GasCan("Пластиковая", 20)
        >>> gascan.add_gas_to_gascan(15)
        """
        if not isinstance(gas, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if gas < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")
        ...
    def count_of_generator(self, generator_volume: Union[int, float]) -> int:
        """
        Разлитие бензина по генераторам

        :param generator_volume: Объем генератора, л

        :raise ValueError: Если объем генератора превышает объем канистры, то возвращается ошибка.

        Пример:
        >>> gascan = GasCan("Пластиковая", 20)
        >>> gascan.count_of_generator(10)
        """
        ...

class Room:
    def __init__(self, length: float, width: float, height: float):
        """
        Создание и подготовка к работе "Комната"

        :param length: Длина квартиры, м
        :param width: Ширина квартиры, м
        :param height: Высота квартиры, м

        Пример:
        room = Room(5, 4, 2.1) # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина комнаты должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина комнаты должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина комнаты должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина комнаты должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота комнаты должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота комнаты должна быть положительным числом")
        self.height = height

    def volume_calculation(self) -> float:
        """
        Расчет объема комнаты.

        :return: Объем заданной комнаты

        Примеры:
        >>> room = Room(5, 4, 2.2)
        >>> room.volume_calculation()
        """
        ...

    def coverage_area(self) -> float:
        """
        Расчет площади стен для отделки.

        :return: Площадь всех стен

        Пример:
        >>> room = Room(5, 4, 2.2)
        >>> room.coverage_area()
        """
        ...
    def wardrobe(self, wardrobe_hight: float, wardrobe_length: float) -> bool:
        """
        Функция, проверяющая влезет ли шкаф в квартиру

        :param wardrobe_hight: Высота шкафа
        :param wardrobe_length: Длина шкафа

        :return: Подойдет ли шкаф для заданной квартиры

        Пример:
        >>> room = Room(5, 4, 2.3)
        >>> room.wardrobe(2.8, 3)
        """
        ...

class Nails:
    def __init__(self, colour: str, length: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Ногти"

        :param colour: Цвет
        :param length: Длина ногтей, мм

        Пример:
        >>> nails = Nails("Розовые", 15) # инициализация экземпляра класса
        """
        if not isinstance(colour, str):
            raise TypeError("Цвет должен быть типа str")
        self.colour = colour

        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина должна быть положительной, либо равна нулю")
        self.length = length

    def cutting_nails(self, cutting_nails_length: Union[int, float]) -> int:
        """
        Функция, которая укорачивает длину ногтей.

        :param cutting_nails_length: Длина после стрижки ногтей

        :raise ValueError: Если длина стрижки, больше чем длина ногтей, то возвращается ошибка.

        Пример:
        >>> nails = Nails("Розовые", 15)
        >>> nails.cutting_nails(12)
        """
        ...

    def nails_extensions(self, nails_extensions_length: Union[int, float]) -> int:
        """
        Функция, которая увеличивает длину ногтей.

        :param nails_extensions_length: Длина наращивания

        Пример:
        >>> nails = Nails("Розовые", 15)
        >>> nails.nails_extensions(20)
        """
        ...


if __name__ == "__main__":
    doctest.testmod() # тестирование примеров, которые находятся в документации
    pass
