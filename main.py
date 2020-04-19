from seals import Integrate,print_graph
import sys

t,sol=Integrate(sys.argv)
if t is not(None):
	print_graph(t,sol)

