from scipy.io import arff
import pandas as pd
from BikePath import BikePath

class PrepareData():
    bikePaths = None

    def __init__(self,path):
        data = arff.loadarff(path)
        df = pd.DataFrame(data[0])
        id = 0

        self.bikePaths = []
        self.bikePaths.insert(0, BikePath(0))

        for i in range(df.icol(0).size):
            if (id != df.at[i, 'ID']):
                id = int(df.at[i, 'ID'])
                self.bikePaths.insert(id, BikePath(id))

            self.bikePaths[int(id)].addCoordinates(df.at[i, 'Longitude'], df.at[i, 'Latitude'])

        df.head()
