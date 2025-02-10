# Movie.py - Movie라는 이름의 모듈

class Movie :
    def __init__(self, title,release, sponsor , rate):
        self.__title = title
        self.__release = release
        self.__sponsor = sponsor
        self.__rate = rate
    
    def __str__(self):
        result = ( f'제목 : {self.__title} ({self.__release})\n'
                   f'배급사 : {self.__sponsor} \n'
                   f'평점 : {self.__rate}'
                ) 
        return result
    
    # getter함수
    def getTitle(self):
        return self.__title
    
    def getRelease(self):
        return self.__release
    
    def getSponsor(self):
        return self.__sponsor
    
    def getRate(self):
        return self.__rate
    
    # 영화검색할 때, 검색어가 포함된 것
    def isNameContain (self, search_name):
        if search_name in self.__title :   # search_name = '히트맨' , title='히트맨2'
            return True
        elif search_name.upper() in self.__title :
            return True
        elif search_name.lower() in self.__title :
              return True
        else :
            return False
    
    # 영화삭제할 때, 검색어와 일치한 것
    def isNameSame(self, delete_name):
        if delete_name == self.__title :
            return True
        else :
            return False
        