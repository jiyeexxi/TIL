from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def login_btn(self):
        return self.driver.find_element(By.XPATH, '//*[@id="account"]/div/a')
