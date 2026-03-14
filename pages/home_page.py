from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.helpers import take_screenshot


class HomePage(BasePage):
#locators:
    @classmethod
    def free_strategy_session(cls):
        return (By.XPATH, "//a[text()='Free Strategy Session']")

    @classmethod
    def automation_links(cls):
        return (By.CSS_SELECTOR, ".et_pb_text_inner ul li a")

# Actions:
    def is_strategy_button_present(self):
    ""
    Verifica si el botón 'Free Strategy Session' está presente en el DOM.

    Flujo:
    Obtiene el locator del botón mediante el método free_strategy_session().
    Utiliza el método is_element_present() de BasePage.
    Selenium espera hasta que el elemento esté presente en el DOM.

    Returns:
            True  -> si el botón existe en el DOM.
            False -> si el botón no se encuentra dentro del tiempo de espera.
    ""
    return self.is_element_present(self.free_strategy_session())
    take_screenshot(self.driver, "is_strategy_button_present")


def click_strategy_button(self):
    """
    Realiza un clic en el botón 'Free Strategy Session'.

    Flujo:
        Obtiene el locator botón mediante free_strategy_session.
        Utiliza el método click de BasePage.
        Selenium espera hasta que el elemento sea clickeable.
        Hace scroll al elemento si es necesario.
        Ejecuta el clic.

    Returns:
        None

    Resultado esperado:
        El navegador debe navegar a la página correspondiente después clic.
    """
    self.click(self.free_strategy_session())
    take_screenshot(self.driver, "click_free_strategy_session")
    
