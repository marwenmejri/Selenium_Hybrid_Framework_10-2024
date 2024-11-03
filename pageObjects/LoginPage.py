from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(by=By.ID,value="username").send_keys(username)

    def set_password(self, password):
        self.driver.find_element(by=By.NAME,value="password").send_keys(password)

    def login(self):
        self.driver.find_element(by=By.ID,value="submit").click()

    def logout(self):
        self.driver.find_element(by=By.XPATH, value="(//a[normalize-space()='Log out'])[1]").click()

if __name__ == '__main__':
    url = "https://practicetestautomation.com/practice-test-login/"
    driver_ = Chrome()
    driver_.implicitly_wait(time_to_wait=5)
    driver_.maximize_window()
    driver_.get(url=url)
    time.sleep(2)

    lp = LoginPage(driver=driver_)
    lp.set_username(username="student")
    time.sleep(2)
    lp.set_password(password="Password123")
    time.sleep(2)
    lp.login()
    time.sleep(2)
    lp.logout()

    time.sleep(2)
    driver_.quit()
