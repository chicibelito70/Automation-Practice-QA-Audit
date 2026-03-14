"""
Helpers reutilizables para el proyecto de automatización.
Contiene utilidades genéricas que pueden ser usadas por múltiples tests y páginas.
"""

import os
from datetime import datetime
from utils.screenshot_manager import ScreenshotManager


def get_timestamp() -> str:
    """
    Genera un timestamp para nombrar archivos de evidencia.
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def ensure_folder(path: str) -> None:
    """
    Crea una carpeta si no existe.

    Args:
        path: Ruta de la carpeta a crear.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def take_screenshot(
    driver,
    name: str,
    evidence_root: str = "Evidencias",
    subfolder: str | None = None,
    default_subfolder: str | None = None,):
    """
    Guarda una captura de pantalla como evidencia.

    Args:
        driver: WebDriver de Selenium.
        name: Nombre base del archivo.
        evidence_root: Carpeta raíz de evidencias.
        subfolder: Carpeta específica del ticket.
        default_subfolder: Carpeta por defecto si no se especifica subfolder.
    """

    folder = subfolder if subfolder else (default_subfolder or "General")
    folder = os.path.join(evidence_root, folder)

    ensure_folder(folder)

    return ScreenshotManager.take_screenshot(driver, name, folder=folder)


def save_page_source(driver, name: str, folder: str = "Evidencias"):
    """
    Guarda el HTML de la página actual.

    Args:
        driver: WebDriver de Selenium.
        name: Nombre del archivo.
        folder: Carpeta donde guardar el HTML.
    """

    ensure_folder(folder)

    file_path = os.path.join(folder, f"{name}.html")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    return file_path


def get_browser_logs(driver):

    try:
        logs = driver.get_log("browser")

        return [
            {
                "level": log["level"],
                "message": log["message"],
                "timestamp": log["timestamp"],
            }
            for log in logs
        ]

    except Exception:
        return []
