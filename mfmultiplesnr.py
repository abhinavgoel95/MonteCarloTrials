from __future__ import division
import math as m
from scipy import special as sp
import numpy as np
import matplotlib.pyplot as plt
import time

def qfunc(arg): #scipy has no q-function. so use error functions to obtain it
	return 0.5-0.5*sp.erf(arg/1.414)

def dbtowatts(pdb):
	temp = pdb
	temp = temp/10
	return m.pow(10,temp)

def calcvar(E,snr):
	return m.sqrt(E/snr)
	
	
	

pfa_m21 = []
pd_m21 = []
pfa_m22 = []
pd_m22 = []
pfa_m23 = []
pd_m23 = []

SNRdB1 = float(input("enter the SNR in dB: "))
SNRdB2 = float(input("enter the SNR in dB: "))
SNRdB3 = float(input("enter the SNR in dB: "))
snr1 = dbtowatts(SNRdB1)
snr2 = dbtowatts(SNRdB2)
snr3 = dbtowatts(SNRdB3)


th = np.linspace(1,100,1000) #treshold signals
#sigma = float(raw_input("enter the std. dev: "))
s = np.linspace(0,1,10)
energy = 0

for i in range(len(s)): #compute signal energy
	energy = energy+m.pow(s[i],2)

sigma1 = calcvar(energy,snr1)
sigma2 = calcvar(energy,snr2)
sigma3 = calcvar(energy,snr3)
	
for k in range(len(th)):
	gamma = np.log(th[k])
	#gamma1 = (m.pow(sigma,2)*gamma) + energy/2 #gamma' value for theoretical calculation
	cpd_m21= 0
	cpfa_m21 = 0
	cpd_m22= 0
	cpfa_m22 = 0
	cpd_m23= 0
	cpfa_m23 = 0

	for n in range(1,10000):
		#declare a known vector s
		#s = np.linspace(0,1,10)
		w1 = np.random.normal(0,sigma1,10)
		w2 = np.random.normal(0,sigma2,10)
		w3 = np.random.normal(0,sigma3,10)

		xh0_1 = w1
		xh1_1 = np.add(s,w1)
		xh0_2 = w2
		xh1_2 = np.add(s,w2)
		xh0_3 = w3
		xh1_3 = np.add(s,w3)
		

		llrh0_m21 = 0
		llrh1_m21 = 0
		llrh0_m22 = 0
		llrh1_m22 = 0
		llrh0_m23 = 0
		llrh1_m23 = 0
		ts =0

		llrh0_m21= np.inner(xh0_1,s)
		llrh1_m21 = np.inner(xh1_1,s)
		llrh0_m22= np.inner(xh0_2,s)
		llrh1_m22 = np.inner(xh1_2,s)
		llrh0_m23= np.inner(xh0_3,s)
		llrh1_m23 = np.inner(xh1_3,s)

		
		

		if(llrh0_m21 > gamma):
			cpfa_m21 = cpfa_m21+1
		if(llrh1_m21 > gamma):
			cpd_m21 = cpd_m21+1
		if(llrh0_m22 > gamma):
			cpfa_m22 = cpfa_m22+1
		if(llrh1_m22 > gamma):
			cpd_m22 = cpd_m22+1
		if(llrh0_m23 > gamma):
			cpfa_m23 = cpfa_m23+1
		if(llrh1_m23> gamma):
			cpd_m23 = cpd_m23+1

	pfa_m21.append(cpfa_m21/10000)
	pd_m21.append(cpd_m21/10000)
	pfa_m22.append(cpfa_m22/10000)
	pd_m22.append(cpd_m22/10000)
	pfa_m23.append(cpfa_m23/10000)
	pd_m23.append(cpd_m23/10000)
	

	
#plt.plot(pfa,pd)
plt.plot(pfa_m21, pd_m21, 'bs',pfa_m22,pd_m22,'r--',pfa_m23,pd_m23,'g^')
#plt.axis([0,1,0,1])
plt.xlabel('Pfa')
plt.ylabel('Pd')
plt.show()

	


