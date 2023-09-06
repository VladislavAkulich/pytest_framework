from injector import inject
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:

    @inject
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_lct = "user-name"
        self.password_lct = "password"
        self.login_btn_lct = "login-button"

    def open(self) -> None:
        self.driver.get("https://www.saucedemo.com/v1/")

    def set_username(self, username) -> None:
        self.driver.find_element(By.ID, self.username_lct).send_keys(username)

    def set_password(self, password) -> None:
        self.driver.find_element(By.ID, self.password_lct).send_keys(password)

    def click_login_btn(self) -> None:
        self.driver.find_element(By.ID, self.login_btn_lct).click()

