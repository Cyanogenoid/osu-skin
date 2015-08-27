import sys

import requests
import lxml.html


# source: http://www.pixiv.net/member_illust.php?mode=medium&illust_id=47640088
konachan_id = 193281
url = 'http://konachan.com/post/show/{}'.format(konachan_id)

page = requests.get(url)
tree = lxml.html.document_fromstring(page.text)
a = tree.cssselect('#highres')[0]
image_url = a.get('href')

image = requests.get(image_url)
with open(sys.argv[1], 'wb') as fd:
    fd.write(image.content)
