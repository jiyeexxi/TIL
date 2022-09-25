# Xpath

## xpath란 무엇인가?

**xml 파일의 원하는 태그나 속성을 쉽게 찾기 위한 path 문법**이다 

- Xpath는 XML문장을 트리로서 다루기 때문에 요소나 속성의 위치를 지정하는 것이 가능하다
- 그렇다면 **selenium에서의 Xpath는 페이지의 HTML 구조를 탐색하는 데 사용되는 XML 경로**이다
- XML 경로 식을 사용하여 웹 페이지에서 요소를 찾기 위한 구문 또는 언어이다
- **HTML과 XML 문서 모두에서 HTML DOM 구조를 사용하여 웹 페이지에서 요소의 위치를 찾을 수 있다**


모두 같은 말이다. 

## 기본 문법
```python
xpath = //tagname[@attribute='Value']
```

- // : 현재 노드를 선택 (자신이 보고있는 페이지의 최상단을 가리킴)
- tagname : 특정 노드의 태그이름 즉, html에서 사용하는 태그명 ex) input, div, img 등
- @ : html 태그 내의 속성을 선택하겠다고 명시
- attribute: 노드의 속성 이름 즉, html 태그 내의 속성명 ex) class, id 등
- value : 속성의 값

## 노드의 관계
*부모(parent), 자식(child), 형제(sibling), 선조(ancestor), 자손(descendant)* 총 5개의 관계가 존재한다


## Axes
컨텍스트(현재) 노드에 대한 관계를 나타내며 트리에서 해당 노드를 기준으로 노드를 찾는 데 사용된다

|Axes 종류|설명|
|------|---|
|ancestor|현재 노드의 모든 조상들|
|ancestor-or-self|현재 노드 포함 현재 노드의 모든 조상들|
|attribute|현재 노드의 모든 속성들|
|child|현재 노드의 모든 자식들|
|descendant|현재 노드의 모든 자손들|
|descendant-or-self|현재 노드 포함 현재 노드의 모든 자손들|
|following|현재 노드의 닫힘 태그 뒤 document 내의 모든 요소들|
|following-sibling|현재 노드의 뒤 모든 형제들|
|namespace|현재 노드의 모든 네임스페이스 노드|
|parent|현재 노드의 닫힘 태그 뒤 document 내의 모든 요소들|
|preceding|현재 노드의 이전 모든 태그들|
|preceding-sibling|현재 노드의 이전 모든 형제들|
|self|현재 노드|

