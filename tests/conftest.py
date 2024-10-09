import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utills.config import ConfigReader


def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    options = Options()
    options.add_experimental_option("detach", True)  # Keeps the browser open after tests

    driver = webdriver.Chrome(options=options)
    # Assign driver to the test class
    request.cls.driver = driver
    driver.maximize_window()
    url = ConfigReader.read_config("general", "url")
    # driver.get("https://www.next.co.il/en")
    driver.get(url)
    yield
    driver.quit()

    def pytest_sessionfinish() -> None:
        environment_properties = {
            'browser': driver.name,
            'driver_version': driver.capabilities['browserVersion']
        }
        allure_env_path = os.path.join("allure-results", 'environment.properties')
        with open(allure_env_path, 'w') as f:
            data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
            f.write(data)
