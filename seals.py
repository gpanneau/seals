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

	Exemples:

	>>> ODEs_system([1.,1.,1.],0,-0.2,0.2,-0.4,0.4,0.6,-0.6,1.,0.2)
	[0.0, 0.0, 0.6000000000000001]
	>>> ODEs_system([1.,1.,1.],0,-0.2,0.2,-0.4,0.4,0.6,-0.6,1.,0.2)
	[0.0, 0.0, 0.6000000000000001]
	>>> ODEs_system([1.,1.,1.],0,-0.2,0.2,-0.4,0.4,0.6,-0.6,1.,0.2)
	[0.0, 0.0, 0.6000000000000001]

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
	
	Exemples:
	
	>>> sand_list(0,0,1,1)
	[1.0, 1.0]
	>>> sand_list(0,0.1,1,1)
	[1.0, 0.9]
	>>> sand_list(0.1,0.2,3,5)
	[1.0, 0.9000000000000001, 0.8000000000000003, 0.7000000000000002, 0.8000000000000002, 0.9000000000000001]
	"""
	sand=[1.]
	for k in range(nb_step_extraction):
		sand.append(sand[k]+sea_sand-extraction_sand)
	for k in range(nb_step_extraction,nb_step):
		sand.append(sand[k]+sea_sand)
	return(sand)

def print_graph(t,sol):
	"""
	Print the results (4 graphics : seals(t),soles(t),lugworms(t),sand(t)).

	Parameters : 
	- t : A sequence of time points for which the system has been solved.
	- sol : A list of 4 lists of floats. The first list is the quantity of seals, the second list is the quantity of soles, the third list is the quantity of lugworms and the fourth list is the quantity of sand.
	Return : 
	- None
	"""

	plt.figure()
	plt.subplot(221)
	plt.plot(t,sol[0],label="Modele proie predateur")
	plt.xlabel("annees")
	plt.ylabel("effectifs")
	plt.title("Evolution du nombre de phoques en fonction du temps")
	plt.legend()

	plt.subplot(222)
	plt.plot(t,sol[1],label="Modele proie predateur")
	plt.xlabel("annees")
	plt.ylabel("effectifs")
	plt.title("Evolution du nombre de soles en fonction du temps")
	plt.legend()

	plt.subplot(223)
	plt.plot(t,sol[2],label="Modele proie predateur")
	plt.xlabel("annees")
	plt.ylabel("effectifs")
	plt.title("Evolution du nombre d'arenicoles en fonction du temps")
	plt.legend()

	plt.subplot(224)
	plt.plot(t,sol[3],label="Sable dans la baie")
	plt.xlabel("annees")
	plt.ylabel("Quantite de sable")
	plt.legend()

	plt.show()
	return(None)

def Integrate(param):
	"""
	Integrate the system for the given parameters.
	
	Parameters:
	- param : parameters given by the user. The parameters are the duration of the extraction, the duration of the experiment and the sand extraction rate.

	Return:
	- None if there is a problem
	- else it returns (t,sol) with :
		- t : A sequence of time points for which the system has been solved.
		- sol : A list of 4 lists of floats. The first list is the quantity of seals, the second list is the quantity of soles, the third list is the quantity of lugworms and the fourth list is the quantity of sand.
	
	Exemples:
	
	>>> Integrate(['seals.py','2','1','0'])
	The duration of the experiment t_max should be longer than the duration of the extraction t_max_extraction
	>>> Integrate(['seals.py','2','2','10'])
	The value of extraction is too big, you removed all the sand of the bay!
	>>> Integrate(['seals.py','2','1'])
	You should give 3 parameters : the duration of the extraction, the duration of the experiment and the sand extraction rate.
	>>> Integrate(['seals.py','2','1','10','2'])
	You should give 3 parameters : the duration of the extraction, the duration of the experiment and the sand extraction rate.
	>>> Integrate(['seals.py','0','0','0'])
	t_max_extraction is >=1 ,t_max is >=1 ,extraction_sand is >=0
	>>> Integrate(['seals.py','a','b','c'])
	t_max_extraction is an int, t_max is an int ,extraction_sand is a float
	>>> Integrate(['seals.py','1','1','0'])
	(array([0.  , 0.05, 0.1 , 0.15, 0.2 , 0.25, 0.3 , 0.35, 0.4 , 0.45, 0.5 ,
	       0.55, 0.6 , 0.65, 0.7 , 0.75, 0.8 , 0.85, 0.9 , 0.95, 1.  ]), [[500.0, 500.00000015257507, 500.00000079550244, 500.00000240937794, 500.000005547382, 500.0000105025175, 500.0000178425359, 500.0000281063836, 500.0000418330072, 500.00005956135317, 500.0000818303682, 500.0001091616707, 500.0001419041076, 500.0001804937564, 500.0002254057551, 500.0002771152413, 500.00033609735306, 500.00040282722813, 500.0004777674761, 500.0005612836973, 500.00065379646765], [50000.0, 50000.0024992629, 50000.009995251945, 50000.022482603505, 50000.03994921952, 50000.06236884597, 50000.0897182443, 50000.12197980321, 50000.15913591136, 50000.20116895741, 50000.24806133002, 50000.2997888385, 50000.35626169075, 50000.41742321633, 50000.483231575796, 50000.55364492974, 50000.62862143872, 50000.708119263305, 50000.79208782212, 50000.88040884255, 50000.97300241292], [1000000000.0, 1000004999.0970415, 1000009995.2769244, 1000014985.655995, 1000019966.9149888, 1000024937.295494, 1000029893.3906544, 1000034831.9665273, 1000039749.7891688, 1000044643.6246359, 1000049510.2389853, 1000054346.5021518, 1000059150.3198171, 1000063919.0747213, 1000068649.9154465, 1000073339.9905739, 1000077986.4486853, 1000082586.4383622, 1000087137.183256, 1000091636.4883034, 1000096081.8290241], [70.0, 70.007, 70.014, 70.021, 70.02799999999999, 70.035, 70.042, 70.04899999999999, 70.056, 70.06299999999999, 70.07, 70.077, 70.08399999999999, 70.091, 70.09799999999998, 70.10499999999999, 70.112, 70.11899999999999, 70.12599999999999, 70.13299999999998, 70.13999999999999]])
	>>> Integrate(['seals.py','1','2','0.2'])
	(array([0.  , 0.05, 0.1 , 0.15, 0.2 , 0.25, 0.3 , 0.35, 0.4 , 0.45, 0.5 ,
	       0.55, 0.6 , 0.65, 0.7 , 0.75, 0.8 , 0.85, 0.9 , 0.95, 1.  , 1.05,
	       1.1 , 1.15, 1.2 , 1.25, 1.3 , 1.35, 1.4 , 1.45, 1.5 , 1.55, 1.6 ,
	       1.65, 1.7 , 1.75, 1.8 , 1.85, 1.9 , 1.95, 2.  ]), [[500.0, 499.999862299849, 499.99894290369343, 499.9964295132588, 499.9915448949694, 499.9835126146087, 499.97156814026533, 499.95496036282503, 499.93295584636166, 499.9048402605752, 499.86992001539386, 499.8275261012962, 499.77701555396106, 499.71777282522675, 499.64921375906914, 499.5707845997813, 499.48196447880287, 499.38226870810377, 499.271251798354, 499.14850561065083, 499.0136572365501, 499.0136572365501, 498.93773172538425, 498.85843025261477, 498.7758199035785, 498.6899821000173, 498.60099454445844, 498.5089343244336, 498.4138845689059, 498.31592935430774, 498.2151559297284, 498.1116532350304, 498.0055129590285, 497.89682878330325, 497.785697244278, 497.67221507022293, 497.5564818896887, 497.4386001834204, 497.3186729138432, 497.19680396495403, 497.07309980039076], [50000.0, 49998.01134516324, 49992.05474298154, 49982.154437241355, 49968.34810405776, 49950.68632714373, 49929.23265902996, 49904.06373341857, 49875.26815383698, 49842.946520927224, 49807.210155053224, 49768.18135575461, 49725.99263647713, 49680.786376974975, 49632.713594390574, 49581.93428871339, 49528.61661785892, 49472.93520080924, 49415.07093110304, 49355.21058351268, 49293.546579370566, 49293.546579370566, 49260.97116262486, 49229.0508184479, 49197.80958651686, 49167.27613598066, 49137.47516526732, 49108.430358435886, 49080.165135277224, 49052.702644995254, 49026.065134147226, 49000.274330364315, 48975.35105183696, 48951.31557820296, 48928.18731976095, 48905.98514712158, 48884.72703839777, 48864.43008531079, 48845.11076168766, 48826.78487515795, 48809.46738508631], [1000000000.0, 998011809.3988706, 996030257.2438616, 994060166.3436931, 992106117.0481589, 990172654.7851391, 988264224.6460229, 986385162.7321596, 984539675.7175285, 982731833.7257658, 980965565.1495647, 979244636.0855192, 977572645.3081262, 975953018.3397909, 974388991.4838066, 972883615.5896423, 971439746.2742897, 970060034.0185175, 968746908.2389302, 967502588.7194524, 966329097.7148334, 966329097.7148334, 966775405.7613055, 967241623.6319724, 967727396.1555673, 968232291.9638138, 968755897.5396574, 969297802.0343143, 969857560.5239522, 970434722.4436969, 971028818.3531406, 971639368.5199152, 972265876.1013764, 972907832.5436581, 973564711.984516, 974235984.97523, 974921104.4341844, 975619505.895799, 976330619.6879712, 977053868.6767311, 977788659.7652326], [70.0, 69.307, 68.614, 67.92099999999999, 67.228, 66.535, 65.84199999999998, 65.14899999999999, 64.45599999999999, 63.76299999999999, 63.069999999999986, 62.37699999999998, 61.68399999999998, 60.990999999999985, 60.29799999999998, 59.604999999999976, 58.91199999999998, 58.21899999999998, 57.525999999999975, 56.83299999999997, 56.13999999999997, 56.14699999999997, 56.15399999999997, 56.16099999999997, 56.16799999999997, 56.17499999999997, 56.18199999999997, 56.188999999999965, 56.19599999999997, 56.20299999999997, 56.209999999999965, 56.21699999999996, 56.22399999999996, 56.23099999999996, 56.237999999999964, 56.24499999999996, 56.25199999999996, 56.25899999999996, 56.265999999999956, 56.27299999999996, 56.27999999999996]])
	"""

	#Import of values
	if len(param)!=4:
		print('You should give 3 parameters : the duration of the extraction, the duration of the experiment and the sand extraction rate.')
		return(None)
	try:
		t_max_extraction,t_max,extraction_sand=int(param[1]),int(param[2]),float(param[3])
	except:
		print('t_max_extraction is an int, t_max is an int ,extraction_sand is a float')
		return(None)
	if t_max_extraction<1 or t_max<1 or extraction_sand<0:
		print('t_max_extraction is >=1 ,t_max is >=1 ,extraction_sand is >=0')
		return(None)
	nb_step=t_max*20
	nb_step_extraction=t_max_extraction*20
	nb_step_without_extraction=nb_step-nb_step_extraction

	sea_sand=0.0001
	extraction_sand/=nb_step_extraction
	sand=sand_list(sea_sand,extraction_sand,nb_step_extraction,nb_step)

	if t_max_extraction>t_max:
		print("The duration of the experiment t_max should be longer than the duration of the extraction t_max_extraction")
		return(None)
	if sand[-1]<0:
		print("The value of extraction is too big, you removed all the sand of the bay!")
		return(None)

	#Data
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

	#Integrate with odeint
	res_extraction = itg.odeint(ODEs_system,Y,t_extraction,args=(ff,gf,fg,hg,hh,gh,sea_sand,extraction_sand))
	res_without_extraction=itg.odeint(ODEs_system,res_extraction[-1],t_without_extraction,args=(ff,gf,fg,hg,hh,gh,sea_sand,0.))

	#enhancement of our data
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
	import doctest
	doctest.testmod()