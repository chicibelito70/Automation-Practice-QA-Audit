"""
TICKET: QA-AUT-002
TÍTULO: Validar que los enlaces de la sección "Automation Practice" redirijan correctamente

TIPO:
Prueba Funcional / Navegación / Integración

PRIORIDAD:
Alta

DESCRIPCIÓN:
La página de Automation Practice contiene una lista de enlaces que redirigen
a diferentes ejercicios de automatización. Estos enlaces son parte fundamental
del contenido del sitio.

Esta prueba valida que cada enlace:

- Exista en el DOM
- Sea visible para el usuario
- Sea clickeable
- Redirija correctamente a la página correspondiente

PRECONDICIONES:
- El navegador se encuentra inicializado
- El usuario accede a https://ultimateqa.com/automation
- La página carga completamente

PASOS DE PRUEBA:
1. Navegar a https://ultimateqa.com/automation
2. Ubicar la sección "Automation Practice"
3. Localizar los enlaces de práctica disponibles
4. Hacer clic en cada enlace
5. Validar que la navegación se realice correctamente

ENLACES A VALIDAR:
- Big page with many elements
- Fake Landing Page
- Fake Pricing Page
- Fill out forms
- Learn how to automate an application that evolves over time
- Login automation
- Interactions with simple elements

RESULTADO ESPERADO:
- Cada enlace debe ser visible
- Cada enlace debe ser clickeable
- Cada enlace debe redirigir a una página válida
- La página destino debe cargar sin errores

AUTOMATIZACIÓN:
Framework: Selenium
Runner: Pytest
Control de inestabilidad: Flaky (reintentos automáticos)

RIESGO SI NO SE PRUEBA:
- Enlaces rotos
- Navegación incorrecta
- Pérdida de funcionalidad principal del sitio
"""

import requests
from flaky import flaky

from config import AUTOMATION_URL
from pages.home_page import HomePage
from utils.helpers import take_screenshot


@flaky(max_runs=1, min_passes=1)
def test_enlaces_automation_practice(driver):

    # Inicializar Page Object
    home = HomePage(driver)

    # Paso 1 del ticket:
    # Navegar a la página de Automation Practice
    driver.get(AUTOMATION_URL)

    # Paso 2 y 3 del ticket:
    # Ubicar la sección y obtener los enlaces disponibles
    enlaces = home.get_automation_links()

    # Validar que existan enlaces en el DOM
    assert len(enlaces) > 0

    # Iterar sobre cada enlace encontrado
    for enlace in enlaces:

        # Validar que el enlace sea visible para el usuario
        assert enlace.is_displayed() == True

        # Guardar el texto del enlace (sirve para debugging y evidencias)
        texto = enlace.text

        # Validar que el enlace sea interactuable haciendo click
        enlace.click()

        # Paso 5 del ticket:
        # Validar que hubo navegación y que no seguimos en la página inicial
        assert driver.current_url != AUTOMATION_URL

        # Regresar a la página anterior para continuar con el siguiente enlace
        driver.back()
