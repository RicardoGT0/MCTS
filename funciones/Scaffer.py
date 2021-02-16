# -*- coding: utf-8 -*-

import math

class Scaffer:

	def suma(self,ni,nf,s):
		f=0.0
		for n in range(ni-1,nf):
			x=s[n]
			x1=s[n+1]
			f=self.gxy(x,x1)+f	
		return f
	
	def gxy(self,x,y):
		f=0
		f=((math.sin(math.sqrt((x**2)+(y**2))))**2)-0.5
		f=f/((1+(0.001*((x**2)+(y**2))))**2)
		return 0.5+f

	def func(self,s):
		f=self.suma(0,len(s)-1,s)
		return f



	

