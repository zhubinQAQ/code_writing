import time


class timer():
    def __init__(self, name):
        self.name = 'solution '+str(name)
        self.start = {}
        self.cost = {}

    def tic(self, key=''):
        self.start[key] = time.time()

    def toc(self, key=''):
        self.cost[key] = time.time() - self.start[key]

    def all(self):
        s = ' [time  cost]-[{}]'.format(self.name)
        total = 0
        for k, v in self.cost.items():
            s += '-{test data %s: %f s}' % (k, v)
            total += v
        s += '-{total: %f s}' % (total)
        return s
