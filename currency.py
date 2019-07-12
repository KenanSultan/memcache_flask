from flask import Flask, jsonify
import json, api
from werkzeug.contrib.cache import MemcachedCache
# from time import time

app = Flask(__name__)  

cache = MemcachedCache(['127.0.0.1:11311'])

@app.route('/currency')
def currency():
    mydata = cache.get('currencies')

    if mydata:
        return jsonify(mydata)

    content = api.getResp()
    if content:
        liste = [{
            'key': val.attrib['Code'],
            'value': val[2].text,
            # 'time': time() 
        } for val in content[1]]

        cache.set('currencies', liste, timeout=10)
        return jsonify(liste)
    else:
        return 'Bad Request'

@app.route('/currency/<string:id>')
def oneCurrency(id):
    mydata = cache.get(id)
    if mydata:
        return jsonify(mydata)

    content = api.getResp()
    if content:
        for val in content[1]:
            if val.attrib['Code'] == id.upper():
                dictionary = {
                    'key': id,
                    'value': val[2].text,
                    # 'time': time() 
                }
                cache.set(id, dictionary, timeout=10)
                return jsonify(dictionary)

        return 'Currency not found'
    else:
        return 'Bad request'

if __name__ == "__main__":
    app.run(debug=True)