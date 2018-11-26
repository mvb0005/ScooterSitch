import json
import folium

myLoc = [39.755580, -104.992100]

m = folium.Map(location=myLoc, zoom_start=20)

file = open('bird.json', 'r')
birdInfo = json.loads(file.read())

for scooter in birdInfo['birds']:
    folium.Marker([scooter['location']['latitude'],
                   scooter['location']['longitude']],
                  popup=scooter['id'],
                  icon=folium.features.CustomIcon('bird.png', icon_size=(40, 40))).add_to(m)

file = open('spin.json', 'r')
spinInfo = json.loads(file.read())

for scooter in spinInfo['vehicles']:
    folium.Marker([scooter['lat'],
                   scooter['lng']],
                  popup=scooter['last4'],
                  icon=folium.features.CustomIcon('spin.png', icon_size=(40, 40))).add_to(m)

file = open('lyft.json', 'r')
lyftInfo = json.loads(file.read())

for scooter in lyftInfo['rideables']:
    folium.Marker([scooter['location']['lat'],
                   scooter['location']['lng']],
                  popup=scooter['rideable_id'],
                  icon=folium.features.CustomIcon('lyft.png', icon_size=(40, 40))).add_to(m)

file = open('lime.json', 'r')
limeInfo = json.loads(file.read())

for scooter in limeInfo['data']['attributes']['bikes']:
    folium.Marker([scooter['attributes']['latitude'],
                   scooter['attributes']['longitude']],
                  popup=scooter['id'],
                  icon=folium.features.CustomIcon('lime.png', icon_size=(40, 40))).add_to(m)


file = open('razor.json', 'r')
razorInfo = json.loads(file.read())

for scooter in razorInfo:
    folium.Marker([scooter['location']['latitude'],
                   scooter['location']['longitude']],
                  popup=scooter['name'],
                  icon=folium.features.CustomIcon('razor.png', icon_size=(40, 40))).add_to(m)

m.save('test.html')
