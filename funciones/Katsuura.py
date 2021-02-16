# -*- coding: utf-8 -*-
import math

class Katsuura:

	def suma(self,ni,nf,x):
		f=0.0
		for n in range(ni,nf+1):
			f1=(2.0**n)*x
			f=(math.fabs(f1-round(f1))/(2.0**n))+f
		return f
	
	def mult(self,ni,nf,s):
		f=1.0
		for n in range(ni-1,nf):
			x=s[n]
			f1=self.suma(1,32,x)
			f=((1.0+((n+1)*f1))**(10.0/(len(s)**1.2)))*f
		return f

	def func(self,s):
		f1=10.0/(len(s)**2.0)
		f=self.mult(1,len(s),s)
		return f1*f-f1

