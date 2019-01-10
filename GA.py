import random
from Chromossome import Chromosome
from Population import Population


class GA():
    IniCoordinate = None
    FinalCoordinate = None

    def __init__(self, IniCoordinate, FinalCoordinate):
        self.IniCoordinate = IniCoordinate
        self.FinalCoordinate = FinalCoordinate


    def Evolution(self, size_pop, Matrix_inf, nGenes, MRate, nGenarations):
        # creates the initial population
        pop = Population(size_pop)
        pop.create_new(Matrix_inf, size_pop, nGenes, True, self.IniCoordinate, self.FinalCoordinate)

        ##evolves the initial population in n generations
        for i in range(nGenarations):
            pop = self.create_new_generation(pop, size_pop, Matrix_inf, nGenes, MRate)
            fittest = pop.Fittest(size_pop)
            print("Path: ", fittest.genes, "Cost:", fittest.cost,"Fitness:", fittest.fitness)
        fittest = pop.Fittest(size_pop)
        ##print solution
        print("\nSolution:")
        print("Path: ", fittest.genes, "Cost:", fittest.cost,"Fitness:", fittest.fitness)

    def create_new_generation(self, pop, size_pop, Matrix_inf, nGenes, MRate):
        newpop = Population(size_pop)
        newpop.chromosomes = []

        # Elitismo
        newpop.chromosomes.append(pop.Fittest(size_pop))

        for i in range(1, size_pop, 1):
            parent1 = self.selection(pop, size_pop)
            parent2 = self.selection(pop, size_pop)

            newpop.chromosomes.append(self.crossover(parent1, parent2, nGenes, Matrix_inf))

        for i in range(1, size_pop, 1):
            newpop.chromosomes[i] = self.mutation(newpop.chromosomes[i], nGenes, MRate, Matrix_inf)

        return (newpop)

    def crossover(self, parent1, parent2, nGenes, Matrix_inf): # crossover de 2 pontos
        position1 = random.randint(0, nGenes - 1)
        position2 = random.randint(0, nGenes - 1)

        child = Chromosome()
        child.genes = []

        if (position1 > position2):
            maior = position1
            position1 = position2
            position2 = maior

        for i in range(nGenes):
            if (position1 <= i <= position2):
                child.genes.append(parent1.genes[i])
            else:
                child.genes.append(None)

        #j=0
        for i in range(nGenes):

                if (child.genes[i] is None):
                    child.genes[i] = parent2.genes[i]
               # j = j+1

        child.generate_cost(Matrix_inf, self.IniCoordinate, self.FinalCoordinate)
        return (child)

    def mutation(self, chromosome, nGenes, MRate, Matrix_inf): #Mutation tipo Swap
        if (random.randint(0, 100) <= MRate):
            position1 = random.randint(0, nGenes - 1)
            position2 = random.randint(0, nGenes - 1)

            getGene = chromosome.genes[position1]
            chromosome.genes[position1] = chromosome.genes[position2]
            chromosome.genes[position2] = getGene
            chromosome.generate_cost(Matrix_inf, self.IniCoordinate, self.FinalCoordinate)
        return (chromosome)

    def selection(self, pop, npop): #Torneio
        fitpop = Population(npop)
        quantity = random.randint(1, npop)
        for i in range(quantity):
            add = random.randint(0, npop - 1)
            fitpop.chromosomes.append(pop.chromosomes[add])
        fit = fitpop.Fittest(quantity)
        return (fit)
