# String summary

**Math.min(a,b)**
- a,b 둘 중 작은 거

</br>

**valueOf**
- String.valueOf(type)
- Integer.valueOf(type)
</br>

**replace(a,b)**
- String s = "#*"
- s.replace('#','1').replace('*','2')
- s = '12'
</br>

**split(String str)**
- String [] strArray = str.split(" ");
- split 함수를 이용해서 str에 있는 문자열을 공백으로 나누어 배열에 저장
  
</br>

**Character.isDigit(x)**
- x가 숫자냐에 대한 boolean return

</br>

**Character.isAlphabetic(x)**
- x가 알파벳이냐에 대한 boolean return

</br>

**Character.toUpperCase(char ch)**
- 문자를 대문자로바꿔줌

</br>

**charAt(int index)**
- 문자열에서 인덱스의 값의 문자를 꺼내옴
</br>

**toCharArray()**
- 문자열을 배열로 만들어줌
</br>

**Integer.parseInt(tmp,2)**
- 문자열(tmp)로 표현된 이진수를 십진수로 넘겨주기
</br>

**IndexOf**
- indexOf는 문자열에서 해당 문자를 검색할 때 첫번째로 발견되는 index를 리턴
- str = "goog" -> str.indexOf('g') -> 0
- 중복 제거에 용이
</br>

**str.substring(int a, int b)**
- str의 인덱스 a부터 b-1까지 할당

**str.substring(int a)**
- str의 인덱스 a부터 끝까지 할당

</br>

**StringBuilder**
- 예를 들어 String 객체 두개를 더하면 새로운 객체가 생성되어 객체가 3개가 된다. 객체의 무한생성을 제한하기 위해 쓰며 출력을 할 경우 toString()을 쓴다.
- String은 불변이지만 StringBuilder는 변경 가능
- String wordReverse = new StringBuilder(x).reverse().toString()
    - 문자열 x를 reverse 해줌
 
</br>

**LinkedHashSet**
```java
// LinkedHashSet을 사용하여 중복을 제거하고 순서를 유지
Set <Character> uniqueChar = new LinkedHashSet<>();

for (char c : str.toCharArray()) {
    uniqueChar.add(c);
}
```
- ksekkset이 kset으로 됨

</br>

**str.equalsIgnoreCase(strReverse)**
- str과 strReverse가 대소문자에 상관없이 같냐에 대해 boolean return

**str.replaceAll("[^A-Z]","")**
- str에서 A부터 Z까지가 아닌 것들은 모두 공백 처리
  
</br>

