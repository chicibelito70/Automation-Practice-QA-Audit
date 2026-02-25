"""
Helpers reutilizables para el proyecto de automatización.
"""
import os
from utils.screenshot_manager import ScreenshotManager


def take_screenshot(driver, name: str, evidence_root: str = "Evidencias",
                    subfolder: str | None = None, default_subfolder: str | None = None):
    """
    Guarda una captura de pantalla como evidencia.

    Args:
        driver: WebDriver de Selenium.
        name: Nombre base del archivo (se añade timestamp automático).
        evidence_root: Carpeta raíz de evidencias (por defecto "Evidencias").
        subfolder: Subcarpeta específica (ej. "Ticket1_FreeStrategySession").
        default_subfolder: Subcarpeta por defecto si subfolder es None (ej. nombre de la página).
    """
    folder = subfolder if subfolder else (default_subfolder or "General")
    folder = os.path.join(evidence_root, folder)
    return ScreenshotManager.take_screenshot(driver, name, folder=folder)
