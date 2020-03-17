# _*_coding:utf-8 _*_
from lxml import etree
import requests

headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
def get_page(url):
    content = requests.get(url,headers=headers).content
    html = etree.HTML(content.decode())
    return html

def get_response(url,ip=None):
    if ip:
        proxies = {
            'http': 'http://' + ip,
        }
        response = requests.get(url,headers=headers,proxies=proxies)
    else:
        response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    pass
