# -*-coding:utf-8
class Node():
    def __init__(self, data=0, next=None):
        self.val = data  # 数据
        self.next = None  # 下一个地址域


class ListNode():
    def __init__(self):
        self.head = Node()  # 创建头尾节点
        self.tail = Node()
        self.head = self.tail

    # 在尾部添加节点的方式创建链表
    def append(self, data):
        p = Node(data, None)
        self.tail.next = p
        self.tail = p

    # 打印链表
    def display(self):
        p = self.head.next
        _p = []
        while p:
            _p.append(p.val)
            p = p.next
        return _p
