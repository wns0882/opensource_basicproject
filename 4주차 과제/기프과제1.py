##변수 선언 부분##
def selection_sort(arr): ##선택정렬##
    for i in range(0,len(arr)-1):
        min_idx = i
        for k in range(i+1,len(arr)):
            if arr[k] < arr[min_idx]:
                min_idx = k
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
##2019038010 박준용##
##메인 함수 부분##
if __name__ == "__main__" :
    list_1 = [0xA37B,0x23CC,0x88D9,0xBB8F,0x3A9A]##배열에 16진수 대입
    pre_list = list(map(hex,list_1))##hex함수를 통해 정수를 16진수로 변
    selection_sort(list_1)
    ox_list = list(map(hex,list_1))
print('정렬 전 데이터: ',end = "")
for i in range(0,len(list_1)):
    print(f"{pre_list[i]}",end = " ")
print('\n정렬 후 데이터: ',end = "")
for i in range(0,len(list_1)):
    print(f"{ox_list[i]}",end = " ")
    
