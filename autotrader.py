import requests
import json

brands = open('carData/carBrands.json')
carModelsJsonString = brands.read()

modelsFile = open('carData/models.json', 'w')

carModels = json.loads(carModelsJsonString)

brandAndModel = {}

i = 1

for carModel in carModels:
    print(i)
    res = requests.get('https://www.autotrader.com/rest/lsc/listing?allListingType=all-cars&makeCode={}&zip=33101&location=%5Bobject%20Object%5D&newSearch=true&searchRadius=0&dma=%5Bobject%20Object%5D&channel=ATC&relevanceConfig=relevance-v2&stats=year%2Cderivedprice'.format(carModel['value']))
    models = json.loads(res.text)['filterGroups']['modelCode'][carModel['value']]['options']

    brandAndModel[carModel['value']] = models
    i += 1

# print(brandAndModel)
modelsFile.write(json.dumps(brandAndModel))

# currentPage = 0
#
# while True:
#     res = requests.get('https://www.autotrader.com/rest/lsc/listing?allListingType=all-cars&city=Cupertino&state=CA&zip=95014&location=%5Bobject%20Object%5D&dma=%5Bobject%20Object%5D&channel=ATC&relevanceConfig=relevance-v2&stats=year%2Cderivedprice&newSearch=false&searchRadius=0&firstRecord={}'.format(currentPage))
#     currentPage += 25
#     print(currentPage)

