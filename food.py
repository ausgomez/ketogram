import urllib, json

api_key = 'fsH5vnlqW2BI46MwQCEvrmw2nAJjb0QyOjWbIoaS'

ds = 'Standard Reference'


def search_food(query):
    url = "https://api.nal.usda.gov/ndb/search/?format=json&api_key=" + api_key + "&q=" + query + "&ds=" + ds
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return ''.join(data["list"]['item'][0]['ndbno'])

def display_carbs(query):
    url = "https://api.nal.usda.gov/ndb/V2/reports?format=json&api_key=" + api_key + "&ndbno=" + query
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return (data["foods"][0]['food']['nutrients'][4]['vslue'])

test = search_food("beer, coke, soda")
print display_carbs(test)