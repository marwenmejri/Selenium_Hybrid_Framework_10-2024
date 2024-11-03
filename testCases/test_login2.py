import time
from utilities.customLogger import sample_logger
from pageObjects.LoginPage import LoginPage


class Test002Login:
    baseURL = "https://practicetestautomation.com/practice-test-login/"
    username = "student"
    password = "Password123"
    logger = sample_logger(filename='Logs/logs.log', mode='a', name='custom_logger2')

    def test_login_page_title2(self, setup):
        self.logger.info("************ Test002Login ************")
        self.logger.info("************ test_login_page_title2 STARTED ************")
        driver = setup
        driver.get(url=self.baseURL)
        time.sleep(2)
        expected_title = "Test Login | Practice Test Automation"
        if driver.title == expected_title:
            self.logger.info("************ test_login_page_title2 PASSED ************")
            # driver.quit()
            assert True
        else:
            driver.save_screenshot(filename="Screenshots/test_login_page_title2.png")
            self.logger.error("************ test_login_page_title2 FAILED ************")
            # driver.quit()
            assert False

    def test_login_positive2(self, setup):
        self.logger.info("************ test_login_positive2 STARTED ************")
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
            self.logger.info("************ test_login_positive2 PASSED ************")
            # driver.quit()
            assert True
        else:
            time.sleep(2)
            driver.save_screenshot(filename="Screenshots/test_login_positive2.png")
            self.logger.error("************ test_login_positive2 FAILED ************")
            # driver.quit()
            assert False

    def test_negative_username2(self, setup):
        self.logger.info("************ test_negative_username2 STARTED ************")
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
            self.logger.info("************ test_negative_username2 PASSED ************")
            # driver.quit()
            assert True
        else:
            driver.save_screenshot(filename="Screenshots/test_negative_username.png")
            self.logger.error("************ test_negative_username2 FAILED ************")
            # driver.quit()
            assert False


# class Test003Login:
#     baseURL = "https://practicetestautomation.com/practice-test-login/"
#     username = "student"
#     password = "Password123"
#     logger = sample_logger(filename='Logs/logs.log')
#
#     def test_login_page_title3(self, setup):
#         self.logger.info("************ Test003Login ************")
#         self.logger.info("************ test_login_page_title3 STARTED ************")
#         driver = setup
#         driver.get(url=self.baseURL)
#         time.sleep(2)
#         expected_title = "Test Login | Practice Test Automation"
#         if driver.title == expected_title:
#             self.logger.info("************ test_login_page_title3 PASSED ************")
#             # driver.quit()
#             assert True
#         else:
#             driver.save_screenshot(filename="Screenshots/test_login_page_title3.png")
#             self.logger.error("************ test_login_page_title3 FAILED ************")
#             # driver.quit()
#             assert False
#
#     def test_login_positive3(self, setup):
#         self.logger.info("************ test_login_positive3 STARTED ************")
#         driver = setup
#         driver.get(url=self.baseURL)
#         time.sleep(2)
#
#         lp = LoginPage(driver=driver)
#         lp.set_username(username=self.username)
#         time.sleep(2)
#         lp.set_password(password=self.password)
#         time.sleep(2)
#         lp.login()
#         time.sleep(2)
#
#         new_page_url = driver.current_url
#         expected_string_url = "practicetestautomation.com/logged-in-successfully/"
#         if expected_string_url in new_page_url:
#             lp.logout()
#             time.sleep(2)
#             self.logger.info("************ test_login_positive3 PASSED ************")
#             # driver.quit()
#             assert True
#         else:
#             time.sleep(2)
#             driver.save_screenshot(filename="Screenshots/test_login_positive3.png")
#             self.logger.error("************ test_login_positive3 FAILED ************")
#             # driver.quit()
#             assert False
#
#     def test_negative_username3(self, setup):
#         self.logger.info("************ test_negative_username3 STARTED ************")
#         driver = setup
#         driver.get(url=self.baseURL)
#         time.sleep(2)
#
#         lp = LoginPage(driver=driver)
#         lp.set_username(username="incorrectUser")
#         time.sleep(2)
#         lp.set_password(password=self.password)
#         time.sleep(2)
#         lp.login()
#         time.sleep(2)
#
#         if "Your username is invalid!" in driver.page_source:
#             self.logger.info("************ test_negative_username3 PASSED ************")
#             # driver.quit()
#             assert True
#         else:
#             driver.save_screenshot(filename="Screenshots/test_negative_username3.png")
#             self.logger.error("************ test_negative_username3 FAILED ************")
#             # driver.quit()
#             assert False
