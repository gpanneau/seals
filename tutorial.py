import seals

param=[4,10,100,0.2] #you have to do "python seals.py 10 100 0.2" in order to have the same results
t,sol=seals.Integrate(param) #return the solution
seals.print_graph(t,sol) #print the solution