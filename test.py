from leetcode.utils.misc import log_info
from leetcode.test_data import test_data
from leetcode.task import *


def main():
    log_info(' ===== start test =====')

    timers = test_2(test_data[2], (1,))
    for timer in timers:
        log_info(timer.all())


if __name__ == '__main__':
    main()
