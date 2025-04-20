# Two pointers & Sliding window summary

</br>

- 대체적으로 이중 for문을 while문의 lt와 rt의 2개의 포인터를 이용하여 시간복잡도를 줄이는 알고리즘이다.
- O(n^2) -> O(n)

</br>

**퀵 정렬(O(nlogn) ~ O(n^2))**

- Arrays.sort(arr)

</br>

**선택 정렬(O(n^2))**

```java
for (int i = 0; i < n; i++) {
  for (int j = i+1; j < n; j++) {
    if (arr1[i] > arr1[j]) {
        int temp = arr1[j];
        arr1[j] = arr1[i];
        arr1[i] = temp;
    }
  }
}
```

</br>

**Sliding Window**

- 한 번에 하나의 요소만 추가하고 제거하여 이전 합을 재사용
