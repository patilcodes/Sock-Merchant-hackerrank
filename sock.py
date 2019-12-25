def sockMerchant(n, ar):
    list=[]
    for i in ar:
        if i not in list:
            list.append(i)
    c=0
    for x in list:
        b=ar.count(x)
        c+=b//2
    return c
