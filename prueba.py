import json
import requests


doc = {
        "document": {
            "id": "0",
            "txt": "Se come muy mal",
        }
    }

params = {
    'key': '22b6a55eab21eb20956914a75264f354',
    'doc': json.dumps(doc)
}
req = requests.post('https://textalytics.com/api/media/1.0/analyze', params=params, verify=False)

print req
print req.content
