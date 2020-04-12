import time as t


class MyTimer:

    def __init__(self):
        self.unit = ['年', '月', '日', '时', '分', '秒']
        self.prompt = "还未开始计时..."
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop()停止计时！"
        print("开始计时...")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("请先调用start()开始计时！")
        else:
            self.end = t.localtime()
            print("停止计时...")
            self._calc()

    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了："
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])

        # 为下一轮初始化变量
        self.begin = 0
        self.end = 0

