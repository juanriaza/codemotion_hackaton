from gevent import monkey
monkey.patch_all(thread=False)

import requests
import grequests
from flask import Flask, render_template, json, request
from werkzeug.contrib.cache import SimpleCache


cache = SimpleCache()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recommend')
def recommend():
    loc = request.args.get('loc', '')
    app.logger.debug(loc)
    cat = request.args.get('cat')
    app.logger.debug(cat)

    rv = cache.get(cat)
    if rv is None:
        rv = get_recommendation(loc, cat)
        cache.set(cat, rv, timeout=500 * 60)
    return rv


def get_recommendation(loc, cat):
    cat_map = {
        'mex': '4bf58dd8d48988d1c1941735'
    }

    params_4sq = {
        'client_id': 'VBOVRLQQQLGGZNPIGYMQ1RDTMGM1ANWM3ZQQT1IBARMYTTPM',
        'client_secret': 'WRGEDMJB4AX41TIXDCUTZVGNFAPCG4B1TM0VJNUR3XYIVPWL',
        'v': '20130815',
        'section': 'food',
        'limit': 10,
        'categoryId': cat
    }
    if loc:
        params_4sq.update({'ll': loc})
    else:
        params_4sq.update({'near': 'Madrid'})
    # req = requests.get('https://api.foursquare.com/v2/venues/categories', params=params_4sq)
    req_4sq = requests.get('https://api.foursquare.com/v2/venues/search', params=params_4sq)

    def parse_tip(tip):
        doc = {
            "document": {
                "id": "0",
                "txt": tip['text'],
            }
        }

        params_textalytics = {
            'key': '22b6a55eab21eb20956914a75264f354',
            'doc': json.dumps(doc)
        }
        req = requests.post('https://textalytics.com/api/media/1.0/analyze',
            params=params_textalytics,
            verify=False)
        tip['anal'] = req.json()
        return tip

    def parse_venue(req_venue):
        # app.logger.debug(req_venue.content)
        tips_data = req_venue.json()['response']['tips']['items']
        tips = map(parse_tip, tips_data[:4])
        # app.logger.debug(tips)
        venue['tips'] = tips
        return venue
    venues_urls = ['https://api.foursquare.com/v2/venues/%s/tips' % venue['id']
        for venue in req_4sq.json()['response']['venues'][:4]]
    venues_req = (grequests.get(u, params=params_4sq) for u in venues_urls)
    venues_response = grequests.map(rs)
    venues_4sq = map(parse_venue, venues_response)

    return json.dumps(venues_4sq)

if __name__ == "__main__":
    app.run(debug=True)
