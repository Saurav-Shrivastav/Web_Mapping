import folium
import pandas

map = folium.Map(location=[30.3543,76.3712], zoom_start=20)
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

fg=folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon) :
    fg.add_child(folium.Marker(location=[lt, ln], popup="This is where I sit.", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")
