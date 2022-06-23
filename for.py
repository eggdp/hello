import random
for i in range(5):
    print(f'{i+1}hello world')
    a1=input('짬뽕 , 짜장 둘중 하나 입력하세요 :')
    print('니가 입력한 값 : ',a1)
    abc='짜장','짬뽕'
    if a1=='짜장' or a1=='짬뽕':
        print('나오나?') 
        m=random.choice(abc)
        print('인공지능이 추천해주는 결과는?', f"{m} 먹어!")
    else:
        print("짬짜면 먹어!!")
