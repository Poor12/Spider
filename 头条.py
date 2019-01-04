import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool
def get_page(offset):
    params={
        'offset':offset,
        'format':'json',
        'keyword':'����',
        'autoload':'true',
        'count':'20',
        'cur_lab':'1'
    }
    # headers={
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
    #     'x-requested-with':'XMLHttpRequest'
    # }
    url='http://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title=item.get('title')
            images=item.get('image_list')
            if images is None:
                continue
            else:
                for image in images:
                    yield {
                        'image':image.get('url'),
                        'title':title
                    }

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response=requests.get(item.get('image'))
        if response.status_code==200:
            file_path='{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('already downloaded',file_path)
    except requests.ConnectionError:
        print('failed')
def main(offset):
    json=get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)
GROUP_START=1
GROUP_END=20
if __name__ == '__main__':
    pool=Pool()
    groups=([x*20 for x in range(GROUP_START,GROUP_END+1)])
    pool.map(main,groups)
    pool.close()
    pool.join()