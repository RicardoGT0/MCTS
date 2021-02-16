# -*- coding: utf-8 -*-

import math

class Rastrigin:

	def suma(self,ni,nf,s):
		f=0.0
		for n in range(ni-1,nf):
			x=s[n]
			f=((x**2.0)-(10.0*math.cos(2.0*math.pi*x))+10.0)+f
		return f

	def func(self,s):
		f=self.suma(1,len(s),s)
		return f

