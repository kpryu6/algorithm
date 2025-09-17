'''
트럭이 다리 지남(일차선)
모두 다 건너려면 몇초?
다리 ____ -> 4대까지 올라감 - bridge_length
최대 weight 무게까지

예
__ - 10kg

지난 트럭으로 while 잡았는데 그럼 문제가있음
너무복잡함

시간   지난 트럭     지나고있는트럭(10kg)     대기
0      []          __                 [7,4,5,6]
1      []          _7                 [4,5,6]
2      []          7_                 [4,5,6]
3      [7]         _4                 [5,6]
4      [7]         45                 [6]
5      [7,4]       5_                 [6]    
6      [7,4,5]     _6                 []
7      [7,4,5]     6_                 []
8      [7,4,5,6]   __                 []
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = deque([0]*bridge_length)
    trucks = deque(truck_weights)
    
    print(on_bridge)
    print(trucks)
    
    bridge_weight = 0
    
    while on_bridge:
        
        answer += 1
        # 다리에 있는거 빼
        finish = on_bridge.popleft()
        bridge_weight -= finish
        
        # 다리에 truck 넣어
        if trucks:
            if trucks[0] + bridge_weight <= weight:
                truck = trucks.popleft()
                on_bridge.append(truck)
                bridge_weight += truck
            else:
                # 다리에 있는 트럭 왼쪽으로 밀기
                on_bridge.append(0)
            
    return answer



