# -*- coding: utf-8 -*-
import math

class Schwefels:

	def gz(self,z,s):
			f=0.0
			if math.fabs(z)<=500:
				f=z*math.sin(math.fabs(z)**(1.0/2.0))
			elif z>500:
				f1=math.sqrt(math.fabs(500.0-math.fmod(z,500.0)))
				f2=((z-500.0)**2.0)/(10000.0*len(s))
				f=(500.0-math.fmod(z,500.0))*math.sin(f1)-(f2)
			elif z<-500:
				f1=math.fmod(math.fabs(z),500.0)-500.0
				f2=math.fabs(math.fmod(math.fabs(z),500.0)-500.0)
				f3=((z+500.0)**2.0)/(10000.0*len(s))
				f=(f1*math.sin(f2))-f3
			return f

	def suma(self,ni,nf,s):
		f=0
		for n in range(ni-1,nf):
			x=s[n]
			z=x+(4.209687462275036*(10.0**2.0))
			f=self.gz(z,s)+f	
		return f


	def func(self,s):
		f=(418.9829*len(s)) - self.suma(1,len(s),s)
		return f
