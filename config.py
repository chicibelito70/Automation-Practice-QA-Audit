# config.py
import os

# URL base por defecto
BASE_URL = "https://ultimateqa.com/"
AUTOMATION_URL = "https://ultimateqa.com/automation"

# Navegador por defecto
BROWSER = os.environ.get("BROWSER", "chrome")

# Rutas de navegador y drivers (opcionales, sin rutas de usuario en el repo).
# Si no se definen, se usa el navegador/driver del sistema o webdriver-manager.
CHROME_BINARY = os.environ.get("CHROME_BINARY")
CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH")

FIREFOX_BINARY = os.environ.get("FIREFOX_BINARY")
GECKODRIVER_PATH = os.environ.get("GECKODRIVER_PATH")

EDGE_BINARY = os.environ.get("EDGE_BINARY")
EDGEDRIVER_PATH = os.environ.get("EDGEDRIVER_PATH")