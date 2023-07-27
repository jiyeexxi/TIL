# selenium 대기 종류

- 물리적 대기
- 암시적 대기 (implicitly wait)
- 명시적 대기 (explicitly wait)

## time.sleep()

- 초단위로 무조건 기다린다

```python
from time import sleep

# 5초간 기다림
sleep(5)
```

## implicitly_wait()

- 웹페이지 전체가 넘어올 때까지 기다린다
- 무조건 작성한 시간까지 대기하는 것(time.sleep이 해당)이 아닌 웹페이지가 1초만에 넘어왔으면 1초만 기다리고 다음 코드를 실행하기 된다

```python
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(10) # chrome 웹페이지 전체가 넘어올때까지 10초 기다리고 넘어오지 않으면 다음 코드를 실행
```

## WebDriverWait()

- implicitly_wait 는 불완전하다. 사이트에 접속하였을 때 전체 페이지가 한번에 다 나오는 경우도 있지만 일부분이 먼저 나오거나 늦게 나오는 경우가 존재한다
- 예를들어, 전체 페이지에 대한 코드는 다 넘어왔지만 실제적으로 사용자가 보이는 화면에 렌더링하여 보여주는데에는 시간이 걸릴 수 있어 일부분이 보이지 않을 수 있다. 이때 implicitly_wait를 사용하게 되면 전체페이지에 대해서는 넘겨줬다고 인식하여 다음 코드를 실행하게 된다. 다음 코드를 실행하였더니 렌더링되고 있던 요소에 대한 부분이라면 실패할 수도 있는 것이다.
- 이때, 사용할 수 있는 것이 explicitly wait 이다. **내가 필요한 요소가 보여질 때까지 기다려라** 라는 의미의 대기이다

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://pythondocs.net")

# EC.presence_of_element_located((By.ID, "idname")) 해당 요소가 나타날 때까지 최대 10초를 기다림
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "idname")))
```

### 참고
[셀레니움 wait 개념 이해하기 (implicitly wait VS explicitly wait)](https://pythondocs.net/selenium/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-wait-%EA%B0%9C%EB%85%90-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-implicitly-wait-vs-explicitly-wait/)