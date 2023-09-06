from injector import Module, singleton, provider
from selenium.webdriver.chrome.webdriver import WebDriver

from app_pages.inventory_page import InventoryPage
from app_pages.login_page import LoginPage


class LoginPageModule(Module):
    @provider
    @singleton
    def provide_login_page(self, driver: WebDriver) -> LoginPage:
        return LoginPage(driver)


class InventoryPageModule(Module):
    @provider
    @singleton
    def provide_inventory_page(self, driver: WebDriver) -> InventoryPage:
        return InventoryPage(driver)
