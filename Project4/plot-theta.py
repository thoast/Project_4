# -*- coding: utf-8 -*-
from matplotlib.pyplot import *
from numpy import *

def get_data(txtfile):
	with open(txtfile,"r") as infile:
		data = {}
		identifiers = infile.readline().split()
		for identifier in identifiers:
			data[identifier] = []

		lines = infile.readlines()
		for line in lines: 
			values = line.split()
			for identifier,value in zip(identifiers,values):
				data[identifier].append(float(value))
		for identifier in identifiers:
			data[identifier] = array(data[identifier])
	return data



b_4 = get_data("MC100000T1N2.txt")
#plot(sqrt(planet["x"]*planet["x"] + planet["y"]*planet["y"]),"r-",label="r")
plot(abs(b_4["E/N"]))
plot([0,len(b_4["E/N"])],[1.99598208594,1.99598208594],"g--")
#ylim( (0, 2.1) )
legend(loc="best")
grid("on")
savefig("test.pdf")
show()


plot(abs(b_4["E/N"])-1.99598208594)
show()