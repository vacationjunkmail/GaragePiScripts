#!/usr/bin/env python3

import requests
url = 'https://omaharentalads.com/images/garage-clipart-empty-garage.png'
image_name = url.split('/')
print(image_name[-1])
r = requests.get(url = url)

download_link = '/home/pi/Downloads/{}'.format(image_name[-1])

with open(download_link,'wb') as f:
    f.write(r.content)

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
