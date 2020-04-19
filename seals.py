import sys
import pylab as plt
import scipy.integrate as itg
import numpy as np



def ODEs_system(y,t,ff,gf,fg,hg,hh,gh,sea_sand,extraction_sand):
	"""
	Computes the derivative of y at t.

	Parameters :
	- y (list of 3 floats) - Number of seals, soles and lugworms at time t in the bay
	- t (float) - Time parameter
	- ff (float) - Seals death rate
	- gf (float) - Seals growth rate because of the soles consumptuion
	- fg (float) - Rate of soles eaten by the seals
	- hg (float) - Soles growth rate because of the soles consumptuion
	- hh (float) - Lugworms growth rate
	- gh (float) - Rate of lugworms eaten by the soles
	- sea_sand (float) - Impact of the sanding (on the lugworms)
	- extraction_sand (float) - Impact of the sand dredging (on the lungworms)

	Return :
	- dydt (list of 3 floats) - Derivate of y at t
	"""
	dydt=[y[0]*(ff+gf*y[1]),
		y[1]*(fg*y[0]+hg*y[2]),
		y[2]*(hh+sea_sand-extraction_sand+gh*y[1])-extraction_sand]
	return(dydt)

def sand_list(sea_sand,extraction_sand,nb_step_extraction,nb_step):
	"""
	Computes the quantity of sand in the bay at each time t.

	Parameters :
	- sea_sand (float) - Impact of the sanding (on the sand quantity)
	- extraction_sand (float) - Impact of the sand dredging (on the sand quantity)
	- nb_step_extraction (int) - Number of extraction time
	- nb_step (int) - Number of different time
	
	Return :
	- sand (list of floats) - Quantity of sand in the bay (rate in comparison to the initial value)
	"""
	sand=[1.]
	for k in range(nb_step_extraction):
		sand.append(sand[k]+sea_sand-extraction_sand)
	for k in range(nb_step_extraction,nb_step):
		sand.append(sand[k]+sea_sand)
	return(sand)

def print_graph(t,sol):
	"""
	Print the results (4 graphics).

	Parameters : 
	- t : A sequence of time points for which the system has been solved.
	- sol : A list of 4 lists of floats. The first list is the quantity of seals, the second list is the quantity of soles, the third list is the quantity of lugworms and the fourth list is the quantity of sand.
	Return : 
	- None
	"""

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
	return(None)

def Integrate(param=sys.argv):
	"""
	Integrate the system for the given parameters.

	Parameters:
	- param : parameters given by the user thanks to sys.argv. The parameters are the duration of the extraction, the duration of the experiment and the sand extraction rate.

	Return:
	- (None,None) if there is a problem
	- else it returns (t,sol) with :
		- t : A sequence of time points for which the system has been solved.
		- sol : A list of 4 lists of floats. The first list is the quantity of seals, the second list is the quantity of soles, the third list is the quantity of lugworms and the fourth list is the quantity of sand.

	"""
	if len(param)!=4:
		print('You should give 3 parameters : the duration of the extraction, the duration of the experiment and the sand extraction rate.')
		return(None,None)
	t_max_extraction,t_max,extraction_sand=int(param[1]),int(param[2]),float(param[3])
	nb_step=t_max*20
	nb_step_extraction=t_max_extraction*20
	nb_step_without_extraction=nb_step-nb_step_extraction

	sea_sand=0.0001
	extraction_sand/=nb_step_extraction
	sand=sand_list(sea_sand,extraction_sand,nb_step_extraction,nb_step)

	if t_max_extraction>t_max:
		print("The duration of the experiment t_max should be longer than the duration of the extraction t_max_extraction")
		return(None,None)
	if sand[-1]<0:
		print("The value of extraction is too big, you removed all the sand of the bay!")
		return(None,None)
	"""données initiales"""
	S0=70
	Nseals=500
	Nsoles=50000
	Nlugworms=1e9
	init=[Nseals,Nsoles,Nlugworms,S0]

	f=1.
	g=1.
	h=1.

	ff=-0.2
	fg=-0.4
	hh=0.6
	gf=-ff
	hg=-fg
	gh=-hh


	Y = [f,g,h]
	t_extraction = np.linspace(0, t_max, nb_step_extraction+1)
	t_without_extraction=np.linspace(0, t_max-t_max_extraction, nb_step_without_extraction)
	t = np.linspace(0, t_max, nb_step+1)

	res_extraction = itg.odeint(ODEs_system,Y,t_extraction,args=(ff,gf,fg,hg,hh,gh,sea_sand,extraction_sand))
	res_without_extraction=itg.odeint(ODEs_system,res_extraction[-1],t_without_extraction,args=(ff,gf,fg,hg,hh,gh,sea_sand,0.))
	sol=[[],[],[],[]]
	for i in range(3):
		for k in range(len(res_extraction)):
			sol[i].append(res_extraction[k][i]*init[i])
		for k in range(len(res_without_extraction)):
			sol[i].append(res_without_extraction[k][i]*init[i])
	for k in range(len(sand)):
		sol[3].append(sand[k]*init[3])
	return(t,sol)

if __name__ == "__main__":
	t,sol=Integrate()
	if t is None:
		print('There is a problem')
	else:
		print_graph(t,sol)