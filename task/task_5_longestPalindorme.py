"""
1。动态规划法

2。马拉车算法
"""


class Solution(object):
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2: return s
        right = 0
        left = 0
        dp = [[False] * len(s)] * len(s)
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                dp[i][j] = ((s[i] == s[j]) and (i == j + 1)) or ((s[i] == s[j]) and dp[i - 1][j + 1])
                if dp[i][j] and (i - j) > (right - left):
                    right = i
                    left = j
        return s[left:right + 1] if right - left >= 1 else s[0]

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2: return s
        _s = '#'.join(list(s))
        r = [0] * len(_s)
        center = 0
        maxRight = 0
        maxstr = ''
        for j in range(1, len(_s) - 1):
            if j < maxRight:
                r[j] = min(maxRight - j, r[2 * center - j])
            if j + r[j] + 1 <= len(_s) - 1:
                while _s[j - r[j] - 1] == _s[j + r[j] + 1]:
                    r[j] += 1
                    if j + r[j] + 1 > len(_s) - 1:
                        break
            if j + r[j] > maxRight:
                maxRight = j + r[j]
                center = j
            if len(_s[j - r[j]:j + r[j] + 1].replace('#', '')) > len(maxstr):
                maxstr = _s[j - r[j]:j + r[j] + 1]
                maxstr = maxstr.replace('#', '')
        return maxstr if len(maxstr) > 1 else s[0]


def test_5(test_data, solution_num):
    from leetcode.utils.timer import timer
    from leetcode.utils.misc import log_data
    timer_result = []
    for num in solution_num:
        _timer = timer(num)
        for i, s in enumerate(test_data):
            i += 1
            _timer.tic(str(i))
            result = getattr(Solution(), 'longestPalindrome{}'.format(num))(s)
            _timer.toc(str(i))
            log_data(__name__, num, s, result)
        timer_result.append(_timer)
    return timer_result


"""
Time complexity: 
Space complexity: 
Time complexity: 
Space complexity: 
"""
