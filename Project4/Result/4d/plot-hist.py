# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from matplotlib.pyplot import *
from numpy import *
import re
import os

output = Popen(["ls"], stdout=PIPE).communicate()[0]
txtfiles = re.findall(".*\.txt",output,re.IGNORECASE)

def make_histogram_dict(txtfile):
	E_dict = {}
	E_test_list = []
	with open(txtfile,"r") as infile:
		infile.readline()
		for line in infile:
			E_value = float(line.split()[-1])
			E_test_list.append(E_value)
			if E_value in E_dict.keys():
				E_dict[E_value] += 1
			else:
				E_dict[E_value] = 1

	E_list = []
	key_list = sorted(E_dict.keys())
	for key in key_list:
		E_list.append(E_dict[key])

	summen = float(sum(E_list))
	for i in range(len(E_list)):
		E_list[i] = E_list[i]/summen

	return E_test_list,key_list,E_list

for txtfile in txtfiles:
	hist_list,x,y = make_histogram_dict(txtfile)
	plot(x,y,linewidth=2)
	xlabel('Energy [E/N]',fontsize=20)
	ylabel('Probability [%]',fontsize=20)
	grid("on")
	tight_layout()
	savefig("%s.pdf" % txtfile[:-4])
	show()

	hist(hist_list,bins=linspace(min(x),max(x),len(x)+0.15*len(x)),histtype="bar", normed=1, facecolor='green')
	xlabel('Energy [E/N]',fontsize=20)
	ylabel('Probability [%]',fontsize=20)
	grid("on")
	tight_layout()
	savefig("%s-hist.pdf" % txtfile[:-4])
	show()