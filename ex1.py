# Code Referenced from ChatGPT
import random
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

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
        return node

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


def generate_random_tasks():
    tasks = []
    integers = list(range(1, 1001))

    for _ in range(1000):
        random.shuffle(integers)
        tasks.append(integers.copy())

    return tasks

def evaluate_tasks(tree, tasks):
    avg_performance = []
    largest_balance = []

    for task in tasks:
        start_time = time.time()
        for integer in task:
            tree.search(integer)
        end_time = time.time()
        avg_performance.append((end_time - start_time) / len(task))

        balance = tree.measure_balance()
        if balance:
            largest_balance.append(max(balance.values()))
        else:
            largest_balance.append(0)

    return avg_performance, largest_balance

def plot_scatter(avg_performance, largest_balance):
    plt.scatter(largest_balance, avg_performance, alpha=0.5)
    plt.title('Scatterplot of Balance vs Search Time')
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time')

    # Set the limits of the x-axis to be more spread out with a higher multiplier
    plt.xlim(0, max(largest_balance) * 1.5)  # Adjust the multiplier as needed

    plt.show()

if __name__ == "__main__":
    tasks = generate_random_tasks()
    tree = BST()

    avg_performance, largest_balance = evaluate_tasks(tree, tasks)
    plot_scatter(avg_performance, largest_balance)
