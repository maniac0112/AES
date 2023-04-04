def matrix(ip_block):
    #convert a 128 bit block to matrix!

    ip_array=[[ip_block[0:8],ip_block[32:40],ip_block[64:72],ip_block[96:104]],
    [ip_block[8:16],ip_block[40:48],ip_block[72:80],ip_block[104:112]],
    [ip_block[16:24],ip_block[48:56],ip_block[80:88],ip_block[112:120]],
    [ip_block[24:32],ip_block[56:64],ip_block[88:96],ip_block[120:128]]]
    return ip_array


def make_key(arr): 
    #linear array of 4 values (1 word each)!
    s=arr[0]+arr[1]+arr[2]+arr[3]
    return matrix(s)


def round_key(ip_arr, keys):
    key_arr=make_key(keys)
    arr2=[[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            x=(10-len(bin(int(key_arr[i][j],2)^int(ip_arr[i][j],2))))*"0"+bin(int(key_arr[i][j],2)^int(ip_arr[i][j],2))[2:]
            arr2[i][j]=x
    return arr2

