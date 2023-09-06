from injector import Module, provider, singleton

from actions.inventory.inventory import InventoryActions
from actions.login.login import LoginActions
from app_pages.inventory_page import InventoryPage
from app_pages.login_page import LoginPage


class LoginActionsModule(Module):
    @provider
    @singleton
    def provide_login_page(self, login_page: LoginPage) -> LoginActions:
        return LoginActions(login_page)


class InventoryActionsModule(Module):
    @provider
    @singleton
    def provide_login_page(self, inventory_page: InventoryPage) -> InventoryActions:
        return InventoryActions(inventory_page)
