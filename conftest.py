import os
import allure
import pytest

def pytest_configure(config):
    """
    Called once before running tests.
    Here we write environment properties for Allure.
    """
    os.makedirs("allure-results", exist_ok=True)
    with open("allure-results/environment.properties", "w") as f:
        f.write(f"Browser={os.environ.get('BROWSER')}\n")
        f.write(f"Resolution={os.environ.get('SCREEN_WIDTH')}x{os.environ.get('SCREEN_HEIGHT')}\n")
        f.write(f"Environment={os.environ.get('ENVIRONMENT')}\n")
        f.write(f"YOLO_VERSION={os.environ.get('YOLO_VERSION')}\n")
        f.write(f"YOLO_IMG_TAG={os.environ.get('YOLO_IMG_TAG')}\n")
        f.write(f"OLLAMA_VERSION={os.environ.get('OLLAMA_VERSION')}\n")
        f.write(f"OLLAMA_UI_IMG_TAG={os.environ.get('OLLAMA_UI_IMG_TAG')}\n")
        f.write(f"POSTGRES_VERSION={os.environ.get('POSTGRES_VERSION')}\n")


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
