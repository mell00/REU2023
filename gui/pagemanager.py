class PageManager:
    def __init__(self):
        self.pages = {}

    def add_page(self, page_name, page_class):
        self.pages[page_name] = page_class

    def get_page(self, page_name):
        return self.pages.get(page_name, None)
