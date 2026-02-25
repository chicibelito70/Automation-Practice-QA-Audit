"""Page Object de la página principal (Automation Practice)."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class HomePage(BasePage):
    """Página Automation Practice - ultimateqa.com/automation."""

    FREE_STRATEGY_SESSION = (By.XPATH, "//a[contains(., 'Strategy')]")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def click_free_strategy_session(
        self,
        evidence_name: str = "click_free_strategy_session",
        capture: bool = True,
        evidence_subfolder: str | None = None,
    ) -> None:
        """Hace clic en el botón Free Strategy Session del header."""
        self.click(self.FREE_STRATEGY_SESSION, evidence_name=evidence_name,
                   capture=capture, evidence_subfolder=evidence_subfolder)

    def is_button_present(
        self,
        evidence_name: str = "verify_free_strategy_session",
        capture: bool = True,
        evidence_subfolder: str | None = None,
    ) -> bool:
        """Comprueba si el botón Free Strategy Session está visible."""
        return self.is_element_present(
            self.FREE_STRATEGY_SESSION,
            evidence_name=evidence_name,
            capture=capture,
            evidence_subfolder=evidence_subfolder,
        )