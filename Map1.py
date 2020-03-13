import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[35.8543,-121.3712], zoom_start=6)

fg=folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev) :
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + " m", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")
