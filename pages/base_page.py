"""Clase base para Page Objects con Selenium."""
from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

from utils.helpers import take_screenshot as _take_screenshot_helper


class BasePage:
    """Clase base con operaciones comunes para todas las páginas."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
        self._evidence_root = "Evidencias"
        self._evidence_subfolder = self.__class__.__name__

    def _take_evidence(self, action_name: str, subfolder: str | None = None):
        """Guarda captura en Evidencias/{subfolder}/{action_name}_*.png"""
        _take_screenshot_helper(
            self.driver, action_name,
            evidence_root=self._evidence_root,
            subfolder=subfolder,
            default_subfolder=self._evidence_subfolder
        )

    def go_to_url(self, url, capture: bool = True, evidence_name: str = "go_to_url", evidence_subfolder: str | None = None):
        self.driver.get(url)
        if capture:
            self._take_evidence(evidence_name, evidence_subfolder)

    def click(self, locator, evidence_name: str = "click", capture: bool = True, evidence_subfolder: str | None = None):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        if capture:
            self._take_evidence(evidence_name, evidence_subfolder)

    def send_keys(self, locator, text, evidence_name: str = "send_keys", capture: bool = True, evidence_subfolder: str | None = None):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        if capture:
            self._take_evidence(evidence_name, evidence_subfolder)

    def is_element_present(
        self,
        locator: Tuple[str, str],
        evidence_name: str = "verify_element",
        capture: bool = True,
        evidence_subfolder: str | None = None,
    ) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            if capture:
                self._take_evidence(evidence_name, evidence_subfolder)
            return True
        except TimeoutException:
            if capture:
                self._take_evidence(f"{evidence_name}_fail", evidence_subfolder)
            return False

    def scroll_to_element(self, locator, evidence_name: str = "scroll", capture: bool = True, evidence_subfolder: str | None = None):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        if capture:
            self._take_evidence(evidence_name, evidence_subfolder)

    def wait_for_url_contains(self, text, capture: bool = True, evidence_name: str = "wait_for_url", evidence_subfolder: str | None = None):
        self.wait.until(EC.url_contains(text))
        if capture:
            self._take_evidence(evidence_name, evidence_subfolder)