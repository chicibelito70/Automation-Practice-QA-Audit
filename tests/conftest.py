"""Fixtures compartidos de pytest."""
import pytest
from selenium import webdriver

from config import BROWSER
from utils.driver_factory import create_driver


@pytest.fixture(scope="function")
def driver():

    driver = create_driver(BROWSER)

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def setup_screenshots(driver):
    """Captura inicial al iniciar cada test."""
    from utils.helpers import take_screenshot
    take_screenshot(driver, "test_start", subfolder="Inicio")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            from utils.helpers import take_screenshot

            test_name = item.name

            take_screenshot(driver, test_name, subfolder="Errores")

