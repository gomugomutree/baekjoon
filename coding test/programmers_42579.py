def solution(genres, plays):
    answer = []
    play_list ={}
    genre_pri = []
    
    # dictionary 
    for key, play in zip(genres, enumerate(plays)):
        # print(key, play)
        
        if key in play_list:
            play_list[key].append(list(play))
        else:
            play_list[key] = [list(play)]

    # {'classic': [[0, 500], [2, 150], [3, 800]], 
    #  'pop': [[1, 600], [4, 2500]]}
    
    # 재생 횟수별 정렬
    for key in play_list:
        play_list[key].sort(key=lambda x: x[1], reverse=True)
    
    #{'classic': [[3, 800], [0, 500], [2, 150]], 
    # 'pop': [[4, 2500], [1, 600]]}
    # print(play_list)
    
    # 장르별 우선순위
    for key in play_list:
        temp = 0
        for i in range(len(play_list[key])):
            temp += play_list[key][i][1]
        genre_pri.append([temp, key])
        
    # 	[[1450, 'classic'], [3100, 'pop']]
    genre_pri.sort(reverse=True)
    # print(genre_pri)
    
    # 장르별 1,2순위 
    for genre in genre_pri:
        # print(play_list[genre[1]][0][0])
        # print(play_list[genre[1]][1][0])
        
        # 장르별 2곡 이상
        if len(play_list[genre[1]]) >1:
            answer.append(play_list[genre[1]][0][0])
            answer.append(play_list[genre[1]][1][0])
        # 장르 1곡
        else: 
            answer.append(play_list[genre[1]][0][0])
    
    return answer