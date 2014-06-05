try:
    # Python 2
    from StringIO import StringIO as BytesIO
except ImportError:
    # Python 3
    from io import BytesIO
import mimetypes

import simplejson as json
import requests
from flask import Flask, request, make_response


app = Flask(__name__)


# URLs for getting share counts
Twitter_URL = "http://urls.api.twitter.com/1/urls/count.json?url=%s"
Facebook_URL = "https://api.facebook.com/method/links.getStats?urls=%s&format=json"

# subject, status, color, format
SHIELD_URL = "http://img.shields.io/badge/%s-%s-%s.%s"


class TwitterHandler():
    '''Get the twitter json data for the url, and process.'''
    shield_subject = 'Tweet'
    shield_color = '55ACEE'

    def get(self, url, format):
        url = Twitter_URL % url
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return self.write_shield('error', 'error', 'red')
        else:
            data = json.loads(response.content)
            return write_shield(self.shield_subject, data['count'], 
                self.shield_color, format)

class FacebookHandler():
    '''Get the facebook json data for the url, and process.'''
    shield_subject = 'Like'
    shield_color = '3b5998'

    def get(self, url, format, fb_type):
        url = Facebook_URL % url
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return self.write_shield('error', 'error', 'red')
        else:
            data = json.loads(response.content)[0]
            if fb_type == 'share':
                return write_shield('Share', data['share_count'], 
                    self.shield_color, format)
            else:
                return write_shield(self.shield_subject, data['like_count'], 
                    self.shield_color, format)


def write_shield(subject, count, color, format):
    '''Obtain and write the shield to the response.'''
    shield_url = SHIELD_URL % (
        subject,
        count,
        color,
        format
    )
    shield_response = requests.get(shield_url)
    img = BytesIO(shield_response.content)
    img.seek(0)
    return img


generators = {
    'twitter': TwitterHandler,
    'facebook': FacebookHandler
}

@app.route('/facebook/<fb_type>/<format>/<path:url>', methods=['GET'])
def fb_shield(url, format='png', fb_type='like'):
    gen_class = FacebookHandler()
    img = gen_class.get(url, format, fb_type)
    resp = make_response(img.read())
    resp.content_type = format
    return resp

@app.route('/<generator>/<format>/<path:url>', methods=['GET'])
def shield(generator, url, format='png', fb_type='like'):
    gen_class = generators[generator]()
    img = gen_class.get(url, format)
    resp = make_response(img.read())
    resp.content_type = format
    return resp


if __name__ == "__main__":
    if '.svg' not in mimetypes.types_map:
        mimetypes.add_type("image/svg+xml", ".svg")
    app.run(debug=True)
