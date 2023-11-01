import sys
import HttpRequest as ht
import Meteor as mt
import MeteorCollection as mc
import plotly.express as px



# =====================================
def extract_meteors_to_list(meteors_json):
    meteors = []
    for a_meteor in meteors_json:
        try:
            m = mt.Meteor(name=a_meteor['name'],
                          id=a_meteor['id'],
                          recclass=a_meteor['recclass'],
                          latitude=a_meteor['geolocation']['latitude'],
                          longitude=a_meteor['geolocation']['longitude'],
                          year=a_meteor['year'],
                          mass=a_meteor['mass']
                          )
        except KeyError:
            pass
        else:
            meteors.append(m)

    return meteors
# =====================================


def main() -> int:
    """Echo the input arguments to standard output"""
    url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
    my_request = ht.myHttpRequest(url)

    my_request.get_http_request()
    meteors_json = my_request.get_json()

    meteors_list = []
    meteors_list = extract_meteors_to_list(meteors_json)
    meteor_collection = mc.MeteorCollection(meteors_list)

    # Show in geo location map
    longitudes, latitudes, masses = meteor_collection.extract_meteor_attributes()

    map_title = 'Meteoroid impacts on Earth'
    hover_text = meteor_collection.extract_hover_text()

    fig = px.scatter_geo(lat=latitudes, lon=longitudes, title=map_title,
                         color=masses,
                         color_continuous_scale='earth',
                         labels={'color': 'Mass(Kg)'},
                         projection='natural earth',
                         hover_name=hover_text
                         )
    fig.show()
    return 0


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
