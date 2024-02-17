import math


if __name__ == "__main__":
    class FadingOscillations:
        """
        Базовый класс. Данный класс описывает затухающие гармонические колебания различных колебательных контуров

        :param natural_frequency: Собственная круговая(!) частота контура [рад/c]
        :param attenuation_coefficient: Коэффициент затухания [Гц]

        Пример:
        >>> oscillation_1 = FadingOscillations(25.4, 3)
        """
        def __init__(self, natural_frequency: float, attenuation_coefficient: float):
            self.natural_frequency = natural_frequency
            self.check(natural_frequency)
            self.attenuation_coefficient = attenuation_coefficient
            self.check(attenuation_coefficient)
            if natural_frequency < attenuation_coefficient:
                raise ValueError("Колебания являются вырожденными.")

        @staticmethod
        def check(parameter: float) -> None:
            """
            Функция, которая проверяет, является ли параметр положительным числом

            :param parameter: Проверяемый параметр

            :raise TypeError: Если параметр не является числом, то вызываем ошибку
            :raise ValueError: Если параметр является отрицательным числом, то вызываем ошибку
            """

            if not isinstance(parameter, (int, float)):
                raise TypeError(f"{parameter} должен быть типа 'float' или 'int'.")
            if parameter < 0:
                raise ValueError(f"Число {parameter} должно быть положительным.")

        def system_frequency(self) -> float:
            """
            Функция считает частоту затухающих колебаний

            :return: Частота затухающих колебаний [рад/c]

            Пример:
            >>> oscillation_1 = FadingOscillations(25.4, 3)
            >>> oscillation_1.system_frequency()
            """

            system_frequency = math.sqrt(self.natural_frequency ** 2 - self.attenuation_coefficient ** 2)
            return round(system_frequency, 2)

        def period(self) -> float:
            """
            Функция считает период колебаний

            :return: Период колебаний [c]

            Пример:
            >>> oscillation_1 = FadingOscillations(25.4, 3)
            >>> oscillation_1.period()
            """

            period = 2 * math.pi/self.system_frequency()
            return round(period, 6)

        def quality(self) -> int:
            """
            Функция считает добротность контура

            :return: Добротность контура

            Пример:
            >>> oscillation_1 = FadingOscillations(25.4, 3)
            >>> oscillation_1.quality()
            """

            quality = math.pi/(self.attenuation_coefficient * self.period())
            return int(quality)

        def __str__(self) -> str:
            return f'Круговая частота собственных колебаний контура - {self.natural_frequency} рад/c,' \
                   f' коэффициент затухания - {self.attenuation_coefficient} Гц.'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(natural_frequency={self.natural_frequency!r}, ' \
                   f'attenuation_coefficient={self.attenuation_coefficient!r} '


    class ForcedOscillations(FadingOscillations):
        """
        Производный класс. Данный класс описывает колебания под действием внешней периодической силы

        :param force_frequency: Круговая(!) частота внешней силы

        Пример:
        >>> oscillation_2 = ForcedOscillations(100, 9, 130)
        """

        def __init__(self, natural_frequency: float, attenuation_coefficient: float, force_frequency: float):
            super().__init__(natural_frequency, attenuation_coefficient)
            self.force_frequency = force_frequency
            self.check(force_frequency)

        def system_frequency(self) -> float:
            """
            Функция считает частоту колебаний. Данный метод перегружен, поскольку изменилась формула подсчета

            :return: Частота колебаний [рад/c]

            Пример:
            >>> oscillation_2 = ForcedOscillations(100, 9, 130)
            >>> oscillation_2.system_frequency()
            """

            system_frequency = math.sqrt(((self.natural_frequency ** 2 - self.force_frequency ** 2) ** 2) +
                                         4 * (self.attenuation_coefficient ** 2) * (self.force_frequency ** 2))
            return round(system_frequency, 4)

        def resonant_frequency(self) -> float:
            """
            Функция считает частоту резонанса

            :return: Частота резонанса [рад/c]

            Пример:
            >>> oscillation_2 = ForcedOscillations(100, 9, 130)
            >>> oscillation_2.resonant_frequency()
            """

            resonant_frequency = math.sqrt(self.natural_frequency ** 2 - 2 * (self.attenuation_coefficient ** 2))
            return round(resonant_frequency, 2)

        def __str__(self) -> str:
            return f'Круговая частота собственных колебаний контура - {self.natural_frequency} рад/c,' \
                   f' коэффициент затухания - {self.attenuation_coefficient} Гц,' \
                   f' круговая частота вынуждающей силы - {self.force_frequency} рад/c.'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(natural_frequency={self.natural_frequency!r}, attenuation_coefficient' \
                   f'={self.attenuation_coefficient!r}, force_frequency={self.force_frequency!r})'
