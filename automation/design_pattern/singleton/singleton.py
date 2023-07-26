from selenium import webdriver


class WebDriverSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver


# 테스트 코드
if __name__ == "__main__":
    # Singleton 패턴을 사용하여 웹 드라이버 생성
    driver_singleton = WebDriverSingleton.get_instance()
    driver1 = driver_singleton.get_driver()
    driver1.get("https://www.naver.com")
    print(driver1.title)

    # 같은 인스턴스를 공유하므로 driver2는 동일한 웹 드라이버 객체를 사용
    driver2 = WebDriverSingleton.get_instance().get_driver()
    driver2.get("https://www.naver.com")
    print(driver2.title)

    # driver1과 driver2는 같은 객체를 가리키므로 동일한 웹 페이지의 상태를 유지
    assert driver1 == driver2

    # 웹 드라이버 종료
    driver_singleton.get_driver().quit()
