# algorithm-study

## HashMap 

</br>

**map.put(key,value)**
- map에 key, value 넣기

</br>

**map.put(key, map.getOrDefault(key,0))**
- map에 해당 key가 있으면 그 key의 value 넣고, 해당 key가 없으면 value를 0을 넣는다.

</br>

**map.containsKey('A')**
- A라는 key가 존재하는가?
- return boolean

**map.containsValue(map.get('A'))**
- A라는 key의 value가 존재하는가?
- return boolean

</br>

**map.size()**
- map의 key 수

</br>

**map.remove('A')**
- map의 A라는 key 삭제
- return map.get('A')

</br>

**map.keySet()**
- key set 반환

</br>

**map.entrySet()**
- key와 value를 모두 포함하는 Entry 객체의 set을 반환

</br>

---


## TreeSet

</br>

**TreeSet<Integer> Tset = new TreeSet<>(Collections.reverseOrder())**
- Collections.reverseOreder()
  - TreeSet을 내림차순으로 정렬
  - 안쓰면 오름차순으로 정렬

 </br>
 
**Tset.remove()**
- 특정값 제거

</br>

**Tset.size()**
- Tset의 크기

</br>

**Tset.first()**
- 첫번째 원소 출력

**Tset.last()**
- 마지막 원소 출력

</br>

**Set은 중복제거에 쓰이고, Tree는 정렬에 쓰인다.**


