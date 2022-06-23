import random
# print('hello')
# print('한글도 되나?')

#만약에 짜장과 짬뽕 둘중에 하나 추천
#내가 짜장이나 짬뽕을적으면 짜장이나 짬뽕 추천
a1=input('짬뽕 , 짜장 둘중 하나 입력하세요 :')
print('니가 입력한 값 : ',a1)


if a1=='짜장' or a1=='짬뽕':
    print('나오나?') # 참일때만 나옴
    #여기에서 짜장과 짬뽕중에 
    abc='짜장','짬뽕'
    m=random.choice(abc)
    print('인공지능이 추천해주는 결과는?', f"{m} 먹어!")
else:
    print("짬짜면 먹어!!")
# 아니면둘다
