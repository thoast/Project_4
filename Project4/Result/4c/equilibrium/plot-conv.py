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



b_4 = get_data("MC10000000T1N20-term100000.txt")
#plot(sqrt(planet["x"]*planet["x"] + planet["y"]*planet["y"]),"r-",label="r")
plot(linspace(0,100,len(abs(b_4["E/N"]))),b_4["E/N"],"r-",linewidth=1.5)
legend(loc="best")
ylabel("Energy [E/N]",fontsize=20)
xlabel("MC cycles [%]",fontsize=20)
grid("on")
tight_layout()
savefig("E-N20-T1-Term.pdf")
show()


#Mabs/N       
plot(linspace(0,100,len(abs(b_4["Mabs/N"]))),b_4["Mabs/N"],"r-",linewidth=1.5)
legend(loc="best")
ylabel("|M| [|M|/N]",fontsize=20)
xlabel("MC cycles [%]",fontsize=20)
grid("on")
tight_layout()
savefig("M-N20-T1-Term.pdf")
show()

