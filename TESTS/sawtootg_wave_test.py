import numpy as np
import matplotlib.pyplot as plt
from mktDSP.generators.signals import Square, Triangular, Sawtooth, Sin, Cos


wave = Sawtooth(10,0,200,1.0)
wave.title = f'Trianghular wave {wave.proteries.frequency}Hz'
print(wave)

plt.title(wave.title)
plt.plot(wave.timeDomain.vector, wave.signal, 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.tight_layout()
plt.show()

wave.proteries.frequency = 1

plt.title(wave.title)
plt.plot(wave.timeDomain.vector, wave.signal, 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.tight_layout()
plt.show()
