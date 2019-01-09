import random
import math

class Chromosome():
    genes=[]
    cost=0
    fitness=0.0
    def __init__(self):
        self.genes = []

    def generate_cost(self,Matrix_inf, IniCoordinate, FinalCoordinate): #TODO mudar o calculo do custo
        self.cost=0
        x=self.genes[0]

        Matrix_Dist = []
        coordA = IniCoordinate

        for i in (self.genes):

            ##
            Matrix_Dist.clear()

            ##Calculates the shortest distance beetween the next path and the actual coordinate,
            ##and gets the next coordinate(the one with the shortest distance)
            print('x: ', x, "genes: ", self.genes)

            for n in range(len(Matrix_inf[x].coordinates)):
                coordB = Matrix_inf[x].coordinates[n]

                Matrix_Dist.append([self.dist_euclidiana(coordA, coordB), coordB])

            Matrix_Dist.sort()
            coordA = Matrix_Dist[0][1]

            self.cost = self.cost + Matrix_Dist[0][0]
            x = i

        self.cost = self.cost + self.dist_euclidiana(coordA, FinalCoordinate) # Adds the distance of the last path to the final point
            ##


        self.generate_fitness()

    def generate_fitness(self):
        self.fitness=1.0/self.cost

    def create_new(self,Matrix_inf,nGenes, IniCoordinate, FinalCoordinate):
        g=[]
        for i in range(nGenes):
            g.append(i)
        random.shuffle(g)
        self.genes=g
        self.generate_cost(Matrix_inf, IniCoordinate, FinalCoordinate)

    def gene(self,i):
        return(self.genes[i])

    def contains_gene(self,gene,nGenes):
        found=False
        for i in range(nGenes):
            if(self.genes[i]== gene):
                found=True
                return(found)
        return(found)

    def dist_euclidiana(self, v1, v2):
        dim, soma = len(v1), 0
        for i in range(dim):
            soma += math.pow(v1[i] - v2[i], 2)
        return math.sqrt(soma)