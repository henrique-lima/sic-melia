import requests
import json

def get_artists(text):
    url= "http://mel.mtg.upf.edu/annotate"
    r = requests.post(url, data={'text':text})
    if r.status_code == 200:
        results = r.json()
        res = []
        for r in results['result']:
           res.append(r['label'])
        return res
    return text
