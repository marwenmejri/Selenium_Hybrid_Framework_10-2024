import time
from utilities.customLogger import sample_logger
from pageObjects.LoginPage import LoginPage


class Test001Login:
    baseURL = "https://practicetestautomation.com/practice-test-login/"
    username = "student"
    password = "Password123"
    logger = sample_logger(filename='Logs/logs.log', mode='a', name='custom_logger1')

    def test_login_page_title(self, setup):
        self.logger.info("************ Test001Login ************")
        self.logger.info("************ test_login_page_title STARTED ************")
        driver = setup
        driver.get(url=self.baseURL)
        time.sleep(2)
        expected_title = "Test Login | Practice Test Automation"
        if driver.title == expected_title:
            self.logger.info("************ test_login_page_title PASSED ************")
            # driver.quit()
            assert True
        else:
            driver.save_screenshot(filename="Screenshots/test_login_page_title.png")
            self.logger.error("************ test_login_page_title FAILED ************")
            # driver.quit()
            assert False

    def test_login_positive(self, setup):
        self.logger.info("************ test_login_positive STARTED ************")
        driver = setup
        driver.get(url=self.baseURL)
        time.sleep(2)

        lp = LoginPage(driver=driver)
        lp.set_username(username=self.username)
        time.sleep(2)
        lp.set_password(password=self.password)
        time.sleep(2)
        lp.login()
        time.sleep(2)

        new_page_url = driver.current_url
        expected_string_url = "practicetestautomation.com/logged-in-successfully/"
        if expected_string_url in new_page_url:
            lp.logout()
            time.sleep(2)
            self.logger.info("************ test_login_positive PASSED ************")
            # driver.quit()
            assert True
        else:
            time.sleep(2)
            driver.save_screenshot(filename="Screenshots/test_login_positive.png")
            self.logger.error("************ test_login_positive FAILED ************")
            # driver.quit()
            assert False

    def test_negative_username(self, setup):
        self.logger.info("************ test_negative_username STARTED ************")
        driver = setup
        driver.get(url=self.baseURL)
        time.sleep(2)

        lp = LoginPage(driver=driver)
        lp.set_username(username="incorrectUser")
        time.sleep(2)
        lp.set_password(password=self.password)
        time.sleep(2)
        lp.login()
        time.sleep(2)

        if "Your username is invalid!" in driver.page_source:
            self.logger.info("************ test_negative_username PASSED ************")
            # driver.quit()
            assert True
        else:
            driver.save_screenshot(filename="Screenshots/test_negative_username.png")
            self.logger.error("************ test_negative_username FAILED ************")
            # driver.quit()
            assert False
