# -*- coding: utf-8 -*-

import math

class Rosenbrock:
	def suma(self,ni,nf,s):
		f=0.0
		for n in range(ni-1,nf):
			x=s[n]
			x1=s[n+1]
			f= (100.0*(((x**2.0)-x1)**2.0)+((x-1.0)**2.0)) + f

		return f

	def func(self,s,ni=1):
		f=self.suma(ni,len(s)-1,s)

		return f

