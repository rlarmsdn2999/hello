from secrets import choice
import time
import random
menulist = ['짜장면', '짬뽕', '탕수육','피자' ,'치킨','라면','삼겹살','소고기','김밥','유부초밥','된장찌개','김치찌개']
print('메뉴 골라줘!')
print('AI가 추천해주는 메뉴는?')
for i in range(5, 0 ,-1):
    print(f'{i}..')
    time.sleep(1)
#print('5..')
#time.sleep(1)
#print('4..')
#time.sleep(1)
#print('3..')
#time.sleep(1)
#print('2..')
#time.sleep(1)
#print('1..')
#time.sleep(1)
print('엄청난 분석을 통해 오늘의 메뉴를 추천드립니다.')
menu = random.choice(menulist)
print(f'{menu} 입니다.')