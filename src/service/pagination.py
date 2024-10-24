class Pagination:
    def __init__(self, items, page_size, page_number):
        self.items = items
        self.page_size = page_size
        self.page_number = page_number

    def paginate(self):
        start_index = (self.page_number - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.items[start_index:end_index]

    def get_max_pages(self):
        return (len(self.items) + self.page_size - 1) // self.page_size


items = ["Егор", "Петр", "Макс", "Дима", "Маша", "Саша", "Коля", "Олег", "Света", "Кеша"]
page_size = 3
page_number = 1

pagination = Pagination(items, page_size, page_number)

print(f"Страница {page_number}: {pagination.paginate()}")
print(pagination.get_max_pages())
