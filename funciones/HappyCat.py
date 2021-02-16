# -*- coding: utf-8 -*-

import math

class HappyCat:

	def suma(self,ni,nf,s,ex):
		f=0.0
		for n in range(ni-1,nf):
			x=s[n]
			f=(x**ex)+f
		return f

	def func(self,s):
		d=len(s)

		f1=self.suma(1,d,s,2.0)-d
		f1=math.fabs(f1)**(1.0/4.0)

		f2=(0.5*self.suma(1,d,s,2.0))+self.suma(1,d,s,1.0)
		f2=f2/d

		return f1+f2+0.5

