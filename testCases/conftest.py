import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope="class")
def setup():
    driver = Chrome()
    driver.implicitly_wait(time_to_wait=5)
    driver.maximize_window()
    yield driver
    driver.quit()


# @pytest.fixture(scope="function")
# def setup():
#     driver = Chrome()
#     driver.implicitly_wait(time_to_wait=5)
#     driver.maximize_window()
#     return driver
