import numpy as np
from mktDSP.generators import TimeDomain
from mktDSP.generators import Property


class Square:

    def __init__(self, frequency:float,
                 phase:float,
                 sampleRate:float,
                 amplitude:float=1.0,
                 title:str=''):
        self.__property = Property(frequency, phase, amplitude, title)
        self.__td = TimeDomain(sampleRate)
        self.__signal = 0

    @property
    def proteries(self):
        return self.__property

    @proteries.setter
    def proteries(self, value):
        self.__property = value

    @property
    def timeDomain(self):
        return self.__td

    @timeDomain.setter
    def timeDomain(self, value):
        self.__td = value

    @property
    def signal(self):
        signal= np.sign(np.sin(2.0 * np.pi * self.proteries.frequency * self.timeDomain.vector + self.proteries.phase))
        return signal

    def __repr__(self):
        return f'{self.proteries}\n {self.timeDomain}, Number of waves count in time {self.timeDomain.numberOfWaveCountInTime(self.proteries.frequency)}'


