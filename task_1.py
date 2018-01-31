import numpy as np
from scipy.io import wavfile
import sys
rate,file_data=wavfile.read(sys.argv[1])
def band_pass(data,freq_data,start,end):
    for i in range(len(freq_data)):
        if ((freq_data[i]>=start) and (freq_data[i]<=end)):
            pass
        else:
            data[i]*=0
    return data
def increase_amp1(data1,data2):
    for i in range(len(data2)):
        if (data1[i]<0 and data2[i]<0) or (data1[i]>0 and data2[i]>0):
            data2[i]*=5
        if (data1[i]<0 and data2[i]>0) or (data1[i]>0 and data2[i]<0):
            data2[i]*=-5
    return data2

N=len(file_data)
t=N/rate
T=1.0/rate

time=np.linspace(0,t,N)
fft_freq=np.fft.fftfreq(N,T)
freq=np.abs(fft_freq)

file_data1=np.fft.fft(file_data)
file_data13=np.abs(file_data1)
filter_data1=band_pass(file_data1,fft_freq,291,293) # human 198 200 or 490 495 or 282 285 khat 1600 1900 or 800 1900
ifft_data1=np.abs(np.fft.ifft(filter_data1))
ifft_data1=increase_amp1(file_data,ifft_data1)
file_data_1=ifft_data1.astype("int16")
wavfile.write("hello22.wav",rate,file_data_1)

import matplotlib.pyplot as plt
plt.plot(freq,np.abs(file_data1))
plt.show()
plt.plot(file_data_1)
plt.show()

