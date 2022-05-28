import xml.etree.ElementTree as ET
#XML parser ElementTree
# extracting data from XML is just as easy as from JSON
# we dig into the datastructures to find what we want.

data = '''
<person>
  <name>Brian</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data) # reads the XML string and returns back a tree object
print('Name:', tree.find('name').text) # looks for a tag named name .text grabs the text attribute or value
print('Attr:', tree.find('email').get('hide'))
