def solution(bridge_length, weight, truck_weights):
    answer = 0 # 초
    on_the_bridge = [0] * bridge_length # 다리 만들기
    end_truck = [] # 나온 트럭 리스트
    start_truck_count = len(truck_weights) # 트럭 리스트
    on_truck = 0 # 다리위 트럭수
    
    # 출력 트럭이 출발 트럭과 같을때까지
    while len(end_truck) != start_truck_count: 
        # print(truck_weights)
        # print(on_the_bridge)
        # print(end_truck)
        # print()
        
        # 다리위의 마지막에 트럭이 있으면
        if on_the_bridge[0] > 0:
            # 트럭을 출력 리스트에 -> 다리가 1개 부족
            end_truck.append(on_the_bridge.pop(0)) 
            on_the_bridge.append(0) # 다리를 크기 윈상복구
            on_truck -= 1 # 다리위 트럭수 -1 
        # 다리위 전부다 1칸씩 이동
        else:
            on_the_bridge.pop(0)
            on_the_bridge.append(0)
            
        # 다리위에 트럭들 + 출발 트럭무게 <= 다리 무게제한
        # 다리길이보다 트럭 대수가 작으면 
        if (sum(on_the_bridge) + truck_weights[0]) <= weight and on_truck < bridge_length:
                on_the_bridge[-1] = truck_weights.pop(0) # 출발 트럭을 다리 맨 처음에 넣는다.
                truck_weights.append(0) # 출발 트럭 끝이 빈값을 넣는다. (lndex 초과를 막기위해)
                on_truck += 1 # 다리위 트럭수 + 1 

        answer += 1 # 1초 경과
        
    return answer
