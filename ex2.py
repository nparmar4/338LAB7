import random
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.balance = 0

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.balance = self._height(node.right) - self._height(node.left)

        pivot = self.find_pivot(node)
        if pivot:
            if pivot.balance == 0:
                print("Case #1: Pivot not detected")
            elif pivot.balance * (key - pivot.key) > 0:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
                pivot.balance += 1 if key < pivot.key else -1

        return node

    def find_pivot(self, node):
        parent = None
        current = node

        while current:
            balance = self._height(current.right) - self._height(current.left)
            if balance != 0:
                return current
            parent = current
            current = current.right if current.key < node.key else current.left

        return parent

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def measure_balance(self):
        return self._measure_balance(self.root)

    def _measure_balance(self, node):
        if node is None:
            return {}

        left_height = self._height(node.left)
        right_height = self._height(node.right)
        balance = abs(left_height - right_height)

        return {
            node.key: balance,
            **self._measure_balance(node.left),
            **self._measure_balance(node.right)
        }

if __name__ == "__main__":
    # Test Cases
    bst = BST()
    print("Test Case 1:")
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(20)
    print("\nTest Case 2:")
    bst.insert(25)
    bst.insert(30)
    bst.insert(3)
    bst.insert(2)
    print("\nTest Case 3:")
    print("Case 3 not supported")

#code was referenced using AI