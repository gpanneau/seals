#! /usr/bin/env python

import sys
import pylab as plt
import scipy.integrate as itg
import numpy as np

def ODEs_system_without_extraction(Y,t,ff,gf,fg,hg,hh,gh,sea_sand):
	Y=[Y[0]*(ff+gf*Y[1]),
		Y[1]*(fg*Y[0]+hg*Y[2]),
		Y[2]*(hh+sea_sand+gh*Y[1])]
	print(Y)
	return(Y)

def ODEs_system_extraction(Y,t,ff,gf,fg,hg,hh,gh,sea_sand,extraction_sand):
	Y=[Y[0]*(ff+gf*Y[1]),
		Y[1]*(fg*Y[0]+hg*Y[2]),
		Y[2]*(hh+sea_sand-extraction_sand+gh*Y[1])-extraction_sand]
	return(Y)

def sand_list(sea_sand,extraction_sand,nb_step_extraction,nb_step):
	sand=[1]
	for k in range(nb_step_extraction):
		sand.append(sand[k]+sea_sand-extraction_sand)
	for k in range(nb_step_extraction,nb_step):
		sand.append(sand[k]+sea_sand)
	return(sand)

def print_graph(t,res_extraction,res_without_extraction,sand,init):
	sol=[[],[],[],[]]
	for i in range(3):
		for k in range(len(res_extraction)):
			sol[i].append(res_extraction[k][i]*init[i])
		for k in range(len(res_without_extraction)):
			sol[i].append(res_without_extraction[k][i]*init[i])
	for k in range(len(sand)):
		sol[3].append(sand[k]*init[3])
	plt.figure()
	plt.subplot(221)
	plt.plot(t,sol[0],label="Modèle proie prédateur")
	plt.xlabel("années")
	plt.ylabel("effectifs")
	plt.title("Evolution du nombre de phoques en fonction du temps")
	plt.legend()

	plt.subplot(222)
	plt.plot(t,sol[1],label="Modèle proie prédateur")
	plt.xlabel("années")
	plt.ylabel("effectifs")
	plt.title("Evolution du nombre de soles en fonction du temps")
	plt.legend()

	plt.subplot(223)
	plt.plot(t,sol[2],label="Modèle proie prédateur")
	plt.xlabel("années")
	plt.ylabel("effectifs")
	plt.title("Evolution du nombre d'arénicoles en fonction du temps")
	plt.legend()

	plt.subplot(224)
	plt.plot(t,sol[3],label="Sable dans la baie")
	plt.xlabel("années")
	plt.ylabel("Quantité de sable")
	plt.legend()

	plt.show()


def main():
	t_max_extraction=25
	t_max = 300
	nb_step=t_max*20
	nb_step_extraction=t_max_extraction*20
	nb_step_without_extraction=nb_step-nb_step_extraction

	sea_sand=0.0001
	extraction_sand=0.001

	"""données initiales"""
	S0=70
	Nseals=500
	Nsoles=50000
	Nlugworms=1e9
	init=[Nseals,Nsoles,Nlugworms,S0]

	f=1
	g=1
	h=1

	ff=-0.2
	fg=-0.4@@	
	hh=0.2

	gf=-ff
	hg=-fg
	gh=-hh


	Y = [f,g,h]
	t_extraction = np.linspace(0, t_max, nb_step_extraction+1)
	t_without_extraction=np.linspace(0, t_max-t_max_extraction, nb_step_without_extraction)
	t = np.linspace(0, t_max, nb_step+1)

	res_extraction = itg.odeint(ODEs_system_extraction,Y,t_extraction,args=(ff,gf,fg,hg,hh,gh,sea_sand,extraction_sand))
	res_without_extraction=itg.odeint(ODEs_system_without_extraction,res_extraction[-1],t_without_extraction,args=(ff,gf,fg,hg,hh,gh,sea_sand))

	print_graph(t,res_extraction,res_without_extraction,sand_list(sea_sand,extraction_sand,nb_step_extraction,nb_step),init)
	return(0)

if __name__ == "__main__":
	main()