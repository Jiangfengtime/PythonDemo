import time as t


class MyTimer:
    def __init__(self):
        self.unit = ['年', '月', '日', '时', '分', '秒']
        self.lasted = []
        self.begin = 0
        self.end = []
        self.prompt = '还未开始及时'

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def start(self):
        self.begin = t.localtime()
        self.prompt = '提示：执行stop()停止计时'
        print("开始计时...")

    def stop(self):
        if not self.begin:
            self.prompt = '请先开始计时'
        else:
            self.end = t.localtime()
            print("停止计时...")
            self._calc()

    def _calc(self):

        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]
        self.lasted = []
        self.begin = 0
        self.end = 0


