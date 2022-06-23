print('입력값 타입 체크')
u = input('입력하시오 :')
print('입력값이 숫자일가 문자일까')
print(type(u))
if u=='1': #문자를 비교
# if int(u)==1:
    print("같다.")
else:
    print("다르다.")