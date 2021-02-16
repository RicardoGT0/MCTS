# -*- coding: utf-8 -*-

import math

class HGBat:

	def suma(self,ni,nf,s,ex):
		f=0.0
		for n in range(ni-1,nf):
			x=s[n]
			f=(x**ex)+f
		return f

	def func(self,s):
		f1=self.suma(1,len(s),s,2.0)**2.0
		f1=f1-(self.suma(1,len(s),s,1.0)**2.0)
		f1=math.fabs(f1)**(1.0/2.0)

		f2=(0.5*self.suma(1,len(s),s,2.0))+self.suma(1,len(s),s,1.0)
		f2=f2/len(s)

		return f1+f2+0.5

