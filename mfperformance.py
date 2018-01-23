from __future__ import division
import math as m
from scipy import special as sp
import numpy as np
import matplotlib.pyplot as plt
import time

def qfunc(arg): #scipy has no q-function. so use error functions to obtain it
	return 0.5-0.5*sp.erf(arg/1.414)
	
pfa = []
pd =[]
pfa_m2 = []
pd_m2 = []
pfa_m3 = []
pd_m3 = []

th = np.linspace(1,100, 100) #treshold signals
sigma = float(input("enter the std. dev: "))
s = np.linspace(0,1,10) #declare a known vector s
energy = 0

for i in range(len(s)): #compute signal energy
	energy = energy+m.pow(s[i],2)
	
for k in range(len(th)):
	gamma = np.log(th[k])
	gamma1 = (m.pow(sigma,2)*gamma) + energy/2 #gamma' value for theoretical calculation
	cpd = 0
	cpfa = 0
	cpd_m2= 0
	cpfa_m2 = 0

	for n in range(1,10000):
		w = np.random.normal(0,sigma,10)

		xh0 = w
		xh1 = np.add(s,w)


		llrh0 = 0
		llrh1 = 0
		llrh0_m2 = 0
		llrh1_m2 = 0
		ts =0
		arg = 0
		arg1 = 0

		for i in range(len(xh0)):
			llrh0 = llrh0 + (-((m.pow((xh0[i] - s[i]),2) - m.pow(xh0[i],2))/(2*m.pow(sigma,2))))

		

		for i in range(len(xh1)):
			llrh1 = llrh1 + (-((m.pow((xh1[i] - s[i]),2) - m.pow(xh1[i],2))/(2*m.pow(sigma,2))))

		llrh0_m2= np.inner(xh0,s)
		llrh1_m2 = np.inner(xh1,s)

		if(llrh0_m2 > gamma):
			cpfa_m2 = cpfa_m2+1
		if(llrh1_m2 > gamma):
			cpd_m2 = cpd_m2+1

		if(llrh0 > gamma):
			cpfa = cpfa+1

		if(llrh1 > gamma):
			cpd = cpd+1

	#pfa_m3.append(qfunc(gamma1/m.sqrt(m.pow(sigma,2)*energy)))
	#pd_m3.append(qfunc((gamma1-energy)/m.sqrt(m.pow(sigma,2)*energy)))
	pfa.append(cpfa/10000)
	pd.append(cpd/10000)
	#pfa_m2.append(cpfa_m2/1000)
	#pd_m2.append(cpd_m2/1000)
	

	
plt.plot(pfa,pd, 'r^')
#plt.plot(pfa_m2,pd_m2, 'gs')
#plt.plot(pfa_m3,pd_m3, 'b^')

#plt.plot(pfa, pd, 'r--', pfa_m2, pd_m2, 'bs',pfa_m3,pd_m3,'g^')
#plt.axis([0,1,0,1])
plt.xlabel('Pfa')
plt.ylabel('Pd')
plt.show()

	


