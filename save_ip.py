POOL_UPPER_THRESHOLD = 10000
from redis_client import RedisClient
from crawler import Crawler

class SaveIp():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        """判断是否达到了代理池限制"""
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print(' 获取器开始执行 ')
        if not self.is_over_threshold():
                proxies = self.crawler.run()
                for proxy in proxies:
                    print(proxy,'存入')
                    self.redis.add(proxy)


if __name__ == '__main__':
    pass
