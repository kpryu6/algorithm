# [level 1] 완주하지 못한 선수 - 42576 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42576) 

### 성능 요약

메모리: 36.8 MB, 시간: 62.95 ms

### 구분

코딩테스트 연습 > 해시

### 채점결과

정확성: 58.3<br/>효율성: 41.7<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 04월 02일 22:08:56

### 문제 설명

<p>수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.</p>

<p>마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.</li>
<li>completion의 길이는 participant의 길이보다 1 작습니다.</li>
<li>참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.</li>
<li>참가자 중에는 동명이인이 있을 수 있습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>participant</th>
<th>completion</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>["leo", "kiki", "eden"]</td>
<td>["eden", "kiki"]</td>
<td>"leo"</td>
</tr>
<tr>
<td>["marina", "josipa", "nikola", "vinko", "filipa"]</td>
<td>["josipa", "filipa", "marina", "nikola"]</td>
<td>"vinko"</td>
</tr>
<tr>
<td>["mislav", "stanko", "mislav", "ana"]</td>
<td>["stanko", "ana", "mislav"]</td>
<td>"mislav"</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>예제 #1<br>
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.</p>

<p>예제 #2<br>
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.</p>

<p>예제 #3<br>
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.</p>

<hr>

<p>※ 공지 - 2023년 01월 25일 테스트케이스가 추가되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---
# 문제 풀이

## 완주하지 못한 선수 1
**Sort**
- 정렬(O(nlogn))과 순차적 비교(O(n))를 통해 구현

</br>

## 완주하지 못한 선수 2
**Counter**
- 각 이름의 등장 횟수를 셈 (O(n))
```python3
from collections import Counter

p = Counter(participant)
# Counter({'mislav': 2, 'stanko': 1, 'ana': 1})
c = Counter(completion)
# Counter({'stanko': 1, 'ana': 1, 'mislav': 1})

diff = p - c
# Counter({'mislav': 1})
```
</br>

## 완주하지 못한 선수 3
**Hash**
- 객체(주로 문자열)에 대해 해시 값을 정수로 반환
- 동일 객체 -> 동일 해시 값
- 참여자들의 이름으로 해시 값을 구해 단 한명의 완주하지 못한 선수의 해시 값을 가감을 이용해 구할 수 있음

</br>

## 완주하지 못한 선수 4

**zip**
- 여러 개의 이터러블(iterable) 객체(예: 리스트, 튜플, 문자열 등)를 동시에 순회할 수 있게 해주는 내장 함수
- 각 요소를 순서대로 묶어 **튜플** 형태로 반환
- 두 리스트의 같은 인덱스에 있는 요소들을 한쌍으로 묶음
```python3
fruits = ["apple", "banana", "cherry", "pineapple"]
colors = ["red", "yellow", "dark red"]

zipped = zip(fruits, colors)
print(list(zipped))
# 출력: [('apple', 'red'), ('banana', 'yellow'), ('cherry', 'dark red')]
```
- 가장 짧은 이터러블의 길이에 맞춰 순회 멈춤
- 반환값은 iterator
  - 필요에 따라 리스트나 튜플로 변환시키기

</br>
