from selenium import webdriver


class WebDriverNotSingleton:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver


# 테스트 코드
if __name__ == "__main__":
    # Singleton 패턴을 적용하지 않고 웹 드라이버 객체 생성
    driver1 = WebDriverNotSingleton().get_driver()
    driver1.get("https://www.naver.com")
    print(driver1.title)

    # 새로운 인스턴스를 생성하므로 driver2는 다른 웹 드라이버 객체를 사용
    driver2 = WebDriverNotSingleton().get_driver()
    driver2.get("https://www.naver.com")
    print(driver2.title)

    # driver1과 driver2는 다른 객체를 가리키므로 서로 독립적인 동작을 수행
    assert driver1 != driver2

    # 웹 드라이버 종료
    driver1.quit()
    driver2.quit()
