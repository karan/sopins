try:
    # Python 2
    from StringIO import StringIO as BytesIO
except ImportError:
    # Python 3
    from io import BytesIO
import mimetypes

import simplejson as json

import requests
from flask import Flask, request, make_response, redirect


app = Flask(__name__)


# URLs for getting share counts
Twitter_URL = "http://cdn.api.twitter.com/1/urls/count.json?url=%s"
Facebook_URL = "https://api.facebook.com/method/links.getStats?urls=%s&format=json"
LinkedIn_URL = "https://www.linkedin.com/countserv/count/share?url=%s&format=json"

# subject, status, color, format
SHIELD_URL = "http://img.shields.io/badge/%s-%s-%s.%s"


class TwitterHandler(object):
    '''Get the twitter json data for the url, and process.'''
    shield_subject = 'Tweet'
    shield_color = '55ACEE'

    def get(self, url, format, endpoint=SHIELD_URL):
        url = Twitter_URL % url
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return write_shield('error', 'error', 'red')
        else:
            data = json.loads(response.content)
            return write_shield(self.shield_subject, data['count'], 
                self.shield_color, format, endpoint=endpoint)

class LinkedInHandler(object):
    shield_subject = 'LinkedIn Share'
    shield_color = '489DC9'

    def get(self, url, format, endpoint=SHIELD_URL):
        url = LinkedIn_URL % url 
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return write_shield('error', 'error', 'red')
        else:
            data = json.loads(response.content)
            return write_shield(self.shield_subject, data['count'], 
                self.shield_color, format, endpoint=endpoint)

class FacebookHandler(object):
    '''Get the facebook json data for the url, and process.'''
    shield_subject = 'Like'
    shield_color = '3b5998'

    def get(self, url, format, fb_type, endpoint=SHIELD_URL):
        url = Facebook_URL % url
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return write_shield('error', 'error', 'red')
        else:
            data = json.loads(response.content)[0]
            if fb_type == 'share':
                return write_shield('Share', data['share_count'], 
                    self.shield_color, format)
            else:
                return write_shield(self.shield_subject, data['like_count'], 
                    self.shield_color, format, endpoint=endpoint)

def write_shield(subject, count, color, format, endpoint=SHIELD_URL):
    '''Obtain and write the shield to the response.'''
    shield_url = endpoint % (
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
    'facebook': FacebookHandler,
    'linkedin': LinkedInHandler
}

@app.route('/', methods=['GET'])
def index():
    return redirect("https://github.com/karan/sopins", code=301)
    
@app.route('/facebook/<fb_type>/<path:url>/pin.<format>', methods=['GET'])
def fb_shield(url, format='png', fb_type='like'):
    gen_class = FacebookHandler()
    if not request.args.get('style') is None:
        styledEndpoint = '{0}?style={1}'.format(SHIELD_URL, request.args.get('style'))
        img = gen_class.get(url, format, fb_type, endpoint=styledEndpoint)
    else:
        img = gen_class.get(url, format, fb_type)
    
    resp = make_response(img.read())
    resp.headers['Content-Type'] = mimetypes.types_map[".{0}".format(format)]
    return resp

@app.route('/<generator>/<path:url>/pin.<format>', methods=['GET'])
def shield(generator, url, format='png', fb_type='like'):
    gen_class = generators[generator]()
    if not request.args.get('style') is None:
        styledEndpoint = '{0}?style={1}'.format(SHIELD_URL, request.args.get('style'))
        img = gen_class.get(url, format, endpoint=styledEndpoint)
    else:
        img = gen_class.get(url, format)
    
    resp = make_response(img.read())
    resp.headers['Content-Type'] = mimetypes.types_map[".{0}".format(format)]
    return resp
    # return Response(img.read(),  mimetype=mimetypes.types_map[".{0}".format(format)])


if __name__ == "__main__":
    if '.svg' not in mimetypes.types_map:
        mimetypes.add_type("image/svg+xml", ".svg")
    app.run(debug=True)
