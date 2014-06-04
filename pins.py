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


Twitter_URL = "http://urls.api.twitter.com/1/urls/count.json?url=%s"
SHIELD_URL = "http://img.shields.io/badge/%s-%s-%s.%s"
# SHIELD_URL = "http://localhost:9000/badge/%s-%s-%s.%s"  # pypip.in uses a local version of img.shields.io


def format_number(singular, number):
    value = singular % {'value': number}
    # Get rid of the .0 but keep the other decimals
    return value.replace('.0', '')


intword_converters = (
    (3, lambda number: format_number('%(value).1fK', number)),
    (6, lambda number: format_number('%(value).1fM', number)),
    (9, lambda number: format_number('%(value).1fB', number)),
)


class TwitterHandler(object):
    '''Get the twitter json data for the url, and process.'''
    shield_subject = None
    request = None
    format = 'png'

    def get(self, url, format, *args, **kwargs):
        self.format = format
        url = Twitter_URL % url
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return self.write_shield('error', 'red')
        else:
            data = json.loads(response.content)
            return self.write_shield(data['count'])

    def write_shield(self, status, colour='brightgreen'):
        '''Obtain and write the shield to the response.'''
        shield_url = SHIELD_URL % (
            self.shield_subject,
            status,
            colour,
            self.format,
        )
        shield_response = requests.get(shield_url)
        img = BytesIO(shield_response.content)
        img.seek(0)
        return img


generators = {
    'twitter': TwitterHandler
}

@app.route('/')
def hello():
    return "Hello world"


@app.route('/url=<path:url>', methods=['GET'])
def shield(url, generator="twitter", extension="png"):
    gen_class = generators[generator]()
    img = gen_class.get(url, extension)
    resp = make_response(img.read())
    resp.content_type = "image/jpeg"
    return resp


if __name__ == "__main__":
    if '.svg' not in mimetypes.types_map:
        mimetypes.add_type("image/svg+xml", ".svg")
    app.run(debug=True)
