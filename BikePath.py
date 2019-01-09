

class BikePath():
    id = 0
    coordinates = None
    def __init__(self, id):
        self.id = id
        self.coordinates = []

    def addCoordinates(self, longitude, latitude):
        self.coordinates.append([longitude,latitude])

    def getCoordinatesSize(self):
        return self.coordinates.__len__()

