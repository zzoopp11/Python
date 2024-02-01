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


class Book:
    def __init__(self, id_, name, pages):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id_: ID книги
        :param name: Название книги
        :param pages: Кол-во страниц в книге
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


class Library:
    def __init__(self, books=[]):
        """
        Создание и подготовка к работе объекта "Библиотека"

        :param books: Список книг
        """
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Функция возвращает идентификатор для добавления новой книги в библиотеку
        """
        if not self.books:
            id_ = 1
        else:
            id_ = max(book.id_ for book in self.books) + 1
        return id_

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Функция возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса

        :param book_id: индекс книги в списке
        """
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index

        raise ValueError("Ошибка. Книги с запрашиваемым id не существует.")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
