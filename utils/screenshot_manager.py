import os
import shutil
from datetime import datetime

class ScreenshotManager:
    @staticmethod
    def delete_old_screenshots(folder='screenshots'):
        if os.path.exists(folder):
            shutil.rmtree(folder)
            os.makedirs(folder)

    @staticmethod
    def take_screenshot(driver, name, folder='screenshots'):
        if not os.path.exists(folder):
            os.makedirs(folder)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{name}_{timestamp}.png"
        path = os.path.join(folder, filename)
        driver.save_screenshot(path)
        return path