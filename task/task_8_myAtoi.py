class Solution(object):
    def myAtoi1(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = []
        label_strs = ['+', '-']
        num_strs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        inds = 0
        for s in str:
            if s == ' ':
                inds += 1
            else:
                break
        str = str[inds:]

        if not len(str) or str[0] not in num_strs+label_strs:
            return 0
        for s in str:
            if s in label_strs:
                label = s
                if len(num):
                    break
                num.append(label)
            if s in num_strs:
                num.append(s)
            elif s not in label_strs:
                break
        num = 0 if len(num)==0 or (len(num)==1 and num[0] not in num_strs) else int(''.join(num))
        num = min(2 ** 31 - 1, num) if num > 2 ** 31 - 1 else num
        num = max(-2 ** 31, num) if num < -2 ** 31 else num
        return num


def test_8(test_data, solution_num):
    from codes_stuff.utils.timer import timer
    from codes_stuff.utils.misc import log_data
    timer_result = []
    for num in solution_num:
        _timer = timer(num)
        for i, s in enumerate(test_data):
            i += 1
            _timer.tic(str(i))
            result = getattr(Solution(), 'myAtoi{}'.format(num))(s)
            _timer.toc(str(i))
            log_data(__name__, num, s, result)
        timer_result.append(_timer)
    return timer_result
