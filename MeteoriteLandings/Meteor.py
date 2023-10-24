class Meteor:
    def __init__(self, name, id, recclass, latitude, longitude, year, mass):
        self.name = name
        self.id = id
        self.recclass = recclass
        self.latitude = latitude
        self.longitude = longitude
        self.year = year
        self.mass = mass

    def __str__(self):
        str1 = f'Name: {self.name} Id: {self.id} Recclass: {self.recclass} '
        str2 = f'Latitude: {self.latitude} Longitude: {self.longitude} '
        str3 = f'Year: {self.year} Mass: {self.mass}'

        return str1 + str2 + str3

