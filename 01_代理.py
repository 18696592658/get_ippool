# _*_coding:utf-8 _*_
import requests
headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
# 从代理网站获取的免费代理
proxy = '117.88.177.247:3000'

proxies = {
    'http': 'http://' + proxy,
    # 'https': 'https://' + proxy,
    # 有的代理可能不支持https协议，可以不写https键对应的代理
}
try:
    response = requests.get('http://www.net.cn/static/customercare/yourip.asp', proxies=proxies,headers=headers)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

if __name__ == '__main__':
    pass
