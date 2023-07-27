# Design_pattern
### 디자인 패턴리란 무엇인가?
소프트웨어에서 자주 발생하는 문제를 해결하기 위해 고안된 솔루션이다.<br> selenium에서도 테스트 설계하고 구현할 때 사용되는 주요 5가지의 패턴이 존재한다

## Singleton
**하나의 오브젝트만 생성되는 특수한 클래스를 생성하는 디자인 패턴**

- 시스템 전체에서 개체의 단인 인스턴스가 필요할 때 자주 사용된다. 예를 들어, Selenium에서 WebDriver 객체는 일반적으로 singleton 이다. 전체 테스트 실행 동안 웹드라이버 인스턴스가 하나만 있어야 하기 때문이다.
```python
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
```

- driver1과 driver2는 동일한 웹드라이버 인스턴스를 가리킨다

<br>

## Page Object Model(POM)
**웹 애플리케이션의 각 페이지를 별도의 클래스로 추상화하여 페이지와 관련된 작업을 수행하여 유지보수를 편리하게 만드는 방법**

- 웹 애플리케이션의 각 페이지에 대해 별도의 클래스를 만들어야 하며 결국, 테스트 로직과 페이지 요소들을 별도로 분리하여 코드를 작성하게 된다
- 페이지 클래스에는 페이지 객체 및 해당 페이지 객체를 구현하는 메서드를 정의할 수 있다
- 기존 코드를 방해하지 않고 유지 관리하고 필요한 경우 언제든지 변경 가능하다
```python
# 테스트 코드
from selenium import webdriver

from automation.design_pattern.page_object_model.login_page import LoginPage


def click_login_btn(driver):
    login_page = LoginPage(driver)
    login_page.login_btn.click()


if __name__ == "__main__":
    url = "https://www.naver.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    click_login_btn(driver)
    driver.close()
```

```python
# 로그인 페이지 클래스
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def login_btn(self):
        return self.driver.find_element(By.XPATH, '//*[@id="account"]/div/a')
```

<br>

## Fluent Interface(Fluent Page Object Model)
**Fluent API를 통해 웹 페이지 조작을 간단하고 가독성 높이는 방법**

- 메서드 체인을 사용하여 구현되며 가장 읽기 쉬운 코드를 제공하는 API 구현하는 것을 의미한다
- 메서드 체인을 제공하고 코드를 더 읽기 쉽고 사용하기 쉽게 만드는 것
```python
# 일반적인 API 코드
file = open("example.txt", "r")
content = file.read()
file.close()
```
```python
# Fluent API를 사용한 코드
content = open("example.txt", "r").read()
```
-  두 예시는 같은 동작을 수행하지만 Fluent API를 사용한 코드는 한 줄로 표현되어 더욱 간결하다


<br>

## Factory
**객체를 생성하는 별도의 Factory 클래스를 사용하여 객체 생성 로직을 캡슐화하는 디자인 패턴**

- 클라이언트 코드에서 직접 객체를 생성하지 않고 Factory에 의해 객체가 생성되며, 객체 생성 로직이 숨겨지게 됩니다.
```python
from selenium import webdriver

class WebDriverFactory:
    @staticmethod
    def create_driver(browser):
        if browser.lower() == "chrome":
            return webdriver.Chrome()
        elif browser.lower() == "firefox":
            return webdriver.Firefox()
        elif browser.lower() == "edge":
            return webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

# 테스트 코드
if __name__ == "__main__":
    # WebDriverFactory를 사용하여 Chrome 웹 드라이버 생성
    chrome_driver = WebDriverFactory.create_driver("chrome")
    chrome_driver.get("https://www.naver.com")
    print(chrome_driver.title)
    chrome_driver.quit()

    # WebDriverFactory를 사용하여 Firefox 웹 드라이버 생성
    firefox_driver = WebDriverFactory.create_driver("firefox")
    firefox_driver.get("https://www.naver.com")
    print(firefox_driver.title)
    firefox_driver.quit()

```
- WebDriverFactory 클래스는 create_driver 메서드를 갖고 있습니다. 이 메서드는 원하는 브라우저에 해당하는 웹 드라이버 객체를 생성하여 반환합니다. 
- 클라이언트 코드에서는 원하는 브라우저 이름을 인자로 넘겨줌으로써 간단하게 웹 드라이버를 생성할 수 있습니다.

<br>

## Facade
**시스템의 복잡성을 숨기고 최종 사용자에게 간단한 인터페이스를 제공하는 패턴**

- 객체지향 디자인 원칙 중 하나인 "단일 책임 원칙"과 "최소 지식 원칙"을 따르는데, 이를 통해 코드의 유지보수성과 재사용성을 향상시키고 복잡성을 감소시킵니다.
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebPageFacade:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def load_page(self, url):
        self.driver.get(url)

    def search(self, query):
        search_input = self.driver.find_element(By.NAME, "q")
        search_input.clear()
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)

    def get_results_count(self):
        results = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3"))
        )
        return len(results)

    def close(self):
        self.driver.quit()

# 테스트 코드
if __name__ == "__main__":
    web_page = WebPageFacade()
    web_page.load_page("https://www.google.com")
    web_page.search("Facade Design Pattern with Selenium")
    results_count = web_page.get_results_count()

    print(f"검색 결과 수: {results_count}")

    web_page.close()

```
- WebPageFacade 클래스는 Facade 패턴을 적용하여 웹 드라이버를 추상화한 클래스입니다
- load_page, search, get_results_count, close 메서드를 제공하여 간단하게 웹 페이지를 로드하고 검색을 수행하며 검색 결과의 수를 가져옵니다. 
- Facade 패턴을 사용하면 클라이언트 코드에서는 단순하고 간결한 인터페이스만을 다루며, 웹 드라이버의 복잡한 기능을 숨기고 쉽게 사용할 수 있습니다. 이로써 코드의 가독성과 유지보수성을 향상시킬 수 있습니다.

<br>

> 참고 사이트 <br>
> - [Fluent Interface Design Pattern in Automation Testing - Faisal Khatri](https://www.lambdatest.com/blog/fluent-interface-design-pattern/) <br>
> - [Refactoring.guru](https://refactoring.guru/refactoring)
> - [Design Patterns in Selenium - By Pooja Deshpande, Community Contributor - February 20, 2023](https://www.browserstack.com/guide/design-patterns-in-selenium)
