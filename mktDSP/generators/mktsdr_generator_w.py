class Property:

    def __init__(self, frequency:float,
                 phase:float=0.0,
                 amplitude:float=1.0,
                 title:str=''):
        self.__f = frequency
        self.__p = phase
        self.__a = amplitude
        self.__title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value:str):
        self.__title = value

    @property
    def frequency(self):
        return self.__f

    @frequency.setter
    def frequency(self, value:float):
        self.__f = value

    @property
    def phase(self):
        return self.__p

    @phase.setter
    def phase(self, value:float):
        self.__p = value

    @property
    def amplitude(self):
        return self.__a

    @amplitude.setter
    def amplitude(self, value:float):
        self.__a = value

    def __repr__(self):
        return f'Props: Amplitude:{self.__a}, Frequency:{self.__f}, Phase:{self.__p}'
