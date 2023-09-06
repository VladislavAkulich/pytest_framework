from injector import inject

from app_pages.login_page import LoginPage
from dto.test_user import TestUser


class LoginActions:

    @inject
    def __init__(self, login_page: LoginPage):
        self.__login_page = login_page

    def login_with_user(self, user: TestUser):
        self.__login_page.open()
        self.__login_page.set_username(user.username)
        self.__login_page.set_password(user.password)
        self.__login_page.click_login_btn()
