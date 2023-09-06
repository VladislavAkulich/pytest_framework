from injector import inject
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class InventoryPage:

    @inject
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.section_lct = "product_label"

    def get_title(self) -> str:
        return self.driver.title

    def get_section_text(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, self.section_lct).text
