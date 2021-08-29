import numpy as np
from mktDSP.generators import TimeDomain
from mktDSP.generators import Property


class Sawtooth:

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
        cotU = np.cos(np.pi * self.timeDomain.vector * self.proteries.frequency + self.proteries.phase)
        cotL = np.sin(np.pi * self.timeDomain.vector * self.proteries.frequency + self.proteries.phase)
        st = ((-2.0 * self.proteries.amplitude) / np.pi) * np.arctan(cotU/ cotL)
        return st

    def __repr__(self):
        return f'{self.proteries}\n {self.timeDomain}, Number of waves count in time {self.timeDomain.numberOfWaveCountInTime(self.proteries.frequency)}'




