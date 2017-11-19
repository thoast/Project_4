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
		#for identifier in identifiers:
		#	data[identifier] = array(data[identifier])
	return data


data_size = {}
for txtfile in txtfiles:
	size = int(txtfile[6:-10])
	data = get_data(txtfile)
	
	if size not in data_size.keys():
		data_size[size] = data
	else:
		for key in data.keys():
			for value in data[key]:
				data_size[size][key].append(value)



teller = 0
label_dict = {	"E/N" : "E/N",				\
				"E-var/TT" : "$C_V$",		\
				"M-var/T" : "$\chi$",		\
				"Mabs/N": "|M|/N"		}


for key in data_size[data_size.keys()[0]].keys():
	teller += 1
	for size in sorted(data_size.keys()):
		if key == "T":
			None
		elif key == "M/N":
			None
		else:
			plot(data_size[size]["T"],data_size[size][key],"o-",label=size,linewidth=2)
	
	if key == "T":
		None
	elif key == "M/N":
		None
	else:
		legend(loc="best")
		ylabel(label_dict[key],fontsize=20)
		xlabel("T",fontsize=20)
		grid("on")
		tight_layout()
		savefig("%s.pdf" % teller)
		show()