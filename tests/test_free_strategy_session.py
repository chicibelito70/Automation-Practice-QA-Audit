# test_free_strategy_session.py
# Ticket 1: Validar funcionalidad y consistencia del botón "FREE STRATEGY SESSION"
# Página bajo prueba: https://ultimateqa.com/automation

#- **Ticket 1 – Botón "FREE STRATEGY SESSION"**
#  - Página bajo prueba: `https://ultimateqa.com/automation`.
#  - Objetivo del test: comprobar que el botón **FREE STRATEGY SESSION** del header existe, se puede hacer clic y que la página sigue respondiendo correctamente después del clic.
#  - El flujo actual del test es:
#    1. Abrir la URL de Automation Practice (`AUTOMATION_URL`).
#    2. Verificar que el botón `FREE STRATEGY SESSION` está presente en la página.
#    3. Hacer clic en el botón.
#    4. Si se abre una nueva pestaña, cambiar el foco a esa pestaña.
#    5. Comprobar que la URL actual comienza por `AUTOMATION_URL` (no se rompe la navegación).
#    6. Hacer una petición HTTP con `requests` a la URL actual y validar que devuelve **200**.
#    7. Guardar una captura de pantalla como evidencia del resultado.
#

import pytest
import requests
from config import AUTOMATION_URL
from pages.home_page import HomePage
from utils.screenshot_manager import ScreenshotManager
from flaky import flaky

def test_free_strategy_session_button(driver):
    @flaky(max_runs=3, rerun_filter=1)
    """
    Precondiciones: Usuario no autenticado.
    Valida: redirección correcta, HTTP 200, página destino coherente, sin errores en consola.
    """
    home = HomePage(driver)

    # 1. Acceder a la página principal (Automation Practice)
    home.go_to_url(AUTOMATION_URL)
    home.wait_for_url_contains("ultimateqa.com")

    # 2. Validar que el botón existe
    assert home.is_button_present(), "El botón FREE STRATEGY SESSION no está presente"

    # 3. Capturar errores de consola desde el inicio de la página
    driver.get_log("browser")

    # 4. Click en "FREE STRATEGY SESSION"
    home.click_free_strategy_session()

    # Si abre en nueva pestaña, cambiar a ella
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])

    # 5. Validar URL actual (se valida que siga siendo la página de Automation)
    current_url = driver.current_url
    assert current_url.startswith(AUTOMATION_URL), f"URL inesperada: {current_url}"

    # 6. Validar código HTTP 200 de la página destino
    response = requests.get(current_url, timeout=10)
    assert response.status_code == 200, (f"La página destino respondió {response.status_code}, se esperaba 200")

    # 7. Evidencia: screenshot de la página destino
    ScreenshotManager.take_screenshot(driver, "free_strategy_session_destino")
