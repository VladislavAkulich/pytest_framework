from injector import Injector

from actions.actions_module import InventoryActionsModule, LoginActionsModule
from actions.inventory.inventory import InventoryActions
from actions.login.login import LoginActions
from app_pages.pages_module import LoginPageModule, InventoryPageModule
from core.driver import DriverModule

injector = Injector([DriverModule, LoginPageModule, InventoryPageModule,
                     LoginActionsModule, InventoryActionsModule])
login_actions = injector.get(LoginActions)
inventory_actions = injector.get(InventoryActions)


def test_login(valid_user):
    login_actions.login_with_user(valid_user)
    assert inventory_actions.is_it_inventory("Swag Labs", "Products")


