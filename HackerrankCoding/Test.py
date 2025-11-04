n=3
result_list=[]
for i in range(n+1):
    for j in range(i+1):
        for k in range(j+1):
            if(i+j+k!=n):
                result_list.append([i,j,k])


print(result_list)


