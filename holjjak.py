import random
#AI가 홀인지 짝인지 문제내면 맞추기.
#내가 입력한 값과 컴퓨터가 문제를 낸 값과
#비교를 해서 맞으면 맞다. 틀리면 틀렸다. 5번 게임을 반복한다.
holjjak = '홀','짝'
# print(f'컴이 낸 문제:{com}')
n= input('몇번 게임을 할거냐:')
for i in range(int(n)): #문자 5 가들어오니 int 로 변환해줘야한다.
    print(f'{i+1}/{n} 게임')
    com=random.choice(holjjak)
    user=input('홀 인지 짝인지 입력 : ')
    print('내가 입력한 값 : ',user)
    print('컴퓨터 :',com)
    if com==user:
        print('맞습니다.:\n')
    else:
        print('틀렸습니다.\n')