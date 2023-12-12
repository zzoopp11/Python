disk_memory_in_mb = 1.44
quantity_pages_in_book = 100
number_lines_on_page = 50
quantity_characters_in_line = 25
memory_for_one_character = 4

memory_for_one_line = quantity_characters_in_line * memory_for_one_character
memory_for_one_page = memory_for_one_line * number_lines_on_page
memory_for_one_book = memory_for_one_page * quantity_pages_in_book

disk_memory_in_bytes = disk_memory_in_mb * 1024 * 1024

quantity_books_in_disk = int(disk_memory_in_bytes // memory_for_one_book)

print("Количество книг, помещающихся на дискету:", quantity_books_in_disk)
