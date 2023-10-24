import sys
import HttpRequest as ht
import Meteor as mt
import plotly.express as px


def extract_meteor_attributes(meteors):
    longitude_, latitude_, mass_ = [],[],[]
    for a_meteor in meteors:
        longitude_.append(a_meteor.longitude)
        latitude_.append(a_meteor.latitude)
        mass_.append(float(a_meteor.mass)/1000)

    return longitude_, latitude_, mass_

# =====================================

def extract_meteors_to_list(meteors_json, meteors):
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

# =====================================

def extract_hover_text(meteors):
    hover_text = []
    for a_meteor in meteors:
        hover_text.append(f'{a_meteor.year} Name: {a_meteor.name}')

    return hover_text

# =====================================


def main() -> int:
    """Echo the input arguments to standard output"""
    url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
    my_request = ht.myHttpRequest(url)

    my_request.get_http_request()
    meteors_json = my_request.get_json()

    meteors = []
    extract_meteors_to_list(meteors_json, meteors)

    # Show in geo location map
    longitudes, latitudes, masses = extract_meteor_attributes(meteors)

    map_title = 'Meteoroid impacts on Earth'
    hover_text = extract_hover_text(meteors)

    fig = px.scatter_geo(lat=latitudes, lon=longitudes, title=map_title,
                         color=masses,
                         color_continuous_scale='reds',
                         labels={'color': 'Mass'},
                         projection='natural earth',
                         hover_name=hover_text
                         )
    fig.show()
    return 0


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
