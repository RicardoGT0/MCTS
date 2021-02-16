# -*- coding: utf-8 -*-

import math

class Weierstrass:

	def sumaK(self,x):
		a=0.5
		b=3.0	
		fk=0.0
		for k in range(0,21):
			fk=((a**k)*math.cos((2*math.pi*(b**k))*(x+0.5)))+fk	
		return fk

	def sumaD(self,ni,nf,s):
		fd=0
		for n in range(ni-1,nf):
			x=s[n]
			fd=self.sumaK(x)+fd
		return fd

	def func(self,s):
		d=len(s)
		fd=self.sumaD(1,d,s)
		fk=self.sumaK(0)
		return fd-(d*fk)

