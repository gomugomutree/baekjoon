def solution(brown, yellow):

    for h in range(3, brown//2):
        w = (brown//2 + 2) - h
        if w >= h and ((w-2) * (h-2)) == yellow:
            return [w, h]
