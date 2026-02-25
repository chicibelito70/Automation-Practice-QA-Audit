import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from utils.screenshot_manager import ScreenshotManager
from config import BROWSER, CHROME_BINARY, CHROMEDRIVER_PATH, FIREFOX_BINARY, GECKODRIVER_PATH, EDGE_BINARY, EDGEDRIVER_PATH


def _chrome_driver():
    options = webdriver.ChromeOptions()
    if CHROME_BINARY:
        options.binary_location = CHROME_BINARY
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    if CHROMEDRIVER_PATH:
        service = ChromeService(executable_path=CHROMEDRIVER_PATH)
        return webdriver.Chrome(service=service, options=options)
    # Sin ruta: Selenium 4 usa Selenium Manager (evita fallo split de webdriver_manager)
    return webdriver.Chrome(options=options)


def _firefox_driver():
    options = webdriver.FirefoxOptions()
    if FIREFOX_BINARY:
        options.binary_location = FIREFOX_BINARY
    options.set_capability("moz:loggingPrefs", {"browser": "ALL"})
    if GECKODRIVER_PATH:
        service = FirefoxService(executable_path=GECKODRIVER_PATH)
        return webdriver.Firefox(service=service, options=options)
    return webdriver.Firefox(options=options)


def _edge_driver():
    options = webdriver.EdgeOptions()
    if EDGE_BINARY:
        options.binary_location = EDGE_BINARY
    options.set_capability("ms:loggingPrefs", {"browser": "ALL"})
    if EDGEDRIVER_PATH:
        service = EdgeService(executable_path=EDGEDRIVER_PATH)
        return webdriver.Edge(service=service, options=options)
    return webdriver.Edge(options=options)


@pytest.fixture(scope='function')
def driver():
    if BROWSER == 'chrome':
        driver = _chrome_driver()
    elif BROWSER == 'firefox':
        driver = _firefox_driver()
    elif BROWSER == 'edge':
        driver = _edge_driver()
    else:
        raise ValueError(f"Navegador no soportado: {BROWSER}")
    
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='function', autouse=True)
def setup_screenshots(driver):
    ScreenshotManager.delete_old_screenshots()
    ScreenshotManager.take_screenshot(driver, 'test_start')