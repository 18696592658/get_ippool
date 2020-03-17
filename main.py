TESTER_CYCLE = 20
GETTER_CYCLE = 20
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

import time
from multiprocessing import Process
from save_ip import SaveIp
from test import Test
from flask_web import app

class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """定时测试代理"""
        test = Test()
        while True:
            print(' 测试器开始运行 ')
            test.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """定时获取代理"""
        save = SaveIp()
        while True:
            print(' 开始抓取代理 ')
            save.run()
            time.sleep(cycle)

    def schedule_api(self):
        """开启 API"""
        app.run('127.0.0.1', 5000)

    def run(self):
        print(' 代理池开始运行 ')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()

sch = Scheduler()
sch.run()
