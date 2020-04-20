"""
This is a tutorial of our program. This equivalent to : 'python main.py 20 200 0.2'

@authors Guilhem Panneau, Dimitri Mikec, Jonathan Louison

@date 04/20/20
"""

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	from seals import Integrate,print_graph

	param=['seals.py','10','100','0.2'] #you have to do "python seals.py 10 100 0.2" in order to have the same results
	t,sol=Integrate(param) #return the solution
	print_graph(t,sol) #print the solution