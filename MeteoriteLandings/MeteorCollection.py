import Meteor as mt


class MeteorCollection:
    def __init__(self, meteors):
        self.meteor_collection = meteors

    def extract_meteor_attributes(self):
        longitude_, latitude_, mass_ = [],[],[]
        for a_meteor in self.meteor_collection:
            longitude_.append(a_meteor.longitude)
            latitude_.append(a_meteor.latitude)
            mass_.append(float(a_meteor.mass)/1000)

        return longitude_, latitude_, mass_

    def extract_hover_text(self):
        hover_text = []
        for a_meteor in self.meteor_collection:
            hover_text.append(f'{a_meteor.year}\nName: {a_meteor.name}')

        return hover_text
