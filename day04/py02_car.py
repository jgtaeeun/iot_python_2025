# 객체지향

# 자료구조 list도 클래스로 정의되어 있다. 
# list의 멤버함수에는 우리가 써본 pop, index, append, __len__ 등이 정의되어 있다.
# 클래스 멤버함수로 이미 만들어져 제공해주는 특수함수들은 __함수명__ 형태이다.

# 모듈하려면 클래스 남겨두고 나머지 주석처리
class Car:
 
    def __init__(self, company=None, name=None, plateNumber=None):
        self.__company=company  #멤버변수 이름 앞에 __ 쓰면 외부접근 불가
        self.__name=name
        self.__plateNumber =plateNumber
        print('Car 클래스를 새로 생성!')
   
   


    # 클래스 자체가 출력되는데 , __str__문자열로 출력되도록 바꿔줌
    def __str__(self):
        return f'제 차는 {self.__company} {self.__name}이고 차번호는 {self.__plateNumber}입니다.'

    def setPlateNumber(self, plateNumber):
        if type(plateNumber) is str:
            self.__plateNumber = plateNumber

    def setName(self, newName='글쎄요'):
        self.__name = newName

    def getName(self):
        return self.__name
# myCar = Car('현대', '아이오닉', '54라9537')
# # #myCar = Car(name='아이오닉', plateNumber='54라9537', company='현대')

# print(myCar)

# myCar.__plateNumber = 2018    #클래스 외부에서 잘못된 데이터를 넣어도 문제가 발생x
# print(myCar)


# myCar.setPlateNumber('54마9538')
# print(myCar)
# print(type('54마9538') is str)

# myCar.setPlateNumber(2018)
# print(myCar)
# print(type(2018) is str)

# yourCar = Car()

# print(yourCar)
# yourCar.setPlateNumber('285구8899')
# yourCar.setName('모닝')
# print(yourCar)

# yourCar.setName()
# print(yourCar)