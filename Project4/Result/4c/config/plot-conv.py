# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from matplotlib.pyplot import *
from numpy import *
import re
import os

output = Popen(["ls"], stdout=PIPE).communicate()[0]
txtfiles = re.findall(".*\.txt",output,re.IGNORECASE)


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


for txtfile in txtfiles:
	b_4 = get_data(txtfile)
	#plot(sqrt(planet["x"]*planet["x"] + planet["y"]*planet["y"]),"r-",label="r")
	plot(b_4["MC"][:10000]*100*100/len(b_4["MC"]),b_4["CONFIG"][:10000]*100,"r-")
	legend(loc="best")
	ylabel("Accepted configurations per MC [%]",fontsize=20)
	xlabel("MC cycles [%]",fontsize=20)
	grid("on")
	tight_layout()
	savefig("energy22-%s.pdf" % txtfile[:-4])
	clf()
