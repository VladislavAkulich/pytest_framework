from selenium import webdriver
from injector import Module, singleton, provider
from selenium.webdriver.chrome.webdriver import WebDriver


class DriverModule(Module):

    @singleton
    @provider
    def provide_driver(self) -> WebDriver:
        return webdriver.Chrome()
