# import requests
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0',
#            'Cookie': 'incap_ses_237_984766=j3GRKzrP5Tb7SC4YHv9JA/s8J2UAAAAAWYnbCCSBYtEcQ9OepJ11ew==;incap_sh_984766=AD0nZQAAAACU9KtZDAAIgPqcqQYQ/vmcqQaqa+ZyTTakR/MGjdalzVH5; U=64621147765273d0150f846bd34ae; visid_incap_984766=CJqIz8WeSEGhPtM3faITvvs8J2UAAAAAQkIPAAAAAACAWZavASaEZ5Xo3exNdKtdbtm9H+aSC3zf; nlbi_984766=FpIoeVTS/m3vE700yccqiAAAAACNlofo1x+1lIFat/FPUwb8; usprivacy=1---; OneTrustWPCCPAGoogleOptOut=false; hmn_saved_search_tooltip=yes; OptanonConsent=isIABGlobal=false&datestamp=Wed+Oct+11+2023+17%3A37%3A29+GMT-0700+(Pacific+Daylight+Time)&version=6.10.0&hosts=&consentId=97edfabc-c7b0-4fe7-8040-7d39cf0fb193&interactionCount=1&landingPath=NotLandingPage&groups=SPD_BG%3A1%2CC0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1&AwaitingReconsent=false; nlbi_984766_2147483392=XwqQI7VM0z2IHZaLyccqiAAAAAAYEr/oTyreuvl4sHcFOy1P; reese84=3:WE/OGhnRwCly/EVMj5S40g==:3S3dtY7R5MFMq5HxN19gglD11U24VdVPl20xRUmb4PjoL56CT/Ajku+tyj2qQHyVsgKleKvYLau1Y5LSuO+aTFcspMxt+FrpI7AFa/dcMzVnNUAsWfZR/EHSZIPx2qhVnISNOSMQoKFpshPocIF9daj2XIh5pmmA3HLPDAe8pQfMJloX1qCvCFx6R3WcnofJRVhcebQp6g+jQHnMdfd1ROT31drgFzOyu0OTm+vZLd17M19Ue6C2B+ne9zL0f1jxOp/qDYW+OqiIFPnXA+Iu6mXmqwEzwHHxTO+ezJ+EKgt85VbuyXmoBzNQUGFR8Lna3Y8vXUsRgVnkowFzgSPZqR+mfvQKtUXQWlOlpuMu3OrMPWF16civCTjL35br6hseVSQFdCu3R/VP8RaAsRtuBpDD4sowWPDCzTklpoxONekJpz1Uzv+qci1Pi5DIvEZgV+LZnbk33SrIyt2wZdL5pQ==:Oc63/IOX8Yndt++Z1xrJWykicp0XK6EwjrAGKbasgm4=; AWSALB=QBD/tWMFGO9gF3wZ2wuYmbxODvzUaAOr8An1wdNCNsY68cG/OWLitRqhlMeRvB5yA6unSxZTMBlo8NGx2v4HE3g4xzh95tM72HOIkY9DR7LIsWlnLw/KngryKEFE; AWSALBCORS=QBD/tWMFGO9gF3wZ2wuYmbxODvzUaAOr8An1wdNCNsY68cG/OWLitRqhlMeRvB5yA6unSxZTMBlo8NGx2v4HE3g4xzh95tM72HOIkY9DR7LIsWlnLw/KngryKEFE; XSRF-TOKEN=eyJpdiI6IkphTlpGRTBjaXFPQjUwV0xySTg1OFE9PSIsInZhbHVlIjoiV1AxcWdvWlVKU3lWcVRreC9oaE05Y3lMak01MWtQWEUxNDR5OHFNaW4yMnVqTkcrd1E5N2w0K1VpT0VyQjJyYXl5VEh1VXBGaEg4UXA2Rlh6eWdtZlFTdXB4TWhTNVhlYUI0T1dZazlORHgzK0pqTW0wSHhtSVpJNGVQMDVLc08iLCJtYWMiOiI2YmZhMjc3MDVmMDI0NjExZTdlN2RkYzY4MzY0NWYwZWU3YzMyNDExYjdlYjQ1MmM1MzRjNTc1YzM0NThlMTk0IiwidGFnIjoiIn0%3D; hemmings_session=eyJpdiI6IktNRVhhcFpVdXgvd3NxZnZxeVdFNWc9PSIsInZhbHVlIjoiY05zK0FvK0JOaWFuaWIvMVJHU2pMS1BGR2NQOXRNeDNhNW03Nkl3N1djUlpxWHZiSEt3TzhrcS9YSDNSNllycm9jcE5admhIbVJJSVk4cTdPV1BrWkRZTmU0R0xKUXQrSHdjVksvdXFVeFVrdlNEU3RlRDZSc20wcVZCY1VjUW4iLCJtYWMiOiJkYTVhYmQ0MDdhZTdmZTQ0OTY3NzI3NDc1Yjg0MzM4N2RmY2UyNmYzN2MxYjk5MDQ2MWFmZmVjZTI3MTBlMzhlIiwidGFnIjoiIn0%3D'
#            }
# url = 'https://www.hemmings.com/stories-api/search/listings?adtype=cars-for-sale&distance=50&page=1&sort_by=popular'
#
#
#
# response = requests.get(url, headers=headers)
# print(response.content)


# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import json
import pymongo

options = Options()
# options.add_argument('--headless=new')
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--enable-javascript")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

CONNECTION_STRING = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.1"

client = pymongo.MongoClient(CONNECTION_STRING)
carDb = client.get_database('CarListings')
listings = carDb.get_collection('hemmings')
proxyListings = carDb.get_collection('hemmings1')
i = 1

while True:
    driver.get(
        'https://www.hemmings.com/stories-api/search/listings?adtype=cars-for-sale&country[]=United+States&distance=3000&page={}&sort_by=recommended'.format(
            i))
    if i == 1:
        input('Press enter to continue (check captcha): ')
    try:
        response = json.loads(driver.find_element(By.TAG_NAME, 'body').text)
        message = response['message']
        print('max page limit reach')
        listings.drop()
        proxyListings.rename('hemmings')
        proxyListings = carDb.get_collection('hemmings1')
        listings = carDb.get_collection('hemmings')
        i = 1
    except KeyError as e:
        carlistings = json.loads(driver.find_element(By.TAG_NAME, 'body').text)
        for result in carlistings['results']:
            try:
                result['_id'] = result['id']
                proxyListings.insert_one(result)
            except:
                pass
        i += 1
