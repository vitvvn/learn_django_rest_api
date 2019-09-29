import json
import requests

ENDPOINT = 'http://localhost:8000/api/status/all/'


def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        pass
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.status_code)

    print(r.text)
    print(r.headers)

    return r


# do(data={'id': 500})
#
do(method='delete', data={'id': 500})

# do(method='put', data={'id': 11, 'content': 'somme cool new content', 'user': 1})

# do(method='post', data={'content': 'somme cool new content', 'user': 1})