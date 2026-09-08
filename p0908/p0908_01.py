# 클래스 : 변수, 함수를 담을 수 있고, 하나로 묶는 것, 데이터를 보호할 수 있음 - 학생성적 : 합, 평균, 등수 등 계산 - 1천줄 이상 넘어갈 때, 유용
# 만드는 방법 : class + 클래스명(앞글자 대문자 써야 함)

# # 클래스 : 변수와 함수를 포함해서 구현 가능
# class Car:
#     color = ""
#     speed = 0

#     def upSpeed(self):
#         self.speed += 10 # 바깥의 변수를 지정하려면, self를 반드시 넣어야 함

#     def downSpeed(self):
#         self.speed -= 10

# # 클래스를 1개 생성
# c = Car() # 객체(인스턴스) 생성
# c.upSpeed()
# c2 = Car()
# c2.upSpeed() # Car클래스에서 upSpeed함수 사용
# c.color = "white"
# print("색상:",c.color)
# print("속도:",c.speed)
# print("속도2:",c.speed)


# --------------------------------------------------------------------------------

class Car:
    color = ""
    speed = 0
    tire = 0
    door = 0

# 생성자 또는 생성함수 : Car가 생성될 때(class Car), 실행되는 함수
    def __init__(self,color,speed,tire,door): 
        self.color = color
        self.speed = speed
        self.tire = tire
        self.door = door


    def upSpeed(self):
        self.speed += 10 # 바깥의 변수를 지정하려면, self를 반드시 넣어야 함

    def downSpeed(self):
        self.speed -= 10

# 클래스를 1개 생성
c = Car() # 객체(인스턴스) 생성 / 4개변수, 2개 함수 만들어짐
c.color = "white" # 위의 color변수로 적용됨
c.speed = 100
c.tire = 5
c.door = 3
c.upSpeed()
c2 = Car() # 객체(인스턴스) 생성 / 4개변수, 2개 함수 만들어짐
c2.color = "skyblue"
c2.speed = 200
c2.tire = 4
c.door = 5
c2.upSpeed() #  -> c, c3와 상관없음
c3 = Car() # 객체(인스턴스) 생성 / 4개변수, 2개 함수 만들어짐
c3.color = "green"
c3.speed = 120
c3.tire = 5
c3.door = 5
c3.upSpeed()

# 각각 개체별로 변수값을 넣기 번거로움 -> 매개변수를 이용하면 작업이 단축

c = Car() # 객체(인스턴스) 생성 / 4개변수, 2개 함수 만들어짐
c.color = "white" # 위의 color변수로 적용됨
c.speed = 100
c.tire = 5
c.door = 3
c.upSpeed()
# 클래스 객체선언: __init__가 있으면 아래와 같이 선언과 같이 한꺼번에 입력가능
c2 = Car("skyblue",200,4,5) # 객체(인스턴스) 생성 / 4개변수, 2개 함수 만들어짐
c2.upSpeed() #  -> c, c3와 상관없음
c3 = Car("gray",50,5,5) # 객체(인스턴스) 생성 / 4개변수, 2개 함수 만들어짐
c3.upSpeed()