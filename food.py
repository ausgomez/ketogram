import urllib, json

api_key = 'fsH5vnlqW2BI46MwQCEvrmw2nAJjb0QyOjWbIoaS'

ds = 'Standard Reference'


def search_food(query):
    url = "https://api.nal.usda.gov/ndb/search/?format=json&api_key=" + api_key + "&q=" + query + "&ds=" + ds
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    id = ''.join(data['list']['item'][0]['ndbno'])
    return id

def display_carbs(query):
    url = "https://api.nal.usda.gov/ndb/V2/reports?format=json&api_key=" + api_key + "&ndbno=" + query
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    carbs = (data['foods'][0]['food']['nutrients'][4]['value'])
    carbs = int(float(carbs))
    return str(carbs * .25)

#test = search_food("beer, coke, soda")
#test2 = display_carbs(test)
#print "search food: " + test
#print "carbs: " + test2