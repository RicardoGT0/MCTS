# -*- coding: utf-8 -*-

import math

class Elliptic:

	def suma(self,ni,nf,s):
		f=0.0
		for n in range(ni-1,nf):
			x=s[n]
			f=(((10.0**6.0)**(n/(nf-1)))*(x**2))+f
		return f

	def func(self,s):
		f=self.suma(1,len(s),s)
		return f

