# -*- coding: utf-8 -*-

import math

class Expanded_GR:

	def suma(self,ni,nf,s):
		f=0.0
		for n in range(ni-1,nf):
			x=s[n]
			x1=s[n+1]
			f=(self.fr(x,x1)**2.0)+f	
		return f
	
	def mult(self,ni,nf,s):
		f=1.0
		for n in range(ni-1,nf):
			x=s[n]
			x1=s[n+1]
			f=(math.cos(self.fr(x,x1)/math.sqrt(n+2)))*f	
		return f

	def func(self,s):
		f1=self.suma(0,len(s)-1,s)
		f2=self.mult(0,len(s)-1,s)
		return (f1/4000.0)-f2+1.0



	def fr(self,x,x1):
		f= (100.0*(((x**2.0)-x1)**2.0))+((x-1)**2.0)
		return f
	

