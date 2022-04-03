## 2019038010 박준용##
import operator
print('원문')
text = """ 내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다.
내가 그의 이름을 불러주었을 때, 그는 내게로 와 꽃이 되었다.
내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞는 누가 나의 이름을 불러다오.
그에게로 가서 나도 그의 꽃이 되고 싶다.
우리들은 모두 무엇이 되고 싶다.
나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다."""
ary = ['\n','.',' ',',']
dict_list = {}
for i in range(len(text)):
    if text[i] in ary:
        continue

    elif text[i] in dict_list:
        dict_list[text[i]]+= 1 

    else:
        dict_list[text[i]] = 1

tu_list = sorted(dict_list.items(), key = operator.itemgetter(1),reverse = True)

print('--------------------------------')
print('문자\t\t빈도수')
print('--------------------------------')
for i in range(len(tu_list)):
    print(f'{tu_list[i][0]}',end = '')
    print("\t\t", end = '')
    print(f'{tu_list[i][1]}')

