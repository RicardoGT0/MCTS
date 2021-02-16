# -*- coding: utf-8 -*-

import math

class Xcuadrada:

	def sumax(self,ni,nf,s):
		f=0.0
		for n in range(ni-1,nf):
			x=s[n]
			f=(x**2.0)+f
		return f


	def func(self,s):
		d=len(s)
		f=self.sumax(1,d,s)
	
		return f

