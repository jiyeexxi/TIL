from selenium import webdriver

from automation.design_pattern.page_object_model.login_page import LoginPage


def login(driver):
    login_page = LoginPage(driver)
    login_page.login_btn.click()


if __name__ == "__main__":
    url = "https://www.naver.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    login(driver)
    driver.close()
