def mixcol(arr):
    #arr is a 2D array of 4x4, with each element being a 8 bit number
    pre_mul=[[2,3,1,1],[1 ,2, 3, 1],[1 ,1, 2 ,3],[3, 1, 1, 2]]
    # prime poly =>  x^8 + x^4 + x^3 + x + 1
    op=[]
    for i in range(4):
        op.append([])
        for j in range(4):
            arr_aux=[]
            for k in range(4):
                x=pre_mul[i][k]
                y=arr[k][j]
                if x==1:
                    arr_aux.append(y)
                elif x==2:
                    if y[0]=="0":
                        xgx=y[1:]+"0"
                        arr_aux.append(xgx)
                    else:
                        xgx=y[1:]+"0"
                        s2="00011011"
                        z=(10-len(bin(int(xgx,2)^int(s2,2))))*"0"+bin(int(xgx,2)^int(s2,2))[2:]
                        arr_aux.append(z)
                else:
                    if y[0]=="0":
                        xgx=y[1:]+"0"
                        z=(10-len(bin(int(xgx,2)^int(y,2))))*"0"+bin(int(xgx,2)^int(y,2))[2:]
                        arr_aux.append(z)
                    else:
                        xgx=y[1:]+"0"
                        s1=bin(int(xgx,2)^int(y,2))[2:]
                        s2="00011011"
                        z=(10-len(bin(int(s1,2)^int(s2,2))))*"0"+bin(int(s1,2)^int(s2,2))[2:]
                        arr_aux.append(z)
            accumulator=0
            for p in arr_aux:
                s=int(p,2)
                accumulator^=s
            op[i].append((10-len(bin(accumulator)))*"0"+bin(accumulator)[2:])
    return op

def inv_mixcol(arr):
    return mixcol(mixcol(mixcol(arr)))
