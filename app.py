import requests
from flask import Flask, render_template, json


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recommend')
def recommend():
    loc = request.args.get('loc', None)
    app.logger.debug(loc)
    cat = request.args.get('cat', 'mex')
    app.logger.debug(cat)

    cat_map = {
        'mex': '4bf58dd8d48988d1c1941735'
    }

    params_4sq = {
        'client_id': 'VBOVRLQQQLGGZNPIGYMQ1RDTMGM1ANWM3ZQQT1IBARMYTTPM',
        'client_secret': 'WRGEDMJB4AX41TIXDCUTZVGNFAPCG4B1TM0VJNUR3XYIVPWL',
        'v': '20130815',
        'section': 'food',
        'limit': 10,
        'categoryId': cat_map[cat]
    }
    if loc:
        params_4sq.update({'loc': loc})
    else:
        params_4sq.update({'near': 'Madrid'})
    # req = requests.get('https://api.foursquare.com/v2/venues/categories', params=params_4sq)
    req_4sq = requests.get('https://api.foursquare.com/v2/venues/search', params=params_4sq)

    '''
    doc = {
        "document": {
            "id": "0",
            "txt": "Se come muy mal",
        }
    }

    params_textalytics = {
        'key': '22b6a55eab21eb20956914a75264f354',
        'doc': json.dumps(doc)
    }
    req = requests.post('https://textalytics.com/api/media/1.0/analyze',
        params=params_textalytics,
        verify=False)
    '''

    return req_4sq.content

if __name__ == "__main__":
    app.run(debug=True)
