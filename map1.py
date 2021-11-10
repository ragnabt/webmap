import folium
import pandas

st = 'Stamen Terrain'
countries_data = 'world.json'
# st = 'Mapbox Bright'

data = pandas.read_csv('Volcanoes2.txt')
# print(data)
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])


html = '''
Volcano name:<br>
<a href='https://www.google.com/search?q=%%22%s%%22' target='_blank'>%s</a><br>
Height: %s m
'''

def elevate_colorize(elevation):
    if elevation <= 0:
        return 'blue'
    elif elevation < 500:
        return 'lightgreen'
    elif elevation <= 1000:
        return 'green'
    elif elevation <= 2000:
        return 'orange'
    elif elevation <= 4000:
        return 'lightred'
    elif elevation > 4000:
        return 'red'

        
map = folium.Map(location=[47.5036622, 19.0338435], zoom_start=5, tiles=st)

fgV = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el, name in zip(lat, lon, elev, name):
    if lt > 89:
        lt = 80

    iframe = folium.IFrame(html=html % (name, name, str(el)), width=150, height=75)
    fgV.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe),
     icon=folium.Icon(elevate_colorize(el))))

fgP = folium.FeatureGroup(name='Population')

fgP.add_child(folium.GeoJson(data=open(countries_data,'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgV)
map.add_child(fgP)
map.add_child(folium.LayerControl())



map.save('Map_html_popup_advanced.html')
# map.save('Map1.html')










