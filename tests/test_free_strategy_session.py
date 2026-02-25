"""Test Ticket 1: Botón FREE STRATEGY SESSION en https://ultimateqa.com/automation"""
import requests
from flaky import flaky

from config import AUTOMATION_URL
from pages.home_page import HomePage
from utils.helpers import take_screenshot

EVIDENCE_SUBFOLDER = "Ticket1_FreeStrategySession"


@flaky(max_runs=3, min_passes=1)
def test_free_strategy_session_button(driver):
    """
    Valida: presencia del botón, clic, URL correcta, HTTP 200.
    Precondiciones: usuario no autenticado.
    """
    home = HomePage(driver)
    ev = {"evidence_subfolder": EVIDENCE_SUBFOLDER}

    # 1. Acceder a la página principal
    home.go_to_url(AUTOMATION_URL, evidence_name="01_navegacion_inicial", **ev)
    home.wait_for_url_contains("ultimateqa.com", evidence_name="02_espera_url", **ev)

    # 2. Validar que el botón existe
    assert home.is_button_present(
        evidence_name="03_verificar_boton_presente", **ev
    ), "El botón FREE STRATEGY SESSION no está presente"

    driver.get_log("browser")

    # 3. Click en FREE STRATEGY SESSION
    home.click_free_strategy_session(
        evidence_name="04_click_free_strategy_session", **ev
    )

    # Si abre en nueva pestaña, cambiar a ella
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])

    # 4. Validar URL y HTTP 200
    current_url = driver.current_url
    assert current_url.startswith(AUTOMATION_URL), f"URL inesperada: {current_url}"
    response = requests.get(current_url, timeout=10)
    assert response.status_code == 200, (
        f"La página destino respondió {response.status_code}, se esperaba 200"
    )

    # 5. Evidencia final
    take_screenshot(driver, "05_resultado_final", subfolder=EVIDENCE_SUBFOLDER)
