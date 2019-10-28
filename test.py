from codes_stuff.utils.misc import log_info
from codes_stuff.test_data import test_data
from codes_stuff.task import *


def main():
    log_info(' ===== start test =====')

    timers = test_8(test_data[8], (1, ))
    for timer in timers:
        log_info(timer.all())


if __name__ == '__main__':
    main()
