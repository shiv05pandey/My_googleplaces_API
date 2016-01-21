import urllib
from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
geolocator = GoogleV3()

addr = raw_input('\nAddress : ')
geolocator = Nominatim()
location = geolocator.geocode(addr)

#location = geolocator.geocode("BTM Layout, Bengaluru, Karnataka, India")12.9151772 77.6102821

address, (latitude, longitude) = geolocator.geocode(addr)
print latitude, longitude
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%.7f,%.7f&radius=500&types=food&name=Biryani&key=AIzaSyDD0dXfpuFSbpGbcFr28w7-IeElAYaBOok'%(latitude,longitude)
resp4 = urllib.urlopen(url)
a4 =resp4.read() 
print a4

