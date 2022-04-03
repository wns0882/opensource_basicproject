##메인 함수 부분##
##2019038010 박준용##
Str_input = list(input("문자열을 입력하세요:"))
for i in range(len(Str_input)): 
    comp = Str_input[i].upper() 
    if comp == Str_input[i]:
        Str_input[i] = Str_input[i].lower()
        
    else:
        Str_input[i] = Str_input[i].upper()
        
print(f"대소문자 변환 결과  --> ", end = '')
for i in range(len(Str_input)):       
    print(f'{Str_input[i]}',end = '')
