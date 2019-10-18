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
        right = left = 0
        dp = [[[]] * len(s)] * len(s)
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i - 1):
                dp[i][j] = (s[i] == s[j]) and (i == j + 1 or dp[i - 1][j + 1])
                if dp[i][j] and (i - j) > (right - left):
                    right = i
                    left = j
        return s[left:right + 1] if right - left >= 1 else None

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        return 0


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
Time complexity: O(log(min(m,n)))
Space complexity: O(1)
"""
