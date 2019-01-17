from GA import GA
from PrepareData import PrepareData
import numpy as np

#Preparing the data
data = PrepareData('ciclovias.arff')
'''
CONF 1
size_pop=50 #size of population
nGenes= len(data.bikePaths )#number of genes in a chromosome/number of bike paths
MRate= 5 #mutation rate
CRate = 90 #crossover rate
nGenerations=100 #quantity of generations

2
size_pop=50 #size of population
nGenes= len(data.bikePaths )#number of genes in a chromosome/number of bike paths
MRate= 1 #mutation rate
CRate = 95 #crossover rate
nGenerations=100 #quantity of generations

3
size_pop=50 #size of population
nGenes= len(data.bikePaths )#number of genes in a chromosome/number of bike paths
MRate= 2 #mutation rate
CRate = 60 #crossover rate
nGenerations=300 #quantity of generations
'''
size_pop=30 #size of population
nGenes= len(data.bikePaths )#number of genes in a chromosome/number of bike paths
MRate= 5 #mutation rate
CRate = 75 #crossover rate
nGenerations=200 #quantity of generations

IniCoordinate = [-34.873742,-8.049938] #11
FinalCoordinate = [-34.88354,-8.0434]#9

BikeRoute=GA(IniCoordinate, FinalCoordinate, size_pop,data.bikePaths,nGenes)
BikeRoute.Evolution(MRate, CRate, nGenerations)
'''
sum = 0
times = 30
fittests = []
for i in range(times):
    BikeRoute.Evolution(MRate, CRate, nGenerations)
    sum = sum + BikeRoute.fittest_cost
    fittests.append(BikeRoute.fittest_cost)

fittests.sort()
min = fittests[0]
max = fittests[times - 1]
avg = sum/times
std = np.std(fittests)
configuracao = 4

min_max_avg_std = configuracao,min,max,avg,std
data.writeCSV('100Gen.csv', min_max_avg_std)
'''