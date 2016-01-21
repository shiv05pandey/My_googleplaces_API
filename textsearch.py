import urllib
import xml.etree.ElementTree as ET

#                     Text Search Requests
url1= 'https://maps.googleapis.com/maps/api/place/textsearch/xml?query=restaurants+in+bangalore&key=AIzaSyDD0dXfpuFSbpGbcFr28w7-IeElAYaBOok'
resp1 = urllib.urlopen(url1)
a1 =resp1.read()
print a1
