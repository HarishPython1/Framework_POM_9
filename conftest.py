import pytest
import os
from testdata import data as data


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='test help')


@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    browser = "chrome"  # request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\BTM-Faculty\\PycharmProjects\\Framework_POM_9\\drivers\\chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.get(data.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.quit()
