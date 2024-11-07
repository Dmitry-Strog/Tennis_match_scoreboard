class Pagination:
    PAGE_SIZE = 3

    def __init__(self, queryset, page_number=1):
        self.__queryset = queryset
        self.__page_number = page_number
        self.__validate_page()

    @property
    def page_number(self):
        return self.__page_number

    def paginate(self):
        self.__validate_page()
        start_index = (self.__page_number - 1) * self.PAGE_SIZE
        end_index = start_index + self.PAGE_SIZE
        return self.__queryset[start_index:end_index]

    def get_max_pages(self):
        return (len(self.__queryset) + self.PAGE_SIZE - 1) // self.PAGE_SIZE

    def __validate_page(self):
        if not 1 <= self.__page_number <= self.get_max_pages():
            self.__page_number = 1

    def has_next_page(self):
        return self.__page_number < self.get_max_pages()

    def has_previous_page(self):
        return self.__page_number > 1

    def next_page(self):
        self.__validate_page()
        self.__page_number += 1
        return self.__page_number

    def previous_page(self):
        self.__validate_page()
        self.__page_number -= 1
        return self.__page_number

