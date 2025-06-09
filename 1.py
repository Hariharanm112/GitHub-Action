def name(m):

    reslt=[]

    for i in m:
        if i in reslt:
            break
        reslt.append(i)

    return reslt
print(name("abcaefg"))