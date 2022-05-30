import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
#enter api key for Google Places here if you have it.
#api_key = ''
#https://developers.google.com/maps/documentation/geocoding/intro


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("please enter URL for XML extraction")
if len(url) < 1: 
    url = 'https://py4e-data.dr-chuck.net/comments_1539140.xml'
    
uh = urllib.request.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)

list = tree.findall('comments/comment/count')
print(list)
