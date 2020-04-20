"""
Do 'python main.py int int float' in ordre to sea the graph.

@authors Guilhem Panneau, Dimitri Mikec, Jonathan Louison

@date 04/20/20
"""

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	from seals import Integrate,print_graph
	import sys

	t, sol=Integrate(sys.argv)
	if t is not(None):
		print_graph(t,sol)

