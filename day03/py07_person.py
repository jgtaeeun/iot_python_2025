class Person:
    #명사(속성)인 멤버변수
    name = '유토'
    age = 27
    weight = 65.5
    gender = 'male'

    #초기화 메서드(파이썬 기본으로 포함)
    def __init__(self, name, age, weight, gender):
        self.name = name
        self.age =age
        self.weight = weight
        self.gender =gender

    #동사(기상)인 멤버함수 (메서드) 
    def getup(self):    #myself
        print(f'{self.name}이(가) 일어납니다.')

    def setWeight(self, weight):
        print(f'{self.name}의 몸무게가 변경됩니다.')
        print(f'현재 몸무게 {self.weight} kg')
        self.weight = weight
        print(f'변경 후 몸무게 {self.weight} kg')

    def getGender(self):
        return self.gender
    
    def __str__(self):
        retStr = f'{self.name}\n{self.weight}\n{self.gender}\n{self.age}'
        return retStr

man = Person('유진' , 23 , 48.5, 'woman')   #__init__ 특수함수 실행
man.getup()
man.setWeight(49.1)
print(f'{man.name}의 성별은 {man.getGender()}')
print('-------------')
print('객체정보')
print(man)