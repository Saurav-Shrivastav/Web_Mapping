import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000 :
        return 'green'
    elif 1000 <= elevation < 2000 :
        return 'orange'
    else :
        return 'red'

map = folium.Map(location=[35.8543,-121.3712], zoom_start=6)

fg=folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev) :
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + " m", icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)

map.save("Map1.html")
