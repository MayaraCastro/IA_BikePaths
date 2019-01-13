import random
from Chromossome import Chromosome
from Population import Population


class GA():
    # Problem configuration
    IniCoordinate = None
    FinalCoordinate = None
    Matrix_inf = None
    size_pop = 0
    nGenes = 0

    # Parameters
    MRate = 0
    CRate = 0
    nGenerations = 0

    #Results
    resultado_fitness = None
    resultado_generation = None
    fittest_cost = 0

    def __init__(self, IniCoordinate, FinalCoordinate, size_pop, Matrix_inf, nGenes):
        #Problem configuration
        self.IniCoordinate = IniCoordinate
        self.FinalCoordinate = FinalCoordinate
        self.Matrix_inf = Matrix_inf
        self.size_pop = size_pop
        self.nGenes = nGenes
        self.resultado_fitness = []
        self.resultado_generation = []

    def Evolution(self, MRate, CRate, nGenerations):

        self.MRate = MRate
        self.CRate = CRate
        self.nGenerations = nGenerations

        # creates the initial population
        pop = Population(self.size_pop)
        pop.create_new(self.Matrix_inf, self.size_pop, self.nGenes, True, self.IniCoordinate, self.FinalCoordinate)

        fittest = pop.Fittest(self.size_pop)

        print("Path: ", fittest.genes, "Cost:", fittest.cost, "Fitness:", fittest.fitness)
        self.resultado_fitness.append(fittest.fitness)
        self.resultado_generation.append(0)

        ##evolves the initial population in n generations
        for i in range(1,self.nGenerations):
            pop = self.create_new_generation(pop)
            fittest = pop.Fittest(self.size_pop)
            print("Path: ", fittest.genes, "Cost:", fittest.cost,"Fitness:", fittest.fitness)

            self.resultado_fitness.append(fittest.fitness)
            self.resultado_generation.append(i)

        fittest = pop.Fittest(self.size_pop)

        ##print solution
        print("\nSolution:")
        print("Path: ", fittest.genes, "Cost:", fittest.cost,"Fitness:", fittest.fitness)
        self.fittest_cost = fittest.cost

    def create_new_generation(self, pop):
        newpop = Population(self.size_pop)
        newpop.chromosomes = []

        # Elitismo
        newpop.chromosomes.append(pop.Fittest(self.size_pop))

        for i in range(1, self.size_pop, 1):
            parent1 = self.selection(pop)
            parent2 = self.selection(pop)

            if (random.randint(0, 100) <= self.CRate):
                newpop.chromosomes.append(self.crossover(parent1, parent2))
            else:
                newpop.chromosomes.append(parent1)

        for i in range(1, self.size_pop, 1):
            newpop.chromosomes[i] = self.mutation(newpop.chromosomes[i])

        return (newpop)

    def crossover(self, parent1, parent2): # crossover de 2 pontos
        position1 = random.randint(0, self.nGenes - 1)
        position2 = random.randint(0, self.nGenes - 1)

        child = Chromosome()
        child.genes = []

        if (position1 > position2):
            maior = position1
            position1 = position2
            position2 = maior

        for i in range(self.nGenes):
            if (position1 <= i <= position2):
                child.genes.append(parent1.genes[i])
            else:
                child.genes.append(None)

        #j=0
        for i in range(self.nGenes):

                if (child.genes[i] is None):
                    child.genes[i] = parent2.genes[i]
               # j = j+1

        child.generate_cost(self.Matrix_inf, self.IniCoordinate, self.FinalCoordinate)
        return (child)

    def mutation(self, chromosome): #Mutation tipo Swap

        for i in range(self.nGenes): #for each position of the cromosome test the occurance of the mutation

            if (random.randint(0, 100) <= self.MRate):
                position1 = i
                position2 = random.randint(0, self.nGenes - 1)

                getGene = chromosome.genes[position1]
                chromosome.genes[position1] = chromosome.genes[position2]
                chromosome.genes[position2] = getGene
                chromosome.generate_cost(self.Matrix_inf, self.IniCoordinate, self.FinalCoordinate)

        return (chromosome)

    def selection(self, pop): #Torneio
        fitpop = Population(self.size_pop)
        quantity = random.randint(1, self.size_pop)
        for i in range(quantity):
            add = random.randint(0, self.size_pop - 1)
            fitpop.chromosomes.append(pop.chromosomes[add])
        fit = fitpop.Fittest(quantity)
        return (fit)
