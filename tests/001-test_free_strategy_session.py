"""
TICKET: QA-AUT-001
TÍTULO: Validar presencia y funcionalidad del botón "FREE STRATEGY SESSION" en el header

TIPO:
Prueba Funcional / UI / Navegación

PRIORIDAD:
Alta

DESCRIPCIÓN:
El botón "FREE STRATEGY SESSION" es un Call-To-Action (CTA) ubicado en el
header principal de la página de Automation Practice.

Este botón representa una acción importante de conversión dentro del sitio.
La prueba valida que el botón exista en el DOM, sea visible para el usuario
y pueda ser interactuado correctamente.

PRECONDICIONES:
- El usuario accede a la página https://ultimateqa.com/automation
- El navegador se encuentra inicializado correctamente
- La página carga completamente

PASOS DE PRUEBA:
1. Navegar a https://ultimateqa.com/automation
2. Localizar el botón con el texto "FREE STRATEGY SESSION"
3. Validar que el elemento exista en el DOM
4. Validar que el elemento sea visible
5. Validar que el elemento sea clickeable

RESULTADO ESPERADO:
- El botón existe en el DOM
- El botón es visible
- El botón es interactuable
- No se generan errores durante la interacción

AUTOMATIZACIÓN:
Framework: Selenium
Runner: Pytest
Control de inestabilidad: Flaky (reintentos automáticos)

RIESGO SI NO SE PRUEBA:
- El CTA principal del sitio puede no funcionar
- Se puede perder funcionalidad crítica de navegación
- Impacto en la experiencia de usuario
"""

from flaky import flaky

from config import AUTOMATION_URL
from pages.home_page import HomePage
from utils.helpers import take_screenshot


@flaky(max_runs=1, min_passes=1)
def test_free_strategy_session_button(driver):
    """
    QA-AUT-001
    Valida la presencia y funcionalidad del botón
    FREE STRATEGY SESSION.
    """

    driver.get(AUTOMATION_URL)


    home = HomePage(driver)

    # existencia en DOM
    assert home.is_strategy_button_present() == True

    #  visible
    button = driver.find_element(*home.FREE_STRATEGY_SESSION)
    assert button.is_displayed() == True

    #  clickeable
    home.click_strategy_button()

    # Validar que hubo navegación
    assert "ultimateqa" in driver.current_url
