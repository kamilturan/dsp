import numpy as np


class TimeDomain:

    def __init__(self, sampleRate: float,
                 tmin:float=0.0,
                 tmax:float=1.0):
        self.__sr = sampleRate
        self.__tmin = tmin
        self.__tmax = tmax
        self.__calc()

    def __calc(self):
        stepSize = (self.__tmax - self.__tmin) / self.__sr
        self.__time = np.arange(self.__tmin, self.__tmax, stepSize)

    @property
    def sampleRate(self):
        return self.__sr

    @sampleRate.setter
    def sampleRate(self, value):
        self.__sr = value

    @property
    def tmin(self):
        return self.__tmin

    @tmin.setter
    def tmin(self, value):
        self.__tmin = value

    @property
    def tmax(self):
        return self.__tmax

    @tmax.setter
    def tmax(self, value):
        self.__tmax = value

    @property
    def vector(self):
        self.__calc()
        return self.__time

    def reConstractTime(self, f , numberOfWaveCount):
        self.__tmin = 0
        self.__tmax = numberOfWaveCount / f

    def numberOfWaveCountInTime(self, f):
        return f * (self.tmax - self.tmin)

    def __len__(self):
        return len(self.__time)

    def __repr__(self):
        return f'Time: [{self.__tmin}s, {self.__tmax}]'

