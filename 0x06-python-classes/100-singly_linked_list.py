#!/usr/bin/python3
"""
Module creating a singly linked list
"""


class Node:
    """
    class creating a Node
    """
    def __init__(self, data, next_node=None):
        """
        method called when the instance is created
        """
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError('data must be an integer')
        self.__next_node = next_node

    @property
    def data(self):
        """
        return the data inside the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        change the data inside the node
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """
        return the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        change the next node
        """
        if isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """
    class creating a singly linked list
    """
    def __init__(self):
        """
        method called when the instance is created
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        insert a node sorted by numerical value in the linked list
        """
        cur = self.__head
        if cur is None or cur.data > value:
            self.__head = Node(value, self.__head)
            return
        while cur.next_node is not None and cur.next_node.data < value:
            cur = cur.next_node
        cur.next_node = Node(value, cur.next_node)

    def __str__(self):
        """
        function automatically called when we print the linked list
        """
        s = ''
        if self.__head:
            while self.__head.next_node:
                s += str(self.__head.data) + '\n'
                self.__head = self.__head.next_node
            s += str(self.__head.data)
        return s
