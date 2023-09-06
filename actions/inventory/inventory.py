from injector import inject

from app_pages.inventory_page import InventoryPage


class InventoryActions:

    @inject
    def __init__(self, inventory_page: InventoryPage):
        self.inventory_page = inventory_page

    def is_it_inventory(self, title: str, section_name: str) -> bool:
        return self.inventory_page.get_title() == title and self.inventory_page.get_section_text() == section_name
