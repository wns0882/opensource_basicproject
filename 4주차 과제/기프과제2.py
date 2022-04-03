##2019038010 박준용##
import operator
train_list = [('토마스', 5), ('헨리', 8),('에드워드', 9),
('에밀리', 5), ('토마스', 4), ('헨리', 7),('토마스', 3),
('에밀리', 8), ('퍼시', 5), ('고든', 13)]

dict_list = {}
for i in range(len(train_list)):
    if train_list[i][0] in dict_list: 
        value = train_list[i][1] + dict_list[train_list[i][0]]
        dict_list[train_list[i][0]] = value
        
    else:
        dict_list[train_list[i][0]] = train_list[i][1]

tu_list = sorted(dict_list.items(), key = operator.itemgetter(1), reverse=True)
        
print('---------------------------')
print('기차        총수송량  순위')
print('---------------------------')
for i in range(len(tu_list)):
    print(f'{tu_list[i][0]}    \t{tu_list[i][1]}', end = '')
    if tu_list[i][1] == tu_list[i-1][1]:        
        print(f"\t{i}")
    else:
        print(f"\t{i+1}")
           
    
    
     






    

