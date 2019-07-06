import urllib.request, json
from .models import Quotes

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTES_URL']



def get_quote():
    '''
    Function that gets the json response to our url request
    '''

    with urllib.request.urlopen(base_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = None

        if get_quote_response:
            id=get_quote_response.get('id')
            author=get_quote_response.get("author")
            quote=get_quote_response.get("quote")
            permalink=get_quote_response.get("permalink")
            quote_results=Quote(id,author,quote,permalink)
            
            
        return quote_results






