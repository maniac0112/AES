import sub_bytes
import shift_rows
import mix_col
import key_expansion
import round_key

def aes(m,key):
    #m is a 128 bit binary message to encrypt!
    key_array=round_key.matrix(key)
    key_schedule=key_expansion.key_expansion(key_array)
    key1=key_schedule[0]+key_schedule[1]+key_schedule[2]+key_schedule[3]
    ip_block=""
    for i in range(len(key1)):
        ip_block+=str(int(key1[i])^int(m[i]))
    ip_array=round_key.matrix(ip_block)
    
    for round in range(1,11):
        #step 1 = > subbytes!
        ip_array=sub_bytes.sub_byte(ip_array)
        #step 2 = > shiftrows!
        ip_array= shift_rows.shift_rows(ip_array)
        #step 3 => mixcols
        if round!=10:
            ip_array= mix_col.mixcol(ip_array)
        ip_array=round_key.round_key(ip_array,key_schedule[4*round:4*round+4])
    #convert to ciphertext!
    s=""
    for i in range(4):
        for j in range(4):
            s+=ip_array[j][i]
    return s

def aes_decrypt(m,key):
    #m is the ciphertext!
    #key is 128 bit symmetric
    key_array=round_key.matrix(key)
    key_schedule=key_expansion.key_expansion(key_array)
    key_schedule.reverse()
    key1=key_schedule[3]+key_schedule[2]+key_schedule[1]+key_schedule[0]
    ip_block=""
    for i in range(len(key1)):
        ip_block+=str(int(key1[i])^int(m[i]))
    ip_array=round_key.matrix(ip_block)
    
    for round in range(1,11):
        #step 1 = > Inv shiftrows!
        ip_array= shift_rows.inv_shift_rows(ip_array)
        #step 2 = > Inv subbytes!
        ip_array=sub_bytes.inv_sub_byte(ip_array)
        #round key addition
        temp=key_schedule[4*round:4*round+4]
        temp.reverse()
        ip_array=round_key.round_key(ip_array,temp)
        #step 3 =>inv mixcols
        if round!=10:
            ip_array= mix_col.inv_mixcol(ip_array)
    #convert to ciphertext!
    s=""
    for i in range(4):
        for j in range(4):
            s+=ip_array[j][i]
    return s
