import sub_bytes

def key_expansion(key):
	w0="".join([key[i][0] for i in range(4)])
	w1="".join([key[i][1] for i in range(4)])
	w2="".join([key[i][2] for i in range(4)])
	w3="".join([key[i][3] for i in range(4)])
	arr=[w0,w1,w2,w3]
	RCs=[]
	for i in range(1,11):
		if i==1:
			RCs.append("00000001")
		else:
			#multiply with x!
			if RCs[-1][0]=="0":
				xgx=RCs[-1][1:]+"0"
				RCs.append(xgx)
			else:
				xgx=RCs[-1][1:]+"0"
				s2="00011011"
				z=(10-len(bin(int(xgx,2)^int(s2,2))))*"0"+bin(int(xgx,2)^int(s2,2))[2:]
				RCs.append(z)

		round_constant_i=RCs[-1]
		left_shifted_w=arr[(i-1)*4+3][8:]+arr[(i-1)*4+3][:8]
		b1=sub_bytes.sub(left_shifted_w[:8])
		b2=sub_bytes.sub(left_shifted_w[8:16])
		b3=sub_bytes.sub(left_shifted_w[16:24])
		b4=sub_bytes.sub(left_shifted_w[24:])
		w_aux=(10-len(bin(int(b1,2)^int(round_constant_i,2))))*"0"+bin(int(b1,2)^int(round_constant_i,2))[2:]+b2+b3+b4
		wi0=(34-len(bin(int(w_aux,2)^int(arr[(i-1)*4],2))))*"0"+bin(int(w_aux,2)^int(arr[(i-1)*4],2))[2:]
		wi1=(34-len(bin(int(wi0,2)^int(arr[(i-1)*4+1],2))))*"0"+bin(int(wi0,2)^int(arr[(i-1)*4+1],2))[2:]
		wi2=(34-len(bin(int(wi1,2)^int(arr[(i-1)*4+2],2))))*"0"+bin(int(wi1,2)^int(arr[(i-1)*4+2],2))[2:]
		wi3=(34-len(bin(int(wi2,2)^int(arr[(i-1)*4+3],2))))*"0"+bin(int(wi2,2)^int(arr[(i-1)*4+3],2))[2:]
		arr.append(wi0)
		arr.append(wi1)
		arr.append(wi2)
		arr.append(wi3)
	return arr
