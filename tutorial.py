from seals import Integrate,print_graph

param=['seals.py','10','100','0.2'] #you have to do "python seals.py 10 100 0.2" in order to have the same results
t,sol=Integrate(param) #return the solution
print_graph(t,sol) #print the solution