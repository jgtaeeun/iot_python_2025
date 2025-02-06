# 모듈-파이썬 파일 .py

# import 모듈명
# from 모듈명 import 상세

import py02_car
hisCar = py02_car.Car('기아차', '스팅거', '몰라') 
print(hisCar)

import py02_car as c
sisterCar = c.Car('페라리','GT911','290S너2468')
print(sisterCar)

from py02_car import Car
herCar = Car('람보르기니','이름몰라','58로1004')
print(herCar )

