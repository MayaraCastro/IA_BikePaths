from scipy.io import arff
import pandas as pd
from BikePath import BikePath

data = arff.loadarff('ciclovias.arff')
df = pd.DataFrame(data[0])
id = 0

bikePaths = []
bikePaths.insert(0,BikePath(0))

for i in range(df.icol(0).size):
    if(id != df.at[i,'ID']):

        id = int(df.at[i, 'ID'])
        bikePaths.insert(id,BikePath(id))

    bikePaths[int(id)].addCoordinates(df.at[i,'Longitude'], df.at[i,'Latitude'])

print(bikePaths[0].id)
print(bikePaths[0].coordinates)
print(bikePaths[0].getCoordinatesSize())
'''
## fazer a matrix de distancia entre ciclovias
Matrix_Dist = []

import math

def dist_euclidiana(v1, v2):
	dim, soma = len(v1), 0
	for i in range(dim):
		soma += math.pow(v1[i] - v2[i], 2)
	return math.sqrt(soma)

y = 16
x = 6
for j in range(len(bikePaths[y].coordinates)):
    for i in range(len(bikePaths[x].coordinates)):
        coordA = bikePaths[y].coordinates[j]

        coordB = bikePaths[x].coordinates[i]

        Matrix_Dist.append([dist_euclidiana(coordA, coordB),coordB] )


Matrix_Dist.sort()
print(Matrix_Dist[0][1])
'''
df.head()

from GA import GA


size_pop=5 #size of population
nGenes= len(bikePaths )#number of genes in a chromosome/number of bike paths
MRate=50 #mutation rate
nGenarations=100 #quantity of generations

IniCoordinate = [-34, -8]
FinalCoordinate = [-33, -7]

BikeRoute=GA(IniCoordinate, FinalCoordinate)
BikeRoute.Evolution(size_pop,bikePaths,nGenes,MRate,nGenarations)