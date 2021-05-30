def EVAL(prim,n):
    signal=[]
    for k in range(len(prim)):
        eval=n/prim[k]-int(n/prim[k])
        if len(prim)==1:
            if eval==0:
                signal.append(0)

        if prim[k]!=1:
            if eval==0:
                signal.append(0)
            else:
                signal.append(1)

    if len(prim)!=1:
        signal.sort()        
        if signal[0]==0:
            check=0
        else:
            check=1
    else:
        check=1
    return check

prim=[1]
for n in range(2,5000,1):
    check=EVAL(prim,n)
    if check==1:
        prim.append(n)
    else:
        next

print(prim)