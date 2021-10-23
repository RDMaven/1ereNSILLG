import folium

#Les coordonnées trouvée grâce au magnifique programme 'Ex_parachute_4.py'.
geoloc = """34°11'58"N 118°10'31"W"""
char = ["°", "'", '"']

geoloc_list = geoloc.split()

geoloc_n = geoloc_list[0]
geoloc_w = geoloc_list[1]


charPrev_n = 0
charPrev_w = 0
n_val = []
w_val = []

for i in char:
    there_is_char_in_n = geoloc_n.find(i) != -1
    there_is_char_in_w = geoloc_w.find(i) != -1

    if there_is_char_in_n:
        charCurrent_n = geoloc_n.find(i)
        n_val.append(geoloc_n[charPrev_n:charCurrent_n])
        charPrev_n = charCurrent_n
        geoloc_n = geoloc_n.replace(i, "")

   
    if there_is_char_in_w:
        charCurrent_w = geoloc_w.find(i)
        w_val.append(geoloc_w[charPrev_w:charCurrent_w])
        charPrev_w = charCurrent_w
        geoloc_w = geoloc_w.replace(i, "")

print(n_val)
print(w_val)

lat = float(n_val[0]) + (float(n_val[1])/60) + (float(n_val[2])/3600) 
long = -1*(float(w_val[0]) + (float(w_val[1])/60) + (float(w_val[2])/3600))

print(lat, long)




import webbrowser


class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start

    def showMap(self):
        #Create the map
        my_map = folium.Map(location = self.center, zoom_start = self.zoom_start)

        #Display the map
        my_map.save("map.html")
        webbrowser.open("map.html")

coords = [lat,long]
map = Map(center = coords, zoom_start = 17)
map.showMap()
