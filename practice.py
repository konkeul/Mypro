'''
* 윤년 계산하기
1. 4의 배수.
2. 100의 배수가 아닐것. ( 1의 조건을 만족하면서 )
3. 400의 배수는 무조건 윤년

* 입력은 이렇게 받으시면 됩니다.
year = int(input("년도를 입력하세요 : "))
'''
year = int(input("년도를 입력하세요 : "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print("윤년")
else: print("비윤년")
    

