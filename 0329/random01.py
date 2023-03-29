import random

com = random.randrange(1,21)
while True : #com과 user가 같으면 반복 종료
    user = int(input('1~20 사이의 수 입력: '))
    if com == user :
        print('맞췄습니다')
        break;
    else com > user :
    print('')