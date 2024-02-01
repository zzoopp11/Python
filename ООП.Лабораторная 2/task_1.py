import doctest


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id_: ID книги
        :param name: Название книги
        :param pages: Кол-во страниц в книге

        Пример:
        >>> book_ = Book(3, "Война и мир", 1300)
        """

        if not isinstance(id_, int):
            raise TypeError("Ошибка. ID книги должен быть целым числом.")
        if id_ < 0:
            raise ValueError("Ошибка. ID книги должен быть положительным числом.")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Ошибка. Название книги должно быть строкой.")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Ошибка. Кол-во страниц в книге должно быть целым числом.")
        if pages <= 0:
            raise ValueError("Ошибка. Кол-во страниц в книге должно быть положительным числом.")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    doctest.testmod()  # Проверяем работоспособность экземпляров класса

    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
