from utils.utils import get_page
import json


class Crawler():
    def run(self):
        ip_list = []
        for i in self.xici_proxy():
            ip_list.append(i)
        for i in self.kuaiproxy():
            ip_list.append(i)
        return ip_list

    # 从西祠代理获取ip
    def xici_proxy(self):
        urls = ['https://www.xicidaili.com/nn/{}'.format(i) for i in (1, 2)]
        for url in urls:
            html = get_page(url)
            res = html.xpath('//tr[position()>1]')
            for r in res:
                ip = r.xpath('./td[2]/text()')[0]
                port = r.xpath('./td[3]/text()')[0]
                ip_type = r.xpath('./td[5]/text()')[0]
                dic = {
                    'ip': ':'.join([ip, port]),
                    'type': ip_type
                }
                dic = json.dumps(dic)
                print(dic)
                yield dic

    # 从快代理获取ip
    def kuaiproxy(self):
        urls = ['https://www.kuaidaili.com/free/inha/{}/'.format(i) for i in range(1, 5)]
        for url in urls:
            html = get_page(url)
            res = html.xpath('//tbody/tr')
            for r in res:
                ip = r.xpath('./td[1]/text()')[0]
                port = r.xpath('./td[2]/text()')[0]
                ip_type = r.xpath('./td[3]/text()')[0]
                dic = {
                    'ip': ':'.join([ip, port]),
                    'type': ip_type
                }
                dic = json.dumps(dic)
                print(dic)
                yield dic

if __name__ == '__main__':
    crawer = Crawler()
    crawer.run()
