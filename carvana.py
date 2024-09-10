import pymongo
import requests
from sys import getsizeof
import json

pageNum = 1
prevReqId = ""
alternate = True

CONNECTION_STRING = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.1"

client = pymongo.MongoClient(CONNECTION_STRING)
carDb = client.get_database('CarListings')
listings = carDb.get_collection('carvana')
proxyListings = carDb.get_collection('carvana1')


def getJsonBody(pagenumber=1):
    jsonBody = {
        "analyticsData": {
            "browser": "Chrome",
            "clientId": "srp_ui",
            "deviceName": "Chrome - OS X",
            "isFirstActiveSearchSession": False,
            "isMobileDevice": False,
            "previousSearchRequestId": prevReqId,
            "referrer": "https://www.carvana.com/"
        },
        "browserCookieId": "d435e62a-ccff-ed7a-2eda-4b728f02666f",
        "filters": {},
        "pagination": {
            "page": pagenumber,
            "pageSize": 100
        },
        "requestedFeatures": [
        ],
        "sortBy": "MostPopular",
        "zip5": "30334"
    }
    return jsonBody


while True:
    jsonBody = getJsonBody(pageNum)
    headers = {
        'Content-Length': str(getsizeof(jsonBody)),
        'Content-Type': 'application/json',
    }
    res = requests.post('https://apik.carvana.io/merch/search/api/v2/search', headers=headers, json=jsonBody)
    if res.status_code != 200:
        break
    else:
        dJson = json.loads(res.content)
        prevReqId = dJson['searchRequestId']
        carListingArrays = dJson['inventory']['vehicles']
        print(pageNum)
        repeated = 0
        for carListing in carListingArrays:
            carListing['_id'] = carListing['vehicleId']
            try:
                proxyListings.insert_one(carListing)
            except Exception as e:
                repeated += 1
                proxyListings.delete_one({'_id': carListing['vehicleId']})
                carListing['_id'] = carListing['vehicleId']
                proxyListings.insert_one(carListing)
        if repeated/100 == 1:
            print('restarted')
            listings.drop()
            proxyListings.rename('carvana')
            proxyListings = carDb.get_collection('carvana1')
            listings = carDb.get_collection('carvana')
            pageNum = 0

        pageNum += 1
        # print(str(pageNum) + " " + str(dJson['inventory']['vehicles'][0]))
        pass
# print(res.content)


