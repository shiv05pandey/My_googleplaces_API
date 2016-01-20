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
url = 'https://maps.googleapis.com/maps/api/place/radarsearch/json?location=%.7f,%.7f&radius=500&types=food|cafe&keyword=vegetarian&key=API_KEY'%(latitude,longitude)
resp = urllib.urlopen(url)
a =resp.read() 
print a
