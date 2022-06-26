x = int(input())
a =[]
for i in range(1, x+1):
    if i < 100:
        a.append(i)
    else:
        if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
            a.append(i)
print(len(a))

        

            
    
