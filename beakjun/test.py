import re

def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    print('1 : ', new_id)
    # 2단계
    secend = re.compile(r'[^ 0-9a-z_.-]')
    new_id = secend.sub('', new_id)
    print('2 :', new_id)
    # 3단계
    for i in range( len(new_id)-1):
        print(i)
        if new_id[i] =='.' and new_id[i+1] == '.':
            new_id = new_id[:i] + new_id[i+1:]
            print(new_id)
    print('3 :', new_id)
    return new_id

solution("...!@BaT#*..y.abcdefghijklm")
