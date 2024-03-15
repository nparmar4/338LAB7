import random
import time
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root is not None
        if key < root.key:
            return self._search_recursive(root.left, key)
        else:
            return self._search_recursive(root.right, key)

    def measure_balance(self, root):
        if root is None:
            return 0
        return abs(self._height(root.left) - self._height(root.right))

    def _height(self, node):
        if node is None:
            return 0
        return max(self._height(node.left), self._height(node.right)) + 1

def generate_random_search_tasks():
    search_tasks = []
    integers = list(range(1, 1001))
    for _ in range(1000):
        random.shuffle(integers)
        search_tasks.append(integers.copy())
    return search_tasks

def measure_performance_and_balance(bst, search_tasks):
    performance = []
    max_balance_values = []
    for task in search_tasks:
        start_time = time.time()
        for integer in task:
            bst.search(integer)
        end_time = time.time()
        search_time = end_time - start_time
        performance.append(search_time)

        max_balance = measure_max_balance(bst.root)
        max_balance_values.append(max_balance)
        
    return performance, max_balance_values

def measure_max_balance(node):
    if node is None:
        return 0
    return max(node.measure_balance(node), measure_max_balance(node.left), measure_max_balance(node.right))

def plot_scatterplot(absolute_balance, search_time):
    plt.scatter(absolute_balance, search_time, alpha=0.5)
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time (s)')
    plt.title('Scatterplot of Absolute Balance vs Search Time')
    plt.show()

if __name__ == "__main__":
    bst = BinarySearchTree()

    # Generate random search tasks
    search_tasks = generate_random_search_tasks()

    # Measure performance and balance
    performance, max_balance_values = measure_performance_and_balance(bst, search_tasks)

    # Plot scatterplot
    plot_scatterplot(max_balance_values, performance)
