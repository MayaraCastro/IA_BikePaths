from GA import GA
from PrepareData import PrepareData

#Preparing the data
data = PrepareData('ciclovias.arff')

size_pop=50 #size of population
nGenes= len(data.bikePaths )#number of genes in a chromosome/number of bike paths
MRate= 5 #mutation rate
nGenarations=100 #quantity of generations
#avaliar mudando as configurações

IniCoordinate = [-34,-8.05]
FinalCoordinate = [-34,-8.09]

BikeRoute=GA(IniCoordinate, FinalCoordinate)
BikeRoute.Evolution(size_pop,data.bikePaths,nGenes,MRate,nGenarations)