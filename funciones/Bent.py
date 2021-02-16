# -*- coding: utf-8 -*-

import math

class Bent:	

	def suma(self,ni,nf,s):
		f=0.0
		for n in range(ni-1,nf):
			x=s[n]
			f=(x**2.0)+f	
		return f
	
	def func(self,s):
		f=self.suma(2,len(s),s)
		return (f*(10.0**6.0))+(s[0]**2.0)


