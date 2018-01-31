import numpy as np
import sys
from scipy.io import wavfile
rate,file_data=wavfile.read(sys.argv[1])
def band_pass(data,freq_data,start,end):
    for i in range(len(freq_data)):
        if (freq_data[i]>=start and freq_data[i]<=end):
            pass
        else:
            data[i]*=0
    return data
def increase_amp1(data1,data2):
    for i in range(len(data2)):
        if (data1[i]<0 and data2[i]<0) or (data1[i]>0 and data2[i]>0):
            data2[i]*=1
        if (data1[i]<0 and data2[i]>0) or (data1[i]>0 and data2[i]<0):
            data2[i]*=-1
    return data2

def remove_small_amplitude(data1,limit):
    for i in range(len(data1)):
        if data1[i]<limit:
            data1[i]*=0
    return data1
def check_equal_data(data2):
    for i in range(len(data2)):
        if i!=len(data2)-1:
            if data2[i]==data2[i+1]:
                pass
            else:
                data3.append(data2[i])
        else:
            data3.append(0)
    return data3

N=len(file_data)
t=N/rate
T=1.0/rate
time=np.linspace(0,t,N)
fft_freq=np.fft.fftfreq(N,T)
file_data1=np.fft.fft(file_data)
file_data2=np.copy(file_data1)
file_data_sound=band_pass(file_data1,fft_freq,390,398)
file_data_noise=band_pass(file_data2,fft_freq,393,418)
ifft_data1_noise=np.abs(np.fft.ifft(file_data_noise))
ifft_data1_sound=np.abs(np.fft.ifft(file_data_sound))
sound_data=increase_amp1(file_data,ifft_data1_sound)
noise_data=increase_amp1(file_data,ifft_data1_noise)
max_sound_data=np.max(sound_data)
print max_sound_data
file_data_2=remove_small_amplitude(noise_data,max_sound_data)
file_data_2=file_data_2.astype("int16")
wavfile.write("hello6.wav",rate,file_data_2)
data1=[]
for i in range(len(file_data_2)):
    if file_data_2[i]!=0:
        data1.append(file_data_2[i])

data2=remove_small_amplitude(data1,max_sound_data+10)
data3=[]
data3=check_equal_data(data2)
data1=list(filter(lambda x:x==0,data3))
count=len(data1)-1
print "\ntotal count={}".format(count)
'''
import matplotlib.pyplot as plt
plt.plot(time,file_data)
plt.show()
plt.plot(time,noise_data)
plt.show()
'''
