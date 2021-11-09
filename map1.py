import folium
import pandas

st = "Stamen Terrain"
# st = "Mapbox Bright"

data = pandas.read_csv("Volcanoes2.txt")
# print(data)
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def elevate_colorize(elevation):
    if elevation <= 0:
        return "blue"
    elif elevation < 500:
        return "lightgreen"
    elif elevation <= 1000:
        return "green"
    elif elevation <= 2000:
        return "orange"
    elif elevation <= 4000:
        return "lightred"
    elif elevation > 4000:
        return "red"

        
map = folium.Map(location=[47.5036622, 19.0338435], zoom_start=5, tiles=st)
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    if lt > 89:
        lt = 80

    iframe = folium.IFrame(html=html % (name, name, str(el)), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(elevate_colorize(el))))

map.add_child(fg)
map.save("Map_html_popup_advanced.html")
# map.save("Map1.html")










