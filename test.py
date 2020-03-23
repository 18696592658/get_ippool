import json
import queue
import threading
import requests
from redis_client import RedisClient
from utils.utils import get_response

VALID_CODE = [200]
URL = 'http://www.baidu.com/'

class Test():
    def __init__(self):
        self.redis = RedisClient()



    def test_single(self,proxy):
        ip= json.loads(proxy)
        ip_type = ip['type']
        ip = ip['ip']
        try:
            response = get_response(URL,ip)
            if response.status_code in VALID_CODE:
                print(ip,ip_type,'正常')
                self.redis.max(proxy)
            else:
                print(ip, ip_type, '-1')
                self.redis.decrease(proxy)

        except Exception as e:
            print(e)
            print(ip, ip_type, '-1')
            self.redis.decrease(proxy)
    def run(self):
        proxies = self.redis.all()
        q = queue.Queue(10)
        for proxy in proxies:
            if not q.full():
                q.put(proxy)
            if not q.empty():
                proxy = q.get()
                t = threading.Thread(target=self.test_single,args=(proxy,))
                t.start()
