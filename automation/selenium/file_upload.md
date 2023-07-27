## 파일경로 종류

- 상대경로
    - 현재 작업 중인 파일을 기준으로 경로를 탐색
        - ./ : 현재 위치
        - ../ : 상위 폴더
- 절대경로
    - 현재 작업 중인 경로와 상관없이 바뀌지 않는 절대적인 경로

## 파일 업로드 방법

### send_keys()

send_keys() 의 문서 설명의 일부분이 다음과 같다.

```python
This can also be used to set file inputs.

::
    file_input = driver.find_element(By.NAME, 'profilePic')
    file_input.send_keys("path/to/profilepic.gif")
    # Generally it's better to wrap the file path in one of the methods
    # in os.path to return the actual path to support cross OS testing.
    # file_input.send_keys(os.path.abspath("path/to/profilepic.gif"))

```

- file_input = driver.find_element(By.NAME, 'profilePic') ⇒ 먼저 파일 업로드하는 element를 찾는다
- file_input.send_keys("path/to/profilepic.gif") ⇒ element에 send_keys(업로드할 파일 경로) 입력
- os에 따라 실제 경로를 반환해 주는 os.path.abspath 메소드 사용하여 절대 경로 전달