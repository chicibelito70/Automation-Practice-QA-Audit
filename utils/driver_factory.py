from selenium import webdriver


def create_driver(browser):

    if browser == "chrome":
        return webdriver.Chrome()

    if browser == "firefox":
        return webdriver.Firefox()

    if browser == "edge":
        return webdriver.Edge()

    raise ValueError("Browser no soportado")
