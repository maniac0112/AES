def shift_rows(Mat):
    shift_amt=0
    new_mat=[[0 for j in range(len(Mat[0]))]for k in range(len(Mat))]
    for r in range(len(Mat)):
        for t in range(len(Mat[0])):
            new_mat[r][t]=Mat[r][(t+shift_amt)%4]
        shift_amt+=1
    return new_mat
   


def inv_shift_rows(Mat):
    shift_amt=0
    new_mat=[[0 for j in range(len(Mat[0]))]for k in range(len(Mat))]
    for r in range(len(Mat)):
        for t in range(len(Mat[0])):
            new_mat[r][t]=Mat[r][(4+t-shift_amt)%4]
        shift_amt+=1
    return new_mat