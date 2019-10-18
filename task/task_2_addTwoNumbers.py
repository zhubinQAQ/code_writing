from leetcode.lib.lib_listnode import *


class Solution(object):
    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode()
        r = re.head
        carry = 0
        l1 = l1.head.next
        l2 = l2.head.next
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = Node(s % 10)
            r = r.next
            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
        if carry > 0:
            r.next = Node(1)
        return re


def test_2(test_data, solution_num):
    from leetcode.utils.timer import timer
    from leetcode.utils.misc import log_data
    timer_result = []
    for num in solution_num:
        _timer = timer(num)
        add = []
        for i, list_data in enumerate(test_data):
            i += 1
            l = ListNode()
            for data in list_data:
                l.append(data)
            add.append(l)
        _timer.tic(str(num))
        result = getattr(Solution(), 'addTwoNumbers{}'.format(num))(add[0], add[1])
        _timer.toc(str(num))
        log_data(__name__, num, (test_data), result.display())
        timer_result.append(_timer)
    return timer_result

"""
Time complexity: O(max(m,n))
Space complexity: O(max(m,n) + 1)
"""