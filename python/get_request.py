#!/usr/bin/env python3
#https://omaharentalads.com/explore/garage-clipart/
import requests
url = ['https://omaharentalads.com/images/garage-clipart-empty-garage.png']
url.append('https://omaharentalads.com/images/garage-clipart-empty-garage-3.png')

for item in url:
    image_name = item.split('/')
    image_name = image_name[-1].replace("-","_")
    r = requests.get(url = item)

    download_link = '/var/www/relay/static/images/{}'.format(image_name)

    with open(download_link,'wb') as f:
        f.write(r.content)

#print(r.status_code)
#print(r.headers['content-type'])
#print(r.encoding)
