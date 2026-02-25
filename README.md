## Automation Practice QA Audit

Este repositorio recoge mis pruebas automatizadas sobre la página **Automation Practice** de Ultimate QA (`https://ultimateqa.com/automation`).  
La idea es tener un proyecto sencillo pero ordenado, que me sirva como práctica de automatización y, al mismo tiempo, como base para ir añadiendo más escenarios poco a poco.

### Tecnologías y dependencias

- **Lenguaje**: Python 3
- **Framework de testing**: `pytest`
- **Automatización web**: `selenium`
- **HTTP simple para validaciones de estado**: `requests`
- **Reportes HTML**: `pytest-html`
- **Utilidad de reintentos**: `flaky`

Todas las dependencias están listadas en `requirements.txt`. La instalación básica es:

```bash
pip install -r requirements.txt
```

### Estructura principal del proyecto

- **`config.py`**  
  Define la configuración básica del proyecto:
  - `BASE_URL` y `AUTOMATION_URL` con las URLs que se usan en las pruebas.
  - `BROWSER`, que indica con qué navegador quiero ejecutar (por defecto `chrome`).
  - Variables que permiten definir rutas de binarios y drivers mediante variables de entorno (`CHROME_BINARY`, `CHROMEDRIVER_PATH`, `GECKODRIVER_PATH`, etc.), evitando dejar rutas locales hardcodeadas en el código.

- **`tests/conftest.py`**  
  Aquí está toda la preparación común de los tests:
  - Fixture `driver` que crea el WebDriver en función del valor de `BROWSER` (`chrome`, `firefox` o `edge`).
  - Si hay una ruta de driver configurada en las variables de entorno, la utiliza; si no, deja que **Selenium Manager** (incluido en Selenium 4) resuelva el driver automáticamente.
  - Fixture `setup_screenshots` (autouse) que limpia la carpeta `screenshots/` antes de cada prueba y toma una captura inicial.

- **`tests/test_free_strategy_session.py`**  
  Contiene el escenario automatizado del Ticket 1. El test se apoya en la clase `HomePage` para interactuar con la UI y en `requests` para comprobar el código de respuesta de la URL.

- **`pages/base_page.py` y `pages/home_page.py`**  
  - `BasePage` concentra las operaciones genéricas sobre Selenium: navegar a una URL, hacer clic, esperar a que un elemento sea visible, esperar a que la URL contenga un texto, etc.
  - `HomePage` representa la página de Automation Practice y, de momento, expone el localizador y los métodos para trabajar con el botón `FREE STRATEGY SESSION`.

- **`utils/screenshot_manager.py`**  
  Pequeña utilidad para gestionar capturas de pantalla: borra las anteriores y crea archivos con timestamp dentro de la carpeta `screenshots/`.

### Cómo ejecutar las pruebas

1. Crear y activar un entorno virtual (opcional pero recomendable).
2. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Desde la raíz del proyecto, lanzar el test actual:

   ```bash
   pytest tests/test_free_strategy_session.py -v
   ```

Por defecto se ejecutará en Chrome. Si quiero cambiar de navegador, puedo hacerlo con la variable de entorno `BROWSER`. Ejemplo en PowerShell:

```powershell
$env:BROWSER = "firefox"
pytest tests/test_free_strategy_session.py -v
```

### Gestión de capturas y archivos locales

Este repositorio no guarda artefactos generados en las ejecuciones ni configuraciones locales del entorno.  
Para eso se añadió un `.gitignore` con las siguientes exclusiones principales:

- Directorios de entorno y posibles secretos: `venv/`, `env/`, `.env`, `*.env`
- Archivos generados por Python/pytest: `__pycache__/`, `.pytest_cache/`, `*.pyc`
- Configuración de IDEs y herramientas: `.vscode/`, `.idea/`, `.cursor/`
- Evidencias y logs: `screenshots/`, `*.log`

De esta forma, el historial del repositorio se centra solo en el código de automatización y no en datos locales o sensibles.

### Próximos pasos (ideas)

Algunas cosas que tengo en mente para continuar con el proyecto:

- Añadir más casos alrededor del botón `FREE STRATEGY SESSION` (por ejemplo, comportamiento en mobile, comprobación del contenido real de la página de destino, etc.).
- Automatizar otros enlaces de `https://ultimateqa.com/automation` (formularios, landing pages de prueba, páginas con muchos elementos).
- Integrar reportes HTML de pytest de forma más formal (configuración de salida, carpeta dedicada de reportes).
- Ajustar las aserciones de consola para filtrar errores conocidos propios del sitio y resaltar solo errores nuevos o inesperados.

Este README resume el estado actual del proyecto y me sirve como referencia rápida de lo que ya está montado y hacia dónde quiero seguir avanzando.