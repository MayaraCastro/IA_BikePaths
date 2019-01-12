from GA import GA
from PrepareData import PrepareData

#Preparing the data
data = PrepareData('ciclovias.arff')

size_pop=50 #size of population
nGenes= len(data.bikePaths )#number of genes in a chromosome/number of bike paths
MRate= 5 #mutation rate
CRate = 90 #crossover rate
nGenarations=100 #quantity of generations

#TODO avaliar mudando as configurações 3 combinações

IniCoordinate = [-34,-8.05]
FinalCoordinate = [-34,-8.09]

BikeRoute=GA(IniCoordinate, FinalCoordinate, size_pop,data.bikePaths,nGenes)
BikeRoute.Evolution(MRate, CRate, nGenarations)