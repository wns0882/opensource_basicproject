##2019038010 박준용##
def base2(Num):
    b = Num%2
    list_2.insert(0,b)
    if Num < 2:
        return
    base2(Num//2)
    
def base8(Num):
    b = Num%8
    list_8.insert(0,b)
    if Num < 8:
        return
    base8(Num//8)

def base16(Num):
    b = Num%16
    list_16.insert(0,hex(b))
    if Num < 8:
        return
    base16(Num//16)        

##메인 함수 부분##
list_2 = []
list_8 = []
list_16 = []


a = int(input("10진수 입력 -->"))
base2(a)
base8(a)
base16(a)

print('2진수 :',end = '')
for i in range (len(list_2)):
    print(list_2[i],end = '')
print('\n8진수 :',end = '')

for i in range (len(list_8)):
    print(list_8[i],end = '')
print('\n16진수 :',end = '')

for i in range (len(list_16)): 
    print(list_16[i][2:],end = '')



    
