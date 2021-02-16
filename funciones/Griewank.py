# -*- coding: utf-8 -*-
import math

class Griewank:

	def suma(self,ni,nf,s):
		f=0.0
		for n in range(ni-1,nf):
			x=s[n]
			f=(x**2.0)+f	
		return f
	
	def mult(self,ni,nf,s):
		f=1.0
		for n in range(ni-1,nf):
			x=s[n]
			f=(math.cos(x/math.sqrt(n+1)))*f	
		return f

	def func(self,s):
		f1=self.suma(1,len(s),s)
		f2=self.mult(1,len(s),s)
		return (f1/4000.0)-f2+1.0

