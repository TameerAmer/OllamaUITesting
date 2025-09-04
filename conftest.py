import os
import allure
import pytest

from dotenv import load_dotenv
import os

# Load variables from .env.compose
load_dotenv(dotenv_path=".env.compose")

def pytest_configure(config):
    os.makedirs("allure-results", exist_ok=True)
    with open("allure-results/environment.properties", "w") as f:
        f.write("Test.Framework=Selenium+Pytest\n")
        f.write("CI.Platform=GitHub Actions\n")
        f.write("Test.Types=UI Automation\n")
        f.write("Browsers=Chrome, Firefox\n")
        f.write("Resolutions=Desktop (1920x1080), Laptop (1366x768), Tablet (1024x768), Mobile (375x667)\n")
        f.write(f"Target.URL={os.environ.get('OLLAMA_URL')}\n")
        f.write(f"Ollama.Version={os.environ.get('OLLAMA_VERSION')}\n")
        f.write(f"Ollama.Image={os.environ.get('OLLAMA_UI_IMG_TAG')}\n")
        f.write(f"YOLO.Version={os.environ.get('YOLO_VERSION')}\n")
        f.write(f"YOLO.Image={os.environ.get('YOLO_IMG_TAG')}\n")
        f.write(f"Postgres.Version={os.environ.get('POSTGRES_VERSION')}\n")



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_call(item):
    """
    Automatically attach labels to each test without repeating them.
    """
    browser = os.environ.get("BROWSER")
    resolution = f"{os.environ.get('SCREEN_WIDTH')}x{os.environ.get('SCREEN_HEIGHT')}"
    environment = os.environ.get("ENVIRONMENT")

    with allure.step("Test metadata"):
        allure.dynamic.label("browser", browser)
        allure.dynamic.label("resolution", resolution)
        allure.dynamic.label("environment", environment)
        allure.dynamic.label("YOLO_VERSION", os.environ.get("YOLO_VERSION"))
        allure.dynamic.label("YOLO_IMG_TAG", os.environ.get("YOLO_IMG_TAG"))
        allure.dynamic.label("OLLAMA_VERSION", os.environ.get("OLLAMA_VERSION"))
        allure.dynamic.label("OLLAMA_UI_IMG_TAG", os.environ.get("OLLAMA_UI_IMG_TAG"))
        allure.dynamic.label("POSTGRES_VERSION", os.environ.get("POSTGRES_VERSION"))

    yield
