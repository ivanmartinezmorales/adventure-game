"""
Stack is a class written to use it when it comes to keeping track of all the movements that a player has made
"""


def Stack(object):

    def __init__(self):
        self.items = []

    def push(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
