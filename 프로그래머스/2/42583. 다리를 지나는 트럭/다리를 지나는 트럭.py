'''
모든 트럭이 다리 건너는 시간
정해진 순서로 거너야함

트럭 2대가 올라갈수있으니까 2칸으로 봤네 1칸당 1초
-> 그니까 2번째 입출력 예가 101임

다리 지탱 개수 = bridge_length
다리 지탱 무게 = weight

빈 것이 아니라 길이만큼 다리를 만들어주고 시작해야됨

'''
def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    # 다리 위
    on_bridge = deque([0] * bridge_length)
    # 대기트럭
    truck_weights = deque(truck_weights)
    
    time = 0
    total_weights = 0
    
    while on_bridge:
        
        time += 1
        left_truck = on_bridge.popleft()
        total_weights -= left_truck
        
        if truck_weights:
            if truck_weights[0] + total_weights <= weight:
                # 대기트럭에서 뽑고
                truck = truck_weights.popleft()
                # on_bridge에 넣기
                on_bridge.append(truck)
                total_weights += truck
            else:
                on_bridge.append(0)
        
        # print(on_bridge)
    return time
        
        
    