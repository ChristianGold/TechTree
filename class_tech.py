__author__ = 'Christian'

class Tech:
    createdTechs=0

    def __init__(self,year):
        self.__year=year
        Tech.createdTechs+=1

    def __del__(self):
        Tech.createdTechs-=1

    def __setYear__(self,year):
        if (type(year)==int):
            self.__year=year
            print("year: ")
            print(self.__year)
        else:
            print("nicht setzbar")