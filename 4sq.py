import pprint
import requests


params = {
    'client_id': 'VBOVRLQQQLGGZNPIGYMQ1RDTMGM1ANWM3ZQQT1IBARMYTTPM',
    'client_secret': 'WRGEDMJB4AX41TIXDCUTZVGNFAPCG4B1TM0VJNUR3XYIVPWL',
    'near': 'Madrid',
    'v': '20130815',
    'section': 'food',
    'categoryId': '4bf58dd8d48988d1c1941735'
}
# req = requests.get('https://api.foursquare.com/v2/venues/categories', params=params)
req = requests.get('https://api.foursquare.com/v2/venues/search', params=params)

print req
pprint.pprint(req.json())
