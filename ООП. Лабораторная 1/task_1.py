# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Computer:
    def __init__(self, video_card: str, processor: str, motherboard: str):
        """
        Создание и подготовка к работе объекта "Компьютер"

        :param video_card: Видеокарта
        :param processor: Процессор
        :param motherboard: Материнская плата

        Пример:
        >>> comp = Computer("GeForce RTX 3060 12 Gb", "Intel Core i7-10700F", "MSI PRO H510M-B")
        """

        self.video_card = video_card
        if not isinstance(video_card, str):
            raise TypeError("Ошибка. Название видеокарты должно являться строкой.")

        self.processor = processor
        if not isinstance(processor, str):
            raise TypeError("Ошибка. Название процессора должно являться строкой.")

        self.motherboard = motherboard
        if not isinstance(motherboard, str):
            raise TypeError("Ошибка. Название материнской платы должно являться строкой.")

    def compatibility_processor_and_motherboard(self) -> bool:
        """
        Функция которая определяет, совместим ли данный процессор с материнской платой

        :return: Является ли процессор и материнская плата совместимыми

        Пример:
        >>> comp = Computer("GeForce RTX 3060 12 Gb", "Intel Core i7-10700F", "MSI PRO H510M-B")
        >>> comp.compatibility_processor_and_motherboard()
        """
        ...

    def supports_video_card(self) -> bool:
        """
        Функция которая определяет, поддерживает ли данная видеокарта Directx 12

        :return: Поддерживает ли данная видеокарта Directx 12

        Пример:
        >>> comp = Computer("GeForce RTX 3060 12 Gb", "Intel Core i7-10700F", "MSI PRO H510M-B")
        >>> comp.supports_video_card()
        """
        ...


class CompanyShare:
    def ___init___(self, company_name: str, share_price: Union[int, float], dividends: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Акция компании"

        :param company_name: Название компании
        :param share_price: Цена акции
        :param dividends: Дивиденды от 1 акции

        Пример:
        >>> shar = CompanyShare("Сбербанк", 276.03, 25)
        """

        self.company_name = company_name
        if not isinstance(company_name, str):
            raise TypeError("Ошибка. Название компании должно быть строкой.")

        self.share_price = share_price
        if not isinstance(share_price, (int, float)):
            raise TypeError("Ошибка. Цена акции должна быть числом.")
        if share_price < 0:
            raise ValueError("Ошибка. Цена акции должна быть положительным числом.")

        self.dividends = dividends
        if not isinstance(dividends, (int, float)):
            raise TypeError("Ошибка. Дивиденды должны быть числом.")
        if dividends < 0:
            raise ValueError("Ошибка. Дивиденды должны быть положительным числом.")

    def change_share_price_for_day(self, new_price: Union[int, float]) -> str:
        """
        Функция которая определяет насколько изменится цена акции за день

        :param new_price: Новая цена акции

        :return: Цена возрасла/упала на ...

        :raise TypeError: Если новая цена не является числом, то выдаем ошибку
        :raise ValueError: Если новая цена не является положительным числом, то выдаем ошибку

        Пример:
         >>> shar = CompanyShare("Сбербанк", 276.03, 25)
         >>> shar.change_share_price_for_day(270.12)
        """
        ...

    def purchase_of_shares(self, number_of_shares: Union[int, float]) -> Union[int, float]:
        """
        Функция которая определяет цену покупки number_of_shares акций

        :param number_of_shares: Кол-во акций

        :return: Цена покупки акций

        :raise TypeError: Если кол-во акций не является целым числом, то выдаем ошибку.
        :raise ValueError: Если кол-во акций не является целым положительным числом, то выдаем ошибку.

        Пример:
        >>> shar = CompanyShare("Сбербанк", 276.03, 25)
        >>> shar.purchase_of_shares(5)
        """
        ...


class Dice:
    def ___init___(self, number_of_faces: int, number_of_dice: int):
        """
        Создание и подготовка к работе объекта "Игральные кости"

        :param number_of_faces: Кол-во граней кубика
        :param number_of_dice: Кол-во кубиков

        Пример:
        >>> dice = Dice(20, 2)
        """

        self.number_of_faces = number_of_faces
        if not isinstance(number_of_faces, int):
            raise TypeError("Ошибка. Кол-во граней должно быть целым числом.")
        if number_of_faces <= 4:
            raise ValueError("Ошибка. Кол-во граней не должно быть меньше 4.")

        self.number_of_dice = number_of_dice
        if not isinstance(number_of_dice, int):
            raise TypeError("Ошибка. Кол-во кубиков должно быть целым числом.")
        if number_of_dice <= 0:
            raise ValueError("Ошибка. Кол-во кубиков должно быть положительным числом.")

    def max_result(self) -> int:
        """
        Функция расчитывает максимально возможный результат броска кубиков

        :return: Максимальный результат

        Пример:
        >>> dice = Dice(20, 2)
        >>> dice.max_result()
        """
        ...

    def chance_of_falling_out(self, number: int) -> Union[int, float]:
        """
        Функция расчитывает шанс выпадения числа (кол-ва очков) за 1 бросок кубиков

        :param number: Кол-во очков

        :return: Шанс выпадения

        :raise TypeError: Если кол-во очков не является целым числом, то выдаем ошибку
        :raise ValueError: Если кол-во очков меньше кол-ва кубиков (минимально возможный результат),
                           или больше максимально возможного результата, то выдаем ошибку

        Пример:
        >>> dice = Dice(20, 2)
        >>> dice.chance_of_falling_out(13)
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
