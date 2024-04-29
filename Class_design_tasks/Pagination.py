'''
Implement the Pagination class to handle paginated data. Paging is used to divide large amounts of data into parts. An instance of the Pagination class must be created based on two values:

source data presented as a list with arbitrary elements
page size, that is, the number of elements displayed on each page
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
The get_visible_items() method should be used to get the page content:

print(pagination.get_visible_items()) # ['a', 'b', 'c', 'd']
Please note that the page content must be presented as a list. Navigation through pages should be done using the following methods:

prev_page() - return to the previous page
next_page() - go to the next page
first_page() - return to the first page
last_page() - go to the last page
go_to_page() - go to the page with the specified number (1 - first page, 2 - second page, and so on)
pagination.next_page()
print(pagination.get_visible_items()) # ['e', 'f', 'g', 'h']

pagination.last_page()
print(pagination.get_visible_items()) # ['y', 'z']
Methods for moving through pages must be applied one after another:

pagination.first_page()
pagination.next_page().next_page()
print(pagination.get_visible_items()) # ['i', 'j', 'k', 'l']
Using the total_pages and current_page attributes it should be possible to get the total number of pages and the current page respectively:

print(pagination.total_pages) #7
print(pagination.current_page) #3
When you are on the first page and move to the previous page, the current page should remain the first page.
Similarly, when you are on the last page and move to the next page, the current page should remain the last page:

pagination.first_page()
pagination.prev_page()
print(pagination.get_visible_items()) # ['a', 'b', 'c', 'd']

pagination.last_page()
pagination.next_page()
print(pagination.get_visible_items()) # ['y', 'z']
When moving to page zero or less, the current page must be the first page. Likewise, when moving to a page whose
number exceeds the total number of pages, the current page should be the last page:

pagination.go_to_page(-100)
print(pagination.get_visible_items()) # ['a', 'b', 'c', 'd']

pagination.go_to_page(100)
print(pagination.get_visible_items()) # ['y', 'z']
'''

class Pagination:
    def __init__(self, data, page_size):
        self.data = data
        self.page_size = page_size
        self.current_page = 1
        self.total_pages = (len(data) + page_size - 1) // page_size

    def get_visible_items(self):
        start_index = (self.current_page - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.data[start_index:end_index]

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        return self

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, page_number):
        if page_number < 1:
            self.current_page = 1
        elif page_number > self.total_pages:
            self.current_page = self.total_pages
        else:
            self.current_page = page_number
        return self