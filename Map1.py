import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")     #Reading the csv file
lat = list(data["LAT"])                     #stored the data in the "LAT" column of the data frame to a list
lon = list(data["LON"])                     #stored the data in the "LON" column of the data frame to a list
elev = list(data["ELEV"])                   #stored the data in the "ELEV" column of the data frame to a list

def color_producer(elevation):              #We produce the color of the marker depending on the height of the volcano using this function
    if elevation < 1000 :
        return 'green'
    elif 1000 <= elevation < 2000 :
        return 'orange'
    else :
        return 'red'

map = folium.Map(location=[35.8543,-121.3712], zoom_start=6)        #creates an object of the Map class and opens at the given location

fg=folium.FeatureGroup(name="My Map")       #making a FeatureGroup class object which will be added as a child to the base Map.

for lt, ln, el in zip(lat, lon, elev) :
    fg.add_child(folium.CircleMarker(location=[lt, ln],             #The CircleMarker class of the folium library is used to mark the location of the volcanoes.
                                     popup=str(el) + " m",
                                     radius = 6,
                                     fill = True,           #it is false by default
                                     fill_color = color_producer(el),
                                     color = 'grey',
                                     fill_opacity = 0.7))

fg.add_child(folium.GeoJson(data = (open('world.json', 'r', encoding = 'utf-8-'))))     #creates a GeoJson object for plotting into a map.
# In this case we mark the borders of different countries by uusig the data in the Json file.
#Adds a GeoJson polygon layer onto the Map.

map.add_child(fg)                 #Adds the feature group layer to the Map.

map.save("Map1.html")           #Saves the Map
