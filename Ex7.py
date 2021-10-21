from numpy import sin, linspace, pi
import matplotlib.pyplot as plt
#import math

n=2000
frequency = 500.0 #en Hz
amplitude = 2.0 #en V
p=1/frequency
t=linspace(0.0,p,100)
uharm = []
ug = [0]



def calc_amplitude(x,y):
    if y%2 == 0:
        ai = 0
        return ai
    else:
        ai = 4*x/(y*pi)
        return ai



for i in range(n):
    ai = calc_amplitude(amplitude, i)
    fi = frequency*i
    uharm.append(ai*sin(2*pi*fi*t))
    ug += uharm[i]
    plt.plot(t,uharm[i])

plt.plot(t, ug)

s="n ="+str(n)+", freq ="+str(frequency)+"Hz, ampl. ="+str(amplitude)+"V"
plt.title("Synthees de Fourier\n"+s)
plt.xlabel("t(s)")
plt.ylabel("u(V)")

plt.show()
