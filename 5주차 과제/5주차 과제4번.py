##2019038010 박준용##
import re
ary = ['A37B','23CC','88D9','BB8F','3A9A']
int_ary = []
print("정렬 전 데이터 -->", end=' ')
for i in range(len(ary)):
    print(ary[i],end=' ')
for i in range(len(ary)):
    str_ary = ''
    for j in range(len(ary[i])): #a37b
        if ary[i][j].isdigit():  
            str_ary += ary[i][j]
        else: continue
    int_ary.append(int(str_ary))

for i in range(len(int_ary)-1):
    least = i
    for j in range(i+1,len(int_ary)):
        if int_ary[j]<int_ary[least]:
            least = j
    int_ary[i],int_ary[least],ary[i],ary[least], = int_ary[least],int_ary[i],ary[least],ary[i]

print("\n정렬 후 데이터 -->", end = ' ')
for i in range(len(ary)):
    print(ary[i], end=' ')
