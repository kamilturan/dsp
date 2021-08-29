import numpy as np
import matplotlib.pyplot as plt
from mktDSP.MkTimeVector import MkTimeVector

def generateSinWave(amplitude:float,
                    frequency:float,
                    phase:float,
                    timeVector):
    return amplitude * np.sin(2*np.pi*frequency*timeVector + phase)

if __name__ == '__main__':
    freq = 10 #Hz
    fs = 100 #Hz
    timeV = MkTimeVector(fs)
