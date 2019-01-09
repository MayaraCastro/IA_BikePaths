import random 
from Chromossome import Chromosome

class Population():
    chromosomes=None
    population_size = 0

    def __init__(self, size_pop):
        self.chromosomes = []
        self.population_size = size_pop

    def create_new(self,Matrix_inf,size_pop,nGenes,initializing, IniCoordinate, FinalCoordinate):
        for i in range(size_pop):     
            new=Chromosome()
            if(initializing):
                new.create_new(Matrix_inf,nGenes, IniCoordinate, FinalCoordinate)
            self.chromosomes.append(new)

    def Return_chromo(self,i):
        return(self.chromosomes[i])

    def Fittest(self,nGenes):

        fit=self.chromosomes[0]
        for i in range(nGenes):
            if(fit.fitness<self.chromosomes[i].fitness):
                    fit=self.chromosomes[i]
        return(fit)