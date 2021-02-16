# -*- coding: utf-8 -*-

import math

class Ackley:

	def sumax(self,ni,nf,s):
		f=0.0
		for n in range(ni-1,nf):
			x=s[n]
			f=(x**2.0)+f
		return f
	def sumacos(self,ni,nf,s):
		f=0.0
		for n in range(ni-1,nf):
			x=s[n]
			f=math.cos(2*math.pi*x)+f
		return f

	def func(self,s):
		d=len(s)
		f1=self.sumax(1,d,s)
		f1=20.0*(math.e**(-0.2*math.sqrt((1.0/d)*f1)))
		
		f2=self.sumacos(1,d,s)
		f2=math.e**((1.0/d)*f2)
		
		f=-f1-f2+20+math.e

		return f

