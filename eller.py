flag = False
for a in range (1, 150):
    for  b in range (a, 151):
        for c in range (b, 151):
            for d in range (c, 151):
                sam = a**5+b**5+c**5+d**5
                e = int(sam**0.2)
                flag = sam == e**5
                if flag:
                    break
            if flag:
                break         
        if flag:
            break   
    if flag:
        break
print (a+b+c+d+e)
